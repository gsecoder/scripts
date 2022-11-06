package controller;


import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

/**
 * @Author sf
 * @File HelloController
 * @Time 2021-04-13 20:40
 * @Description
 */
// @Controller是为了让Spring IOC容器初始化时自动扫描到
@Controller
// @RequestMapping是为了映射请求路径，这里因为类与方法上都有映射所以访问时应该是/HelloController/hello
@RequestMapping("/HelloController")
public class HelloController {
	
	// 真实访问地址 : 项目名/HelloController/hello
	@RequestMapping("/hello")
	public String sayHello(Model model){
		// 方法中声明Model类型的参数是为了把Action中的数据带到视图中；
		// 方法返回的结果是视图的名称hello，加上配置文件中的前后缀变成WEB-INF/jsp/hello.jsp。
		
		// 向模型中添加属性msg与值，可以在JSP页面中取出并渲染
		model.addAttribute("msg", "Hello, SpringMVC");
		// web-inf/jsp/hello.jsp
		return "hello";
	}
}
