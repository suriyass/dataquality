package sample;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class pb_for_rfr {

	public static void main(String[] args) throws IOException, InterruptedException {
		
		 StringBuilder sb = new StringBuilder();
		// TODO Auto-generated method stub
		try {
			ProcessBuilder pb = new ProcessBuilder("/usr/bin/python", "/Users/suriyas/test1.py ");
		     Process p = pb.start();
		     BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
		     int exitCode = p.waitFor();
	         System.out.println("Exit Code : "+exitCode);
		     String line = " ";
			 while ((line = in.readLine()) != null){
				sb.append(line);
			    sb.append("\n");
         }
	}catch(Exception e){System.out.println(e);}
		System.out.println("value is : " + sb); 
	        }
	    }
	

	


