package timeDifference;
import java.util.Scanner;


public class timeDifference {
	
	public static void main(String args[]) {
	
	Scanner number = new Scanner(System.in);
	
	System.out.println("Enter the first number:");
	int number1 = number.nextInt();
			
	System.out.println("Enter the second number:");
	int number2 = number.nextInt();
	
	int h1 = number1/10000;
	int h2 = number2/10000;
	
	int m1 = (number1/100%100);
	int m2 = (number2/100%100);
	
	int s1 = number1%100;
	int s2 = number2%100;
	
	int total1 = (h1 * 3600) + (m1 * 60) + s1 ;
	int total2 = (h2 * 3600) + (m2 * 60) + s2 ;
	
	int times =  total2 - total1;
	
	int hh = (times/3600)*10000;
	int mm = ((times%3600)/60) * 100;
	int ss = (times%3600)%60;
	
	
	int diff = (hh+mm+ss) * (-1);
	System.out.println(diff);
	




	
	
	
	}

}
