package easyexcel_operate;

import com.alibaba.excel.context.AnalysisContext;
import com.alibaba.excel.event.AnalysisEventListener;

import java.util.Map;

/**
 * @Author secoder
 * @File ReadDemoDataListener
 * @Time 2021-08-07 18:23
 * @Description 读取Excel需要先写一个监听器继承AnalysisEventListener
 */
// 有个很重要的点DemoDataListener 不能被spring管理，要每次读取excel都要new,然后里面用到spring可以构造方法传进去
public class DemoDataListener extends AnalysisEventListener<DemoData> {
    
    // 一行行读取excel内容
    @Override
    public void invoke(DemoData demoData, AnalysisContext analysisContext) {
        System.out.println("***" + demoData);
    }
    
    // 读取表头
    @Override
    public void invokeHeadMap(Map<Integer, String> headMap, AnalysisContext context) {
        System.out.println("表头：" + headMap);
    }
    
    // 读取完成之后
    @Override
    public void doAfterAllAnalysed(AnalysisContext analysisContext) {
        System.out.println("读取完成");
    }
}
