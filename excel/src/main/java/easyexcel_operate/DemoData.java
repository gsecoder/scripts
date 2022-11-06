package easyexcel_operate;

import com.alibaba.excel.annotation.ExcelIgnore;
import com.alibaba.excel.annotation.ExcelProperty;
import lombok.Data;

import java.util.Date;

/**
 * @Author secoder
 * @File DemoData
 * @Time 2021-08-07 14:05
 * @Description
 */
@Data
public class DemoData {

    // 设置Excel表头
    @ExcelProperty("字符串标题")
    private String string;
    @ExcelProperty("日期标题")
    private Date date;
    @ExcelProperty("数字标题")
    private Double doubleData;

    /**
     * 忽略这个字段
     */
    @ExcelIgnore
    private String ignore;
}
