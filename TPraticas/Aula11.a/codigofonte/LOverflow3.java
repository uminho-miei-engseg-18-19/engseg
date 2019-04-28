

import java.util.Scanner;

public class LOverflow3 {
  public static void main(String[] args) {

    Scanner scan = new Scanner(System.in);
    int[] vals = new int[10];

    System.out.println("Quantos valores quer guardar no array? ");
    int count = scan.nextInt();

    for (int i = 0; i < count; i++ ) {
      vals[i] = count-i;
    }

    System.out.println("Que valor deseja recuperar? ");
    int which = scan.nextInt();

    System.out.println("O valor é " +vals[which]);
  }
}
