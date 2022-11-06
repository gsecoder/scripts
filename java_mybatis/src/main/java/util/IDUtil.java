package util;

import java.util.UUID;

/**
 * @Author secoder
 * @File IDUtil
 * @Time 2021-04-10 11:39
 * @Description
 */
public class IDUtil {

    public static String genId(){
        return UUID.randomUUID().toString().replaceAll("-", "");
    }
}
