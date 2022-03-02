package deck;

import java.util.*;
import java.lang.Math;

class Deckofcards {

  void PrintCard(int card) {
    String[] cards = { "ACE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN",
        "KING" };
    String[] suits = { "SPADES", "HEARTS", "CLUBS", "DIAMONDS" };
    int a[] = new int[5];
    Random rand = new Random();
    int i;
    System.out.println("\n*****Computer*****");
    for (i = 0; i < 5; i++) {
      a[i] = Math.abs(rand.nextInt(52) - 1);
      System.out.println(cards[(a[i] % 13)] + " of " + suits[(a[i] / 13)]);
    }

    System.out.println("\n*****Player*****");
    for (i = 0; i < 5; i++) {
      a[i] = Math.abs(rand.nextInt(52) - 1);
      System.out.println(cards[(a[i] % 13)] + " of " + suits[(a[i] / 13)]);
    }
  }

  public static void main(String[] args) {
    Deckofcards d = new Deckofcards();
    d.PrintCard(0);
    d.PrintCard(1);
    d.PrintCard(2);
    d.PrintCard(3);
    d.PrintCard(4);
    d.PrintCard(5);
    d.PrintCard(6);
    d.PrintCard(7);
    d.PrintCard(8);
    d.PrintCard(9);
  }

}