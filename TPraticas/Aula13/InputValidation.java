
import java.util.Scanner;

public class InputValidation {

  public static void main(String[] args) {
    int[] vals = new int[10];

    for (int i = 0; i < 10; i++) {
      vals[i] = (i+1)*(i+1);
    }

    System.out.print("Insira um número: ");
    Scanner sc = new Scanner(System.in);
    int which = sc.nextInt();

    int square = vals[which-1];
    System.out.println("O quadrado de "+which+" é "+square);
  }
}
