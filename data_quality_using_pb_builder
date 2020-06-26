package sample;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

public class pb_builder {
	public static void main(String a[]) throws IOException, InterruptedException{
		StringBuilder sb = new StringBuilder();
		try{
		ProcessBuilder pb = new ProcessBuilder(Arrays.asList("/usr/bin/python", "/Users/suriyas/dataquality.py"));
   		 Process p = pb.start();
   		 BufferedReader bfr = new BufferedReader(new InputStreamReader(p.getInputStream()));
   		 String line = "";
         System.out.println("Running Python starts: " + line);
         int exitCode = p.waitFor();
         System.out.println("Exit Code : "+exitCode);
            while ((line = bfr.readLine()) != null){
            	sb.append(line);
            	sb.append("\n");

            }

        }catch(Exception e){System.out.println(e);}
		System.out.println(sb);
		        }
		    }
		


		



package sample;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

public class pb_builder {
	public static void main(String a[]) throws IOException, InterruptedException{
		StringBuilder sb = new StringBuilder();
		try{
		ProcessBuilder pb = new ProcessBuilder(Arrays.asList("/usr/bin/python", "/Users/suriyas/dataquality.py"));
   		 Process p = pb.start();
   		 BufferedReader bfr = new BufferedReader(new InputStreamReader(p.getInputStream()));
   		 String line = "";
         System.out.println("Running Python starts: " + line);
         int exitCode = p.waitFor();
         System.out.println("Exit Code : "+exitCode);
            while ((line = bfr.readLine()) != null){
            	sb.append(line);
            	sb.append("\n");

            }

        }catch(Exception e){System.out.println(e);}
		System.out.println(sb);
		        }
		    }
		


		



