package easyexcel_operate;

import com.alibaba.excel.annotation.ExcelProperty;
import com.alibaba.excel.annotation.write.style.ColumnWidth;
import com.alibaba.excel.annotation.write.style.ContentRowHeight;
import com.alibaba.excel.converters.string.StringImageConverter;
import lombok.Data;

import java.io.File;
import java.io.InputStream;
import java.net.URL;

/**
 * @Author secoder
 * @File ImageData
 * @Time 2021-08-10 00:14
 * @Description
 */
@Data
@ContentRowHeight(100)
@ColumnWidth(100 / 8)
public class ImageData {
    private File file;
    private InputStream inputStream;
    /**
     * 如果string类型 必须指定转换器，string默认转换成string
     */
    @ExcelProperty(converter = StringImageConverter.class)
    private String string;
    private byte[] byteArray;
    /**
     * 根据URL导出
     */
    private URL url;
}
