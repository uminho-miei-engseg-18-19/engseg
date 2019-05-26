
import java.util.*;

public class WhileEx
{
  public static void main(String[] args)
  {
    Scanner console = new Scanner(System.in);
    int age;
    int total = 0;

    System.out.println("Insira 10 idades: ");
    for (int i = 0;i < 10; i++)
    {
      age = console.nextInt();
      total = total + age;
    }
    System.out.println("Média de idades: " + (float)total/10);
  }
}