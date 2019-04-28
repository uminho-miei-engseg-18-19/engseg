
public class LOverflow
 {
  public static void main(String[] args)
  {
    int importantData =1;
    int[]  buffer = new int[10];

    for (int i =0; i < 500; i++) {  
      buffer[i] = 7;
      System.out.println("i = "+i);
    }

    System.out.println("after buffer overflow ");
    System.out.println("Important data  = "+importantData);
  }
}
