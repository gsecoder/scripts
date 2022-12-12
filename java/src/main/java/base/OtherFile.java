package base;

public class OtherFile {
}

class Something {
    public static void main(String[] something_to_do) {
        for(int i=0; i<something_to_do.length; i++){
            System.out.println(
                    "args[" + i + "]=" + something_to_do[i]
            );
        }
        System.out.println("Do something ...");
    }
}