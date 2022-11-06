package easyexcel_operate;

import com.alibaba.excel.EasyExcel;
import org.junit.Test;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

/**
 * @Author secoder
 * @File EasyExcelDataTest
 * @Time 2021-08-07 14:14
 * @Description
 */
public class EasyExcelReadTest {

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
     * 简单的读
     */
    @Test
    public void simpleReadTest() {
        String fileName = excel_path + "EasyExcel.xlsx";
        EasyExcel.read(fileName, DemoData.class, new DemoDataListener()).sheet().doRead();
    }
}
