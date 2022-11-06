package poi_excel;

import org.junit.Test;

import java.io.IOException;

/**
 * @Author secoder
 * @File ExcelReadTest
 * @Time 2021-08-06 10:36
 * @Description
 */
public class ExcelReadTest {
	
	ExcelRead excelRead = new ExcelRead();
	String excel_path = "src/main/java/excel_data/";
	
	@Test
	public void read2003Test(){
		try {
			excelRead.read2003(excel_path);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	@Test
	public void read2007Test(){
		try {
			excelRead.read2007(excel_path);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
