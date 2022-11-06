package poi_excel;

import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

/**
 * @Author secoder
 * @File ExcelRead
 * @Time 2021-08-06 10:18
 * @Description
 */
public class ExcelRead {
	
	/**
	 * 2003版本读取xls文件
	 * @param path
	 * @throws IOException
	 */
	public void read2003(String path) throws IOException {
		
		// 新建一个文件输入流，读取我们要读取的文件
		InputStream inputStream = new FileInputStream(path + "custom_2003.xls");
		
		// 创建工作簿读取文件输入流
		Workbook workbook = new HSSFWorkbook(inputStream);
		// 读取工作簿中文件的第1sheet页
		Sheet sheet = workbook.getSheetAt(0);
		
		// 读取第一行第一列
		Row row = sheet.getRow(0);
		Cell cell = row.getCell(0);
		
		// 输出单元格
		System.out.println(cell.getStringCellValue());
		
		// 操作完毕关闭文件输入流
		inputStream.close();
	}
	
	/**
	 * 2007版本读取xlsx文件
	 * @param path
	 * @throws IOException
	 */
	public void read2007(String path) throws IOException {
		
		// 新建一个文件输入流，读取我们要读取的文件
		InputStream inputStream = new FileInputStream(path + "custom_2007.xlsx");
		
		// 创建工作簿读物文件输入流
		Workbook workbook = new XSSFWorkbook(inputStream);
		// 读物第一sheet页
		Sheet sheet = workbook.getSheetAt(0);
		
		// 读取第一行第一列
		Row row = sheet.getRow(0);
		Cell cell = row.getCell(0);
		
		// 输出单元格
		System.out.println(cell.getStringCellValue());
		
		// 操作完毕后关闭文件输入流
		inputStream.close();
	}
}
