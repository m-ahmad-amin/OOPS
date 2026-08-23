package GameProject.characters;
import GameProject.characters.Player;
public class Enemy {
    static void testPlayerAccess() {
        Player p1 = new Player();
        System.out.println(p1.name + " " + p1.coins + " " + p1.level);
    }

    public static void main(String[] args) {
        testPlayerAccess();
    }
}