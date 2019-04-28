

import java.util.Scanner;

public class IntegerCheck {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int i;
    byte b;
    short sh;
    long lon;
    System.out.println("int válido   entre " + Integer.MIN_VALUE + " e " + Integer.MAX_VALUE );
    System.out.println("byte válido  entre " + Byte.MIN_VALUE + " e " + Byte.MAX_VALUE );
    System.out.println("short válido entre " + Short.MIN_VALUE + " e " + Short.MAX_VALUE );
    System.out.println("long válido  entre " + Long.MIN_VALUE + " e " + Long.MAX_VALUE );
  }
}
