class Student {
    String name;
    int age;
//    static String name2 = this.name;
    static void study() {
        System.out.println("w");
    }

    void greet() {
        study();
    }

    Student(String name) {
        this.name = name;
    }
}
public class Main {
    public static void main(String[] args){
        Student s1 = new Student("Ahmad");
        s1.study();
//        System.out.println(s1);
//        System.out.println(new Student("Ahmad"));
    }
}