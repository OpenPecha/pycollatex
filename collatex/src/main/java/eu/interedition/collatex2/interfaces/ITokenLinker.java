package eu.interedition.collatex2.interfaces;

import java.util.Comparator;
import java.util.Map;


public interface ITokenLinker {

  Map<INormalizedToken, INormalizedToken> link(IWitness graph, IWitness b, Comparator<INormalizedToken> comparator);

}