package sample;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import javax.script.ScriptException;

public class if_else_pb_builder {
	public static void main(String[] args) throws ScriptException, IOException {
		 StringBuilder sb = new StringBuilder();
		 Scanner s= new Scanner(System.in);
		 try {
		  String line =" ";
		 System.out.println("Enter the corresponding number near to the name of the operation which you would like to perform on the dataset");
		 System.out.println("0. Describe the data");
		 System.out.println("01. Describe the data visualy");
		 System.out.println("1. Normalise the words having same meaning  ");
		 System.out.println("2. Fill the missing values");
		 System.out.println("3. Normalize the datatype of individual column");
		 System.out.println("4. Drop the entire column which has full missing value");
		 System.out.println("5. Fill the misising values using Median"); 
		 System.out.println("6. Find the correlation among the columns using pearson method");
		 System.out.println("7. Count of total number of missing values");
		 System.out.println("8. Find the correlation");	
		 String param1 = s.next();
	     ProcessBuilder pb = new ProcessBuilder("/usr/bin/python", "/Users/suriyas/dataqual.py" , "" + param1);
	     Process p = pb.start();
	     BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
    	 while ((line = in.readLine()) != null){
    		 sb.append(line);
    		 sb.append("\n");
	     
		}
		 }
	     catch (Exception e) {
	            System.out.println(e);
		 }
		 System.out.println("value is : " + sb); 
}
}

