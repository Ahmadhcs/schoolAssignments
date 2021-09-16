package car_three;
import java.util.Scanner;




public class car_three {
	


	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String inputs = "haha";
		
		
		Car[] Cars = new Car[10];
		for(int i=0; i <Cars.length; i++)
			Cars[i] = new Car();
		
		System.out.print("Enter a number between 1-10 to select a car: ");
		int car_number = input.nextInt();
		
		while(car_number>10 || car_number<1)
		{
			System.out.print("Incorrect! Please enter a number between 1-10 to select a valid car: ");
			car_number = input.nextInt();
		}
		
		int movement;
		String pos = "";

		Cars[car_number-1] = new Car();
		loop:
		while(!inputs.equalsIgnoreCase("Q"))
		{
			System.out.println("What would you like to do?\n" + "1: Turn the ignition on/off\n" + "2: Change the position of the car\n" 	+ "3: Change cars\n"	+ "Q: Quit program\n");
			inputs = input.next();
			switch(inputs.toLowerCase()) {
			case "1":
				Cars[car_number-1].ignitionSwitch();
				break;
			case "2":
			{
				System.out.println("Vertical or horizontal");
				pos = input.next();
				while(!pos.equalsIgnoreCase("V") || !pos.equalsIgnoreCase("H"))//error handle this pleaseAhmad
					if(pos.equalsIgnoreCase("v"))
					{
						System.out.print("Enter Movement");
						movement = input.nextInt();
						Cars[car_number-1].moveVertical(movement);
						break;
						
					}else if(pos.equalsIgnoreCase("h")){
						System.out.print("Enter Movement");
						movement = input.nextInt();
						Cars[car_number-1].moveHorizontal(movement);
						break;
					}else {
						System.out.println("Vertical or horizontal");
						pos = input.next();
					}
				break;
			}
			case "3":
				System.out.print("what car number do you want to switch to");
				car_number = input.nextInt();
				
				break;
			case "q":
				break loop;
			
		}
		state(Cars[car_number-1], car_number);
	}
	}
	public static void state(Car Ahmad, int car_number) {
		System.out.println("Car #" + car_number);
		System.out.println("Information");
		System.out.println("Color: " + Ahmad.getColor());
		if(Ahmad.getIgnition())
			System.out.println("Ignition: On");
		else
			System.out.println("Ignition: Off");
		System.out.println("Location: (" + Ahmad.getX() + ","+ Ahmad.getY()+")");
		for(int i=1; i<=20;i++) {
			for(int y=1; y<=20;y++) {
				if (y == Ahmad.getX() & i == Ahmad.getY()) 
					System.out.print(Ahmad.getColorCar());
				else 
					System.out.print("-");
				}
			System.out.println("");
	}
	}

}

	
	
	


		


	
	
	
	


