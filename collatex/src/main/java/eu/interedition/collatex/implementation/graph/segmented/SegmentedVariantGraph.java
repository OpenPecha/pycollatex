/**
 * CollateX - a Java library for collating textual sources,
 * for example, to produce an apparatus.
 *
 * Copyright (C) 2010 ESF COST Action "Interedition".
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

package eu.interedition.collatex.implementation.graph.segmented;

import org.jgrapht.experimental.dag.DirectedAcyclicGraph;

import eu.interedition.collatex.implementation.graph.VariantGraphEdge;
import eu.interedition.collatex.interfaces.IVariantGraphEdge;


/*************
 * 
 * @author ronald
 * This class is intended to be like a VariantGraph, only the difference is that parallel segmentation
 * is applied
 * So that VariantGraphVertices contain Phrases instead of Tokens!
 * This class has a strong relation with JGraph
 * It might be a good idea to merge the two in the future!
 */
@SuppressWarnings("serial")
public class SegmentedVariantGraph extends DirectedAcyclicGraph<ISegmentedVariantGraphVertex, IVariantGraphEdge> implements ISegmentedVariantGraph {
    private ISegmentedVariantGraphVertex endVertex;
    
	public SegmentedVariantGraph() {
		super(VariantGraphEdge.class);
	}

  @Override
  public ISegmentedVariantGraphVertex getEndVertex() {
    return endVertex;
  }

  protected void setEndVertex(ISegmentedVariantGraphVertex endVertex) {
    this.endVertex = endVertex;
  }

}