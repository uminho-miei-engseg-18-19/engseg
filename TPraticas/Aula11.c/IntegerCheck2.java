
import java.util.Scanner;

public class IntegerCheck2 {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int i;
    byte b;
    short sh;
    long lon;
    System.out.println("Int válido   entre " + Integer.MIN_VALUE + " e " + Integer.MAX_VALUE );
    System.out.println("Byte válido  entre " + Byte.MIN_VALUE + " e " + Byte.MAX_VALUE );
    System.out.println("Short válido entre " + Short.MIN_VALUE + " e " + Short.MAX_VALUE );
    System.out.println("Long válido  entre " + Long.MIN_VALUE + " e " + Long.MAX_VALUE );
    
    System.out.print("Insira valor Int: ");
    i = (int) scan.nextLong();
    System.out.print("Insira valor Byte: ");
    b = (byte) scan.nextLong();
    System.out.print("Insira valor Short: ");
    sh = (short) scan.nextLong();
    System.out.print("Insira valor Long: ");
    lon = (long) scan.nextLong();

    System.out.println("\nInseriu os seguintes valores: ");
    System.out.println("Int: " + i);
    System.out.println("Byte: " + b);
    System.out.println("Short: " + sh);
    System.out.println("Long: " + lon);
    
    i = Integer.MAX_VALUE + 1;
    System.out.println("Integer Overflow: " + Integer.MAX_VALUE + " + 1 = " +i);
  }
}
