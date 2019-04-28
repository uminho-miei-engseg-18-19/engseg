
import java.util.Scanner;

public class IntegerError {

  public static void main(String[] args) {

    Scanner scan = new Scanner(System.in);
    // variáveis
    int i;
    int j;
    int result;

    System.out.println("Maior inteiro: "+Integer.MAX_VALUE);
    System.out.println("Menor inteiro: "+Integer.MIN_VALUE);

    System.out.print("Input de dois valores inteiros: ");
    i = scan.nextInt();
    j = scan.nextInt();

    System.out.println("\nValores entrados: ");
    System.out.println("Inteiros: "+ i + " " + j);

    result =  i * 10;
    System.out.println("Multiplicação do primeiro número por dez: "+result);
    result =  i + j;
    System.out.println("Soma dos dois números: "+result);
    result =  i * j;
    System.out.println("Produto dos dois números: "+result);
 
  }
}
