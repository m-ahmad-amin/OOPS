interface A {
    void run();
}

public class Main {
    public static void main(String[] args) {
        A a = () -> {
            System.out.println("Hello");
        };

        a.run();
    }
}