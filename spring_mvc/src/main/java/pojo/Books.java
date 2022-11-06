package pojo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
/**
 * @Author sf
 * @File Books
 * @Time 2021-04-14 21:34
 * @Description
 */
@Data 
@AllArgsConstructor
@NoArgsConstructor
public class Books {
	
	private int bookID;
	private String bookName;
    private int bookCounts;
    private String detail;
}
