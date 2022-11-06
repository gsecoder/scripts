package easyexcel_operate;

import com.alibaba.excel.EasyExcel;
import com.alibaba.excel.ExcelWriter;
import com.alibaba.excel.write.metadata.WriteSheet;
import org.junit.Test;

import java.io.InputStream;
import java.util.*;

/**
 * @Author secoder
 * @File EasyExcelDataTest
 * @Time 2021-08-07 14:14
 * @Description
 */
public class EasyExcelWriteTest {

    String excel_path = "src/main/java/excel_data/";

    private List<DemoData> data() {
        List<DemoData> list = new ArrayList<DemoData>();
        for (int i = 0; i < 10; i++) {
            DemoData data = new DemoData();
            data.setString("字符串" + i);
            data.setDate(new Date());
            data.setDoubleData(0.56);
            list.add(data);
        }
        return list;
    }

    /**
     * 简单的写
     */
    @Test
    public void simpleWriteTest() {
        // 写法一
        String fileName = excel_path + "simpleWriteExcel.xlsx";
        // 这里 需要指定写用哪个class去写，然后写到第一个sheet，名字为模板 然后文件流会 自动关闭
        // 如果这里想使用03 则 传入excelType参数即可
        EasyExcel.write(fileName, DemoData.class).sheet("sheet页").doWrite(data());
    }

    /**
     * 根据参数只导出指定列
     *      <p>1.创建excel对应的实体对象 参照{@link DemoData}</p>
     *      <p>2.根据自己或者排除自己需要的列</p>
     *      <p>3.直接写即可</p>
     */
    @Test
    public void excludeOrIncludeWrite() {
        // 被操作的Excel文件
        String fileName = excel_path + "excludeOrIncludeWriteExcel.xlsx";

        // 根据用户传入字段 假设我们要忽略 date
        Set<String> excludeColumnFiledNames = new HashSet<String>();
        excludeColumnFiledNames.add("date");

        // 这里需要指定写用哪个class去写，然后写到第一个sheet，名字为模板 然后文件流会自动关闭
        EasyExcel.write(fileName, DemoData.class).excludeColumnFiledNames(excludeColumnFiledNames).sheet("sheet").doWrite(data());
    }

    /**
     * <h3>指定列写入</h3>
     *      <p>1.创建excel对应的实体对象 参照{@link IndexData} </p>
     *      <p>2.使用{@link ExcelProperty}注解指定写入的列</p>
     *      <p>3.直接写即可</p>
     */
    @Test
    public void indexWriteTest(){
        String fileName = excel_path + "indexWriteExcel.xlsx";
        EasyExcel.write(fileName, IndexData.class).sheet("模板").doWrite(data());
    }


    /**
     * <h3>复杂头希尔</h3>
     *      <p>1.创建Excel对象的实体对象，参照{@link ComplexHeadData}</p>
     *      <p>2.使用{@link ExcelProperty}注解指定复杂的头</p>
     *      <p>3.直接写即可</p>
     */
    @Test
    public void complexHeadWriteTest() {
        String fileName = excel_path + "complexHeadWrite.xlsx";
        EasyExcel.write(fileName, ComplexHeadData.class).sheet("模板").doWrite(data());
    }

    /**
     * <h3>重复多次写入</h3>
     *      <p>1.创建Excel对应的实体对象，参照{@link ComplexHeadData}</p>
     *      <p>2.使用{@link com.alibaba.excel.annotation.ExcelProperty}注解指定复杂的头</p>
     *      <p>3.直接调用二次写入即可</p>
     */
    @Test
    public void repeatedWriteTest() {
        /**
         * <h3>方法一：如果写到同一个sheet</h3>
         */
        String fileName = excel_path + "repeatedWriteOneSheet.xlsx";
        ExcelWriter excelWriter = null;
        try {
            // 这里需要指定用哪个class去写
            excelWriter = EasyExcel.write(fileName, DemoData.class).build();
            // 注意：如果同一个sheet只要创建一次
            WriteSheet writeSheet = EasyExcel.writerSheet("模板").build();
            // 调用写入，实际开发中根据数据库的分页的总的椰树来
            for (int i = 0; i < 5; i++) {
                // 分页去数据库查询数据，这里可以去数据库查询每一页的数据
                List<DemoData> data = data();
                excelWriter.write(data, writeSheet);
            }
        } finally {
            // 关闭流
            if (excelWriter != null){
                excelWriter.finish();
            }
        }

        /**
         * <h3>方法二：如果写到不同的sheet 同一个对象</h3>
         */
        fileName = excel_path + "repeatedWriteDiffSheet.xlsx";
        try {
            // 这里 指定文件
            excelWriter = EasyExcel.write(fileName, DemoData.class).build();
            // 去调用写入,这里我调用了五次，实际使用时根据数据库分页的总的页数来。这里最终会写到5个sheet里面
            for (int i = 0; i < 5; i++) {
                // 每次都要创建writeSheet 这里注意必须指定sheetNo 而且sheetName必须不一样
                WriteSheet writeSheet = EasyExcel.writerSheet(i, "模板" + i).build();
                // 分页去数据库查询数据 这里可以去数据库查询每一页的数据
                List<DemoData> data = data();
                excelWriter.write(data, writeSheet);
            }
        } finally {
            // 千万别忘记finish 会帮忙关闭流
            if (excelWriter != null) {
                excelWriter.finish();
            }
        }

        /**
         * <h3>方法3 如果写到不同的sheet 不同的对象</h3>
         */
        fileName = excel_path + "repeatedWriteDiffSheetDiffObject.xlsx";
        try {
            // 这里 指定文件
            excelWriter = EasyExcel.write(fileName).build();
            // 去调用写入,这里我调用了五次，实际使用时根据数据库分页的总的页数来。这里最终会写到5个sheet里面
            for (int i = 0; i < 5; i++) {
                // 每次都要创建writeSheet 这里注意必须指定sheetNo 而且sheetName必须不一样。这里注意DemoData.class 可以每次都变，我这里为了方便 所以用的同一个class 实际上可以一直变
                WriteSheet writeSheet = EasyExcel.writerSheet(i, "模板" + i).head(DemoData.class).build();
                // 分页去数据库查询数据 这里可以去数据库查询每一页的数据
                List<DemoData> data = data();
                excelWriter.write(data, writeSheet);
            }
        } finally {
            // 千万别忘记finish 会帮忙关闭流
            if (excelWriter != null) {
                excelWriter.finish();
            }
        }
    }


    /**
     * 日期、数字或者自定义格式转换
     * <p>1. 创建excel对应的实体对象 参照{@link ConverterData}
     * <p>2. 使用{@link ExcelProperty}配合使用注解{@link DateTimeFormat}、{@link NumberFormat}或者自定义注解
     * <p>3. 直接写即可
     */
    @Test
    public void converterWriteTest(){
        String fileName = excel_path + "converterWrite.xlsx";
        EasyExcel.write(fileName, ConverterData.class).sheet("模板").doWrite(data());
    }


    /**
     * 图片导出
     * <p>
     * 1. 创建excel对应的实体对象 参照{@link ImageData}
     * <p>
     * 2. 直接写即可
     */
    @Test
    public void imageWriteTest() throws Exception {
        String fileName = excel_path + "imageWrite.xlsx";
        // 如果使用流 记得关闭
        InputStream inputStream = null;
    }

    /**
     * <h3>根据模板写入</h3>
     *      <p>1. 创建excel对应的实体对象 参照{@link IndexData}
     *      <p>2. 使用{@link ExcelProperty}注解指定写入的列
     *      <p>3. 使用withTemplate 写取模板
     *      <p>4. 直接写即可
     */
    @Test
    public void templateWriteTest() {
        String templateFileName = excel_path + "demo.xlsx";
        String fileName = excel_path + "templateWrite.xlsx";
        EasyExcel.write(fileName, DemoData.class).withTemplate(templateFileName).sheet().doWrite(data());
    }


    /**
     * 列宽、行高
     * <p>1. 创建excel对应的实体对象 参照{@link WidthAndHeightData}
     * <p>2. 使用注解{@link ColumnWidth}、{@link HeadRowHeight}、{@link ContentRowHeight}指定宽度或高度
     * <p>3. 直接写即可
     */
    @Test
    public void widthAndHeightWriteTest() {
        String fileName = excel_path + "widthAndHeightWrite.xlsx";
        // 这里 需要指定写用哪个class去写，然后写到第一个sheet，名字为模板 然后文件流会自动关闭
        EasyExcel.write(fileName, WidthAndHeightData.class).sheet("模板").doWrite(data());
    }
}
