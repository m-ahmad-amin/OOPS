package GameProject.weapons;

import GameProject.characters.Player;

public class Weapon {
    static void testPlayerAccess() {
        Player p1 = new Player();
        System.out.println(p1.name);
    }

    public static void main(String[] args) {
        testPlayerAccess();
    }
}