package poi_excel;

import org.junit.Test;

import java.io.IOException;

/**
 * @Author secoder
 * @File ExcelWriteTest
 * @Time 2021-08-04 20:32
 * @Description
 */
public class ExcelWriteTest {
	
	ExcelWrite excelWrite = new ExcelWrite();
	/**
		File directory = new File("");
		String customFile;
		
		{
			try {
				customFile = directory.getCanonicalPath();
				System.out.println("customFile: " + customFile);
				System.out.println("测试：" + System.getProperty("java.class.path"));
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	 */
	
	String excel_path = "src/main/java/excel_data/";
	
	@Test
	public void write2003Test(){
		try {
			excelWrite.write2003(excel_path);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	@Test
	public void write2007Test(){
		try {
			excelWrite.write2007(excel_path);
		} catch (IOException e){
			e.printStackTrace();
		}
	}
	
	@Test
	public void write2003BigDataTest(){
		try {
			excelWrite.write2003BigData(excel_path);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	@Test
	public void write2007BigDataTest(){
		try {
			excelWrite.write2007BigData(excel_path);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	@Test
	public void write2007BigDataSXSSFTest(){
		try {
			excelWrite.write2007SXSSF(excel_path);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
