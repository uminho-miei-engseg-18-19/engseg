
import java.io.*;  // File
import java.util.*;  // Scanner

public class ReadTemps
{
    public static void main (String[] args) throws FileNotFoundException
    {
      Scanner inFile = new Scanner(new File("/tmp/temps.txt"));  
      double[] temps = new double[10];
      int numTemps = 0;

      while (inFile.hasNextDouble())
      {
        temps[numTemps] = inFile.nextDouble();
        numTemps++;
      }
      System.out.println("Foram lidas " + numTemps + " temperaturas.");

    }
}