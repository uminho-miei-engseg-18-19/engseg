
import java.util.*;

public class Input {
    public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);

    int sz = getArraySize(scan);
    String[] names = getNames(scan,sz);

    int which = getWhich(scan);
    String aName = getName(which,names);

    System.out.println("Nome escolhido: "+aName);
  }

  public static int getArraySize(Scanner scan) {
    System.out.print("Quantos nomes? ");
    int n =  scan.nextInt();
    scan.nextLine();
    return n;
  }

  public static String[] getNames(Scanner scan, int sz) {
    String[] names = new String[sz];
    for (int i = 0; i < sz; i++ ){
      System.out.print("Insira nome #"+(i+1)+": ");
      names[i] = scan.nextLine();
    }
    return names;
  }

  public static int getWhich(Scanner scan) {
    System.out.print("Escolha o nome #: ");
    int x = scan.nextInt();
    return x;
  }

  public static String getName(int n,String[] vals) {
      return vals[n-1];
  }
}