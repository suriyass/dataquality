package sample;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

import javax.script.ScriptException;

public class pb {
	public static void main(String[] args) throws ScriptException, IOException {
		 StringBuilder sb = new StringBuilder();


		 try {
		  String line =" ";
		 Scanner s= new Scanner(System.in);
		 System.out.println("Enter the corresponding number near to the name of the operation which you would like to perform on the dataset");
		 System.out.println("1. Count of missing value total");
		 System.out.println("2. normalize the data type");
		 System.out.println("3. Fill the missing values");
		 System.out.println("4. Drop the entire colum which has full values as missing value");
		 String param1 = s.next();
		 String param2 = s.next();
		 String param3 = s.next();
	     ProcessBuilder pb = new ProcessBuilder("/usr/bin/python", "/Users/suriyas/test5.py", "" + param1, "" + param2, "" + param3);
	     Process p = pb.start();
	     BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
	    
		String line1;
		while ((line = in.readLine()) != null){
	    // int ret = new Integer(in.readLine()).intValue();
	     sb.append(line);
	     sb.append("\n");
	     //System.out.println("value is : " + ret); 
		}
	     
	         
		 }
	     catch (Exception e) {
	            System.out.println(e);
		 }
		 System.out.println("value is : " + sb); 
}
}


