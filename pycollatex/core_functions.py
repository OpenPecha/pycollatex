"""
Created on May 3, 2014

@author: Ronald Haentjens Dekker
"""
from xml.etree import ElementTree as etree
from xml.dom.minidom import Document
from collections import defaultdict
from pycollatex.core_classes import Collation, VariantGraph, join, AlignmentTable, VariantGraphRanking
from pycollatex.exceptions import SegmentationError
from pycollatex.experimental_astar_aligner import ExperimentalAstarAligner
import json
from pycollatex.edit_graph_aligner import EditGraphAligner
from pycollatex.near_matching import perform_near_match


# Valid options for output are:
# "table" for the alignment table (default)
# "graph" for the variant graph
# "json" for the alignment table exported as JSON
# "csv", "tsv" for CSV and TSV output
# "xml" for the alignment table as pseudo-TEI XML
#   All columns are output as <app> elements, regardless of whether they have variation
#   Each witness is in a separate <rdg> element with the siglum in a @wit attribute
#       (i.e, witnesses with identical readings are nonetheless in separate <rdg> elements)
def collate(collation, output="table", layout="horizontal", segmentation=True, near_match=False, astar=False,
            detect_transpositions=False, debug_scores=False, properties_filter=None, indent=False):
    # collation may be collation or json; if it's the latter, use it to build a real collation
    if isinstance(collation, dict):
        json_collation = Collation()
        for witness in collation["witnesses"]:
            json_collation.add_witness(witness)
        collation = json_collation

    # assume collation is collation (by now); no error trapping
    if not astar:
        algorithm = EditGraphAligner(collation, near_match=False, detect_transpositions=detect_transpositions,
                                     debug_scores=debug_scores, properties_filter=properties_filter)
    else:
        algorithm = ExperimentalAstarAligner(collation, near_match=False, debug_scores=debug_scores)

    # build graph
    graph = VariantGraph()
    algorithm.collate(graph)
    ranking = VariantGraphRanking.of(graph)
    if near_match:
        # Segmentation not supported for near matching; raise exception if necessary
        # There is already a graph ('graph', without near-match edges) and ranking ('ranking')
        if segmentation:
            raise SegmentationError('segmentation must be set to False for near matching')
        ranking = perform_near_match(graph, ranking)

    # join parallel segments
    if segmentation:
        join(graph)
        ranking = VariantGraphRanking.of(graph)
    # check which output format is requested: graph or table
    if output == "graph":
        return graph
    # create alignment table
    table = AlignmentTable(collation, graph, layout, ranking)
    if output == "json":
        return export_alignment_table_as_json(table)
    if output == "table":
        return table
    if output == "xml":
        return export_alignment_table_as_xml(table)
    else:
        raise Exception("Unknown output type: " + output)


def export_alignment_table_as_json(table, indent=None, status=False):
    json_output = {"table": []}
    sigli = []
    for row in table.rows:
        sigli.append(row.header)
        json_output["table"].append(
            [[listItem.token_data for listItem in cell] if cell else None for cell in row.cells])
    json_output["witnesses"] = sigli
    if status:
        variant_status = []
        for column in table.columns:
            variant_status.append(column.variant)
        json_output["status"] = variant_status
    return json.dumps(json_output, sort_keys=True, indent=indent, ensure_ascii=False)


def export_alignment_table_as_xml(table):
    readings = []
    for column in table.columns:
        app = etree.Element('app')
        for key, value in sorted(column.tokens_per_witness.items()):
            child = etree.Element('rdg')
            child.attrib['wit'] = "#" + key
            child.text = "".join(str(item.token_data["t"]) for item in value)
            app.append(child)
        # Without the encoding specification, outputs bytes instead of a string
        result = etree.tostring(app, encoding="unicode")
        readings.append(result)
    return "<root>" + "".join(readings) + "</root>"