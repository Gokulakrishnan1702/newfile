import java.util.*;

public class age{
    public static void main(String[] args)
  {
    Scanner obj = new Scanner(system.in);
    int age = obj.nextInt();    
    obj.close();  

try {
    validage(int);
     system.out.println("Valid age.");
}
catch (IllegalArgumentException e)
  {
    
    system.out.println("Error " + e.getMessage() );

  }
  public static void validage(int age) throw new IllegalArgumentException
   {
    if(age<18)
    {
        throw new IllegalArgumentException("Age must be above 18.");
    }

} }
}