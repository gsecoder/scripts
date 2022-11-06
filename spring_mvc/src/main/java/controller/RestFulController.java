package controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

/**
 * @Author sf
 * @File RestFulController
 * @Time 2021-04-14 20:48
 * @Description
 */
@Controller
public class RestFulController {
	
	// 映射访问路径
	@RequestMapping("/commit/{p1}/{p2}")
	public String index(@PathVariable int p1, @PathVariable int p2, Model model){
		// 在Spring MVC中可以使用  @PathVariable 注解，让方法参数的值对应绑定到一个URI模板变量上
		int result = p1 + p2;
		// Spring MVC会自动实例化一个Model对象用于向视图中传值
		 model.addAttribute("msg", "结果："+result);
       // 返回视图位置
       return "hello";
	}
	
	@RequestMapping(value = "/hi", method = RequestMethod.GET)
	public String sayHi(Model model){
		model.addAttribute("msg", "hi spring mvc");
		return "hello";
	}
	
	@RequestMapping(value = "/post", method = RequestMethod.POST)
	public String sayPost(Model model){
		model.addAttribute("msg", "hi post");
		return "hello";
	}

}
