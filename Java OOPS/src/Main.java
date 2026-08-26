public class Main {
    public static void helper(int... args) {
        for (int arg : args) System.out.println(arg);
    }
    public static void main(String[] args){
        helper(new int[]{1, 2});
    }
}