package car_three;

public class Car {
	
	private char color;
	private boolean ignition;
	private int x_coord; 
	private int y_coord; 
	
	
	public Car()
	{
		
		
		int number = (int) (Math.random()*5);
		if(number ==1) 
			this.color = 'R';
		else if(number==0) 
			this.color = 'G';
		else if(number==2) 
			this.color = 'B';
		else if(number==3) 
			this.color = 'W';
		else if(number==4) 
			this.color = 'S';
			
		this.ignition = false;

		int random_x = (int) (Math.random() * 20)+1;
		this.x_coord = random_x;
		
		int random_y = (int) (Math.random() * 20)+1;
		this.y_coord = random_y;
		
		
	}
	
	public char getColorCar()
	{
		return this.color = color;
	}


	public String getColor() {
		switch(this.color){
			case('R'):
				return "Red";
			case('W'):
				return "White";
			case('G'):
				return "Green";
			case('B'):
				return "Blue";
			case('S'):
				return "Silver";
		}
		return null;
		
		
	}


	public char assignColor() {
		int number = (int) (Math.random()*5);
		if(number==1) 
			this.color = 'R';
		else if(number==0) 
			this.color = 'G';
		else if(number==2) 
			this.color = 'B';
		else if(number==3) 
			this.color = 'W';
		else if(number==4) 
			this.color = 'S';
		return this.color;
	}


	public boolean getIgnition() {
		return this.ignition;
	}


	public void ignitionSwitch() {
		if(this.ignition)
			this.ignition = false;
		else
			this.ignition = true;
	}


	public int getX() {
		return this.x_coord;
	}


	public void moveVertical(int spaces) {
		int temp = this.y_coord + spaces;
		if(!ignition) 
			System.out.print("Ignition is off");
		else 
			if(temp <= 20 && temp >=1) 
				this.y_coord = temp;
			else
				System.out.println("Bad, out of BOUNDS!");
		}
	


	public int getY() {
		return this.y_coord;
	}
	
	


	public void moveHorizontal(int spaces) {
		int temp = this.x_coord + spaces;
		if(!ignition) 
			System.out.println("Ignition is off");
		else
			if(temp <= 20 && temp >=1) 
				this.x_coord = temp;
			else
				System.out.println("Bad, out of BOUNDS!");
		}
	
	
	
	
	}
	
	
	
	
	
	
	
	

	

