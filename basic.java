import java.util.Scanner;
public class demo{
    public static void main(String args[]){
      Scanner sc =new Scanner(System.in);
      System.out.println("Enter the Number:");
      int n=sc.nextInt();
        for(int i=0;i<=n;i++)
        {
            if(i==n)
            {
            System.out.println(n);
            }
        }
    }
}