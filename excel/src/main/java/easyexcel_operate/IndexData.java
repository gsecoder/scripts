package easyexcel_operate;

import com.alibaba.excel.annotation.ExcelProperty;
import lombok.Data;

import java.util.Date;

/**
 * @Author secoder
 * @File IndexData
 * @Time 2021-08-09 22:54
 * @Description
 */
@Data
public class IndexData {
    @ExcelProperty(value = "字符串标题", index = 0)
    private String string;

    @ExcelProperty(value = "日期标题", index = 1)
    private Date date;

    /**
     * 这里设置3，会导致第二列为空
     */
    @ExcelProperty(value = "第四列", index = 3)
    private Double doubleData;

}
