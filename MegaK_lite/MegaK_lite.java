default com.company;
import java.util.Scanner;
import java.lang.String;
public class Main {
	public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
	    Scanner scanChar = new Scanner(System.in);
		int x, y;
		String q;
		x = scan.nextInt();
		q = scanChar.nextLine();
	    y = scan.nextInt();
        switch (q) {
	        case "+":
	            System.out.println(x+y);
	            break;
	        case "-":
	            System.out.println(x-y);
	            break;
	        case "*":
	            System.out.println(x*y);
	            break;
	        case "/":
	            System.out.println(x/y);
	            break;
	        default:
	            System.out.println(x%y);
	    }
	}
}
