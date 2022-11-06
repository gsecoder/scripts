public class ProcessLoopQuit {
public static void main(String[] args) {
	// break
	for (int i = 0; i <= 10; i++) {
		if(i % 2 != 0) {
			System.out.println(i);
			break;
		}
		System.out.println("i1: " + i);
	}
	System.out.println("===== end break =====");
	
	// continue
	for (int i = 0; i <= 10; i++) {
		if(i % 2 == 0) {
			System.out.print("");
			continue;
		}
		System.out.println("i2: " + i);
	}
	System.out.println("===== end continue =====");
}
}
