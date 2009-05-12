package com.sd_editions.collatex.output;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

import com.sd_editions.collatex.permutations.Witness;
import com.sd_editions.collatex.permutations.WitnessBuilder;

public class AlignmentTable2Test {
  @Test
  public void testCreateSuperBase() {
    WitnessBuilder builder = new WitnessBuilder();
    Witness a = builder.build("A", "the first witness");
    AlignmentTable2 alignmentTable = new AlignmentTable2();
    alignmentTable.addFirstWitness(a);
    Witness superBase = alignmentTable.createSuperBase();
    assertEquals("the first witness", superBase.toString());
  }
}
