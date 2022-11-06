package poi_excel;

import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.streaming.SXSSFWorkbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.joda.time.DateTime;

import java.io.FileOutputStream;
import java.io.IOException;

/**
 * @Author secoder
 * @File ExcelWrite
 * @Time 2021-08-04 20:06
 * @Description
 */
public class ExcelWrite {
	
	// 注意：目录最后这里没有/，否则会报错找不到路径
	String excel_path = "../excel_data";
	
	/**
	 * target003版本写
	 * @param path
	 * @throws IOException
	 */
	public void write2003(String path) throws IOException {
		
		// 创建新的2003Excel工作簿
		Workbook workbook = new HSSFWorkbook();
		
		// 在Excel工作簿中新建一个工作表（sheet），其名为缺省值sheet0
		//Sheet sheet = workbook.createSheet();
		// 指定sheet名创建新的sheet
		Sheet sheet = workbook.createSheet("自定义2003_sheet页");
		
		// 创建行（row 1）
		Row row1 = sheet.createRow(0);
		// 创建单元格（col 1-1），并填充字符串值
		Cell cell11 = row1.createCell(0);
		cell11.setCellValue("这是个字符串");
		// 创建单元格（col 1-2），并填充数字值
		Cell cell12 = row1.createCell(1);
		cell12.setCellValue(999);
		
		// 创建行（row 2）
		Row row2 = sheet.createRow(1);
		// 创建单元格（col 2-1），并填充字符串值
		Cell cell21 = row2.createCell(0);
		cell21.setCellValue("统计时间");
		// 创建单元格（col 2-2），并填充时间值
		Cell cell22 = row2.createCell(1);
		String dateTime = new DateTime().toString("yyyy-MM-dd HH:mm:ss");
		cell22.setCellValue(dateTime);
		
		// 新建一文件输出流（注意要先创建文件夹）
		FileOutputStream outputStream = new FileOutputStream(path + "custom_2003.xls");
		// 把相应的Excel工作簿存到磁盘
		workbook.write(outputStream);
		// 操作结束，关闭文件流
		outputStream.close();
		
		System.out.println("2003Excel文件生成成功");
	}
	
	
	public void write2007(String path) throws IOException {
		
		// 创建新的2007Excel工作簿
		Workbook workbook = new XSSFWorkbook();
		
		// 自定义创建的Excel工作簿中的sheet页
		Sheet sheet = workbook.createSheet("自定义2007_sheet页");
		
		// 创建行（row 1）
		Row row1 = sheet.createRow(0);
		// 创建单元格（col 1-1），并填充单元格值
		Cell cell11 = row1.createCell(0);
		cell11.setCellValue("1-1单元格");
		// 创建单元格（col 1-2），并填充值
		Cell cell12 = row1.createCell(1);
		cell12.setCellValue(1213);
		
		// 创建行（row 2）
		Row row2 = sheet.createRow(1);
		// 创建单元格（col 2-1）
		Cell cell21 = row2.createCell(0);
		cell21.setCellValue("2-1单元格");
		// 创建单元格（col 2-2）
		Cell cell22 = row2.createCell(1);
		cell22.setCellValue("2-2");
		
		// 新建文件输出流
		FileOutputStream fileOutputStream = new FileOutputStream(path + "custom_2007.xlsx");
		// 把Excel存储到磁盘中
		workbook.write(fileOutputStream);
		// 关闭数据流
		fileOutputStream.close();
		
		System.out.println("2007Excel文件生成成功");
	}
	
	/**
	 * 大文件写HSSF-2003
	 * 缺点：最多只能处理65536行，否则会抛出异常
	 * 		java.lang.IllegalArgumentException: Invalid row number (65536) outside
	 * 		allowable range (0..65535)	
	 * @throws IOException
	 */
	public void write2003BigData(String path) throws IOException {
		
		// 记录开始时间
		long beginTime = System.currentTimeMillis();
		
		// 创建一个SxSSFworkbook
		Workbook workbook = new HSSFWorkbook();
		
		// 创建一个sheet
		Sheet sheet = workbook.createSheet();
		
		// xls文件最大支持65535行
		for (int rowNum = 0; rowNum < 65535; rowNum++){
			// 创建一个行
			Row row = sheet.createRow(rowNum);
			for (int cellNum = 0; cellNum < 10; cellNum++){
				Cell cell = row.createCell(cellNum);
				cell.setCellValue(cellNum);
			}
		}
		System.out.println("Done");
		
		// 创建文件输入流
		FileOutputStream fileOutputStream = new FileOutputStream(path + "2003bigData.xls");
		// 将相应的Excel工作存储到磁盘中
		workbook.write(fileOutputStream);
		// 关闭文件输入流
		fileOutputStream.close();
		
		// 记录结束时间
		long endTime = System.currentTimeMillis();
		System.out.println("整体耗时：" + (double) (endTime - beginTime)/1000); 
	}

	/**
	 * 大文件写XSSF -- 2007
	 * 缺点：写数据时速度非常慢，非常耗内存，也会发生内存溢出，如100万条
	 * 优点：可以写较大的数据量，如20万条
	 * @param path
	 * @throws IOException
	 */
	public void write2007BigData(String path) throws IOException {
		
		// 记录开始时间
		long startTime = System.currentTimeMillis();
		
		// 创建一个新的XSSFWorkbook
		Workbook workbook = new XSSFWorkbook();
		
		// 创建一个sheet
		Sheet sheet = workbook.createSheet();
		
		// xls文件最大支持65535行
		for (int rowNum=0; rowNum<100000; rowNum++){
			// 创建行
			Row row = sheet.createRow(rowNum);
			// 创建单元格
			for (int cellNum=0; cellNum<10; cellNum++){
				Cell cell = row.createCell(cellNum);
				cell.setCellValue(cellNum);
			}
		}
		System.out.println("Excel数据装填完成");
		
		// 创建文件输入流
		FileOutputStream fileOutputStream = new FileOutputStream(path + "2007BigData.xlsx");
		// 将Excel文件写入磁盘
		workbook.write(fileOutputStream);
		// 操作完毕关闭文件输入流
		fileOutputStream.close();
		
		// 记录结束时间
		long endTime = System.currentTimeMillis();
		// 计算生成2007大数据文件总耗时
		System.out.println("生成2007大数据文件总耗时：" + (double) (endTime - startTime)/1000);
	}

	/**
	 * 优点：可以写非常大的数据量，如100万条甚至更多条，写数据速度快，占用更少的内存
	 * 注意：
	 * 	过程中会产生临时文件，需要清理临时文件
	 * 	默认有100条记录保存在内存中，如果超过这个数量，则最前面的数据被写入临时文件
	 * 	如果想自定义内存中数据的数量，可以使用new SXSSFWorkbook(数量)
	 * @throws IOException
	 */
	public void write2007SXSSF(String path) throws IOException {

		// 记录开始时间
		long startTime = System.currentTimeMillis();

		// 创建一个SXSSFWorkbook
		Workbook workbook = new SXSSFWorkbook();

		// 创建一个sheet
		Sheet sheet = workbook.createSheet("SXSSFWorkbook");

		// 总行量
		for (int rowNum=0; rowNum<100000; rowNum++){
			// 创建行
			Row row = sheet.createRow(rowNum);
			for (int cellNum=0; cellNum<10; cellNum++){
				// 创建单元格
				Cell cell = row.createCell(cellNum);
				cell.setCellValue(cellNum);
			}
		}
		System.out.printf("Excel填充值");

		// 创建文件输入流
		FileOutputStream fileOutputStream = new FileOutputStream(path + "2007BigData_SXSSF.xlsx");
		// Excel文件输入到磁盘中
		workbook.write(fileOutputStream);
		// 关闭输入文件流
		fileOutputStream.close();

		// 清理临时文件
		((SXSSFWorkbook)workbook).dispose();

		// 记录结束时间
		long endTime = System.currentTimeMillis();
		System.out.println("总耗时：" + (double)(endTime-startTime)/1000);
	}
	
}
