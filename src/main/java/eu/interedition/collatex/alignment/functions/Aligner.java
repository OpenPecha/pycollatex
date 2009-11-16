package eu.interedition.collatex.alignment.functions;

import java.util.Collection;
import java.util.List;
import java.util.Set;

import com.google.common.collect.Lists;
import com.google.common.collect.Sets;

import eu.interedition.collatex.alignment.Alignment;
import eu.interedition.collatex.alignment.Gap;
import eu.interedition.collatex.alignment.Match;
import eu.interedition.collatex.alignment.MatchSequence;
import eu.interedition.collatex.alignment.UnfixedAlignment;
import eu.interedition.collatex.input.Segment;
import eu.interedition.collatex.input.Witness;
import eu.interedition.collatex.input.Word;
import eu.interedition.collatex.match.Matcher;

public class Aligner {

  public static Alignment<Word> align(final Witness a, final Witness b) {
    return align(a.getFirstSegment(), b.getFirstSegment());
  }

  public static Alignment<Word> align(final Segment a, final Segment b) {
    final UnfixedAlignment<Word> unfixedAlignment = Matcher.match(a, b);

    return align(a, b, unfixedAlignment);
  }

  public static Alignment<Word> align(final Segment a, final Segment b, final UnfixedAlignment<Word> unfixedAlignment) {
    UnfixedAlignment<Word> temp = unfixedAlignment;
    while (temp.hasUnfixedWords()) {
      temp = Aligner.permutate(a, b, temp);
    }
    final Alignment<Word> alignment = Alignment.create(temp.getFixedMatches(), a, b);
    return alignment;
  }

  public static UnfixedAlignment<Word> permutate(final Segment a, final Segment b, final UnfixedAlignment alignment) {
    final Collection<Match<Word>> unfixedMatches = getMatchesToPermutateWith(alignment);
    final List<UnfixedAlignment<Word>> alignments = getAlignmentsForUnfixedMatches(alignment, unfixedMatches);
    final UnfixedAlignment<Word> bestAlignment = selectBestPossibleAlignment(a, b, alignments);
    return bestAlignment;
  }

  private static Collection<Match<Word>> getMatchesToPermutateWith(final UnfixedAlignment<Word> alignment) {
    final Word nextBase = selectNextUnfixedWordToAlign(alignment);
    final Collection<Match<Word>> unfixedMatchesFrom = alignment.getMatchesThatLinkFrom(nextBase);
    final Word nextWitness = unfixedMatchesFrom.iterator().next().getWitnessWord();
    final Collection<Match<Word>> unfixedMatchesTo = alignment.getMatchesThatLinkTo(nextWitness);
    Collection<Match<Word>> unfixedMatches;
    if (unfixedMatchesFrom.size() > unfixedMatchesTo.size()) {
      unfixedMatches = unfixedMatchesFrom;
      //      System.out.println("next word that is going to be matched: (from a) " + nextBase + " at position: " + nextBase.position);
    } else {
      unfixedMatches = unfixedMatchesTo;
      //      System.out.println("next word that is going to be matched: (from b) " + nextWitness + " at position: " + nextWitness.position);
    }
    return unfixedMatches;
  }

  private static Word selectNextUnfixedWordToAlign(final UnfixedAlignment<Word> alignment) {
    // Check whether there are unfixed near matches.
    // Align them first!
    // Note: this is probably not generic enough!
    if (!alignment.getUnfixedNearMatches().isEmpty()) {
      final Word nextNearFromBase = alignment.getUnfixedNearMatches().iterator().next().getBaseWord();
      return nextNearFromBase;
    }

    final Set<Word> unfixedWords = alignment.getUnfixedWords();
    final Word nextBase = unfixedWords.iterator().next();
    return nextBase;
  }

  // TODO: naming here is not cool!
  private static List<UnfixedAlignment<Word>> getAlignmentsForUnfixedMatches(final UnfixedAlignment<Word> previousAlignment, final Collection<Match<Word>> unfixedMatches) {
    final List<UnfixedAlignment<Word>> permutationsForMatchGroup = Lists.newArrayList();
    for (final Match<Word> possibleMatch : unfixedMatches) {
      UnfixedAlignment<Word> alignment = previousAlignment.fixMatch(possibleMatch);
      alignment = fixTheOnlyOtherPossibleMatch(unfixedMatches, possibleMatch, alignment);
      permutationsForMatchGroup.add(alignment);
    }
    return permutationsForMatchGroup;
  }

  private static UnfixedAlignment<Word> fixTheOnlyOtherPossibleMatch(final Collection<Match<Word>> unfixedMatches, final Match<Word> possibleMatch, final UnfixedAlignment<Word> alignment) {
    UnfixedAlignment<Word> result = alignment;
    if (unfixedMatches.size() == 2) {
      final Set<Match<Word>> temp = Sets.newLinkedHashSet(unfixedMatches);
      temp.remove(possibleMatch);
      final Match<Word> matchToSearch = temp.iterator().next();
      final Set<Match<Word>> unfixedMatchesInNewAlignment = alignment.getUnfixedMatches();
      Match<Word> matchToFix = null;
      for (final Match<Word> matchToCheck : unfixedMatchesInNewAlignment) {
        if (matchToFix == null && (matchToCheck.getBaseWord().equals(matchToSearch.getBaseWord()) || matchToCheck.getWitnessWord().equals(matchToSearch.getWitnessWord()))) {
          matchToFix = matchToCheck;
        }
      }
      if (matchToFix != null) {
        //        System.out.println("Also fixed match " + matchToFix);
        result = alignment.fixMatch(matchToFix);
      }
    }
    return result;
  }

  // TODO: move all the collation creation out of the way!
  private static UnfixedAlignment<Word> selectBestPossibleAlignment(final Segment a, final Segment b, final List<UnfixedAlignment<Word>> alignments) {
    UnfixedAlignment bestAlignment = null;
    Alignment bestCollation = null;

    // TODO: add test for lowest number of matchsequences (transpositions)
    // NOTE: this can be done in a nicer way with the min function!
    for (final UnfixedAlignment alignment : alignments) {
      final Alignment collation = Alignment.create(alignment.getFixedMatches(), a, b);
      final List<Gap> nonMatches = collation.getGaps();
      final List<MatchSequence> matchSequences = collation.getMatchSequences();
      //      System.out.println(alignment.getFixedMatches().toString() + ":" + matchSequences.size() + ":" + nonMatches.size());
      if (bestAlignment == null || bestCollation == null || matchSequences.size() < bestCollation.getMatchSequences().size() || nonMatches.size() < bestCollation.getGaps().size()) {
        bestAlignment = alignment;
        bestCollation = Alignment.create(bestAlignment.getFixedMatches(), a, b);
      }
    }
    if (bestAlignment == null) throw new RuntimeException("Unexpected error!");
    return bestAlignment;
  }

}
