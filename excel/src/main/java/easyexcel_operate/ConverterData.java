package easyexcel_operate;

import com.alibaba.excel.annotation.ExcelProperty;
import com.alibaba.excel.annotation.format.DateTimeFormat;
import com.alibaba.excel.annotation.format.NumberFormat;
import lombok.Data;

import java.util.Date;

/**
 * @Author secoder
 * @File ConverterData
 * @Time 2021-08-09 23:53
 * @Description
 */
@Data
public class ConverterData {

    /**
     * 想所有的 字符串起前面加上"自定义："三个字
     */
    @ExcelProperty(value = "字符串标题")
    private String string;

    /**
     * excel 用年月日的格式
     */
    @DateTimeFormat("yyyy年MM月dd日HH时mm分ss秒")
    @ExcelProperty("日期标题")
    private Date date;

    /**
     * excel 用百分比表示
     */
    @NumberFormat("#.##%")
    @ExcelProperty(value = "数字标题")
    private Double doubleData;
}
