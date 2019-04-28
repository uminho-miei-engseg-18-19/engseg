
import java.util.Scanner;
public class LOverflow2
{
  public static void main(String[] args)
  {
    int[] tests = new int[10];
    int test;
    int count;
    Scanner scan = new Scanner(System.in);

    System.out.print("Quantos números? ");
    count = scan.nextInt();
    for (int i =0 ; i < count; i++)
    {
    	System.out.print("Introduza número: ");
   	test  = scan.nextInt();
    	tests[i]= test;
    }
  }
}
