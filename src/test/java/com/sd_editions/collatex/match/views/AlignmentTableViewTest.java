package com.sd_editions.collatex.match.views;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

import com.sd_editions.collatex.permutations.CollateCore;
import com.sd_editions.collatex.permutations.Modifications;

public class AlignmentTableViewTest {
  @Test
  public void testSimple() {
    String w1 = "a b";
    String w2 = "a b";
    String expected = "<xml>a b</xml>";
    assertEquals(expected, getGoing(w1, w2));
  }

  @Test
  public void testAddition() {
    String w1 = "a b";
    String w2 = "a c b";
    String expected = "<xml>a <app>c</app> b</xml>";
    assertEquals(expected, getGoing(w1, w2));
  }

  @Test
  public void testOmmission() {
    String w1 = "a c b";
    String w2 = "a b";
    String expected = "<xml>a <app>c</app> b</xml>";
    assertEquals(expected, getGoing(w1, w2));
  }

  public String getGoing(String w1, String w2) {
    // TODO: make a constructor for Witness, Witness
    //    Witness base = new Witness(w1);
    //    Witness witness = new Witness(w2);
    CollateCore core = new CollateCore(w1, w2);
    Modifications modifications = core.compareWitness(1, 2).get(0);
    AlignmentTable table = new AlignmentTable(modifications);
    String xml = table.toXML();
    return xml;
  }
}
