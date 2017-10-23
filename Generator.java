import java.util.List;
import java.io.File;
import java.io.FileOutputStream;
import java.util.ArrayList;
import java.util.Random;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;


public class Generator {
	
	private static String[] NAMES = {"Aakash Gupta", "Aastha Gupta", "Aayush Shende", "Aayush Mittal", "Abhishek Kainth",
								"Abhishek Kumar", "Abhishek Singh", "Aditi Sharma", "Akash Roy", "Akhil Malik",
								"Akhil Tomar", "Akshay Pilania", "Akshit Kwatra", "Aman", "Aman Priyadarshi",
								"Amar Malik", "Anand", "Aneesh Varma", "Anjana Shah", "Ankur Prasad",
								"Ankush Babbar", "Ann Mary George", "Anshul Gupta", "Anuj Yadav", "Anwesha Padhy",
								"Apar Madan", "Apoorva Sharma", "Apurva Singh", "Arko Gupta", "Arun Yadav",
								"Aryan Singh", "Ashita Dey", "Ashok Yadav", "Ayush Garg", "Ayush Pal",
								"Bhupain Singhmar", "Chaitanya Chawla", "Chetan Mithra", "Chhavi", "Deeheem Ansari",
								"Deeksha", "Deepak Rathi", "Deepanshu Pandey", "Deepika Naryani", "Devesh Saini",
								"Dhananjay Khanna", "Dinesh Agarwal", "Divya Panwar", "Divye Girotra", "Garimendra Verma",
								"Garvit Aggarwal", "Gaurav Prasad", "Gurneesh Singh Anand", "Gurtej Kochar", "Harshil Yadav",
								"Hemant Jadon", "Hitesh Kumar Mahour", "Inderpreet Singh Saggu", "Ipshita Chatterjee", "Isha",
								"Jaskirat Singh Arora" };
	private static final int MAX_CALLDUARTION = 100;
	private static final int MAX_SMSCOUNT = 30;
	private static final int MAX_WHATSAPPCOUNT = 200;
	private static final int MAX_MUTUALFRIENDS = 100;
	
	public static void main(String[] args) {
		
		//initialising the workbook 
		XSSFWorkbook workbook = new XSSFWorkbook();		
		XSSFSheet sheet = workbook.createSheet("Student Data");
		
		List<Object[]> data = new ArrayList<Object[]>();
        data.add(new Object[] {"S.No.", "Student1", "Student2", "Call Duration",
        							"FB Friend", "Mutual Friends", "SMS", "WhatsApp"});
        
        int Sno = 1;
        Random rand = new Random();
        for(int i = 0; i < NAMES.length; i++){
        	String Person1 = NAMES[i];
        	for(int j = i + 1; j < NAMES.length; j++){
        		String Person2 = NAMES[j];
        		data.add(new Object[] {Sno++, Person1, Person2, 
    					rand.nextInt(MAX_CALLDUARTION) + 1, rand.nextInt(2),
    					rand.nextInt(MAX_MUTUALFRIENDS) + 1, rand.nextInt(MAX_SMSCOUNT) + 1,
    					rand.nextInt(MAX_WHATSAPPCOUNT) + 1});
        	}
        }
        int Serial = Sno;
        int rownum = 0;
        for (Object[] objArr: data)
        {
            Row row = sheet.createRow(rownum++);
            int cellnum = 0;
            for (Object obj : objArr)
            {
               Cell cell = row.createCell(cellnum++);
               if(obj instanceof String)
                    cell.setCellValue((String)obj);
                else if(obj instanceof Integer)
                    cell.setCellValue((Integer)obj);
            }
        }
	//protecting the filestream
        try
        {
            FileOutputStream out = new FileOutputStream(new File("Student Data.xlsx"));
            workbook.write(out);
            out.close();
            workbook.close();
            System.out.println("Student Data.xlsx written successfully on disk.");
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
	}
}
