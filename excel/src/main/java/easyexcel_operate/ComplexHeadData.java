package easyexcel_operate;

import com.alibaba.excel.annotation.ExcelProperty;
import lombok.Data;

/**
 * @Author secoder
 * @File ComplexHeadData
 * @Time 2021-08-09 23:07
 * @Description
 */
@Data
public class ComplexHeadData {
    @ExcelProperty({"主标题", "字符串标题"})
    private String string;
    @ExcelProperty({"主标题", "日期标题"})
    private Data date;
    @ExcelProperty({"主标题", "数字标题"})
    private Double doubleData;
}
