package GameProject.characters;
public class Player {
    public String name;
    private int health;
    protected int level;
    int coins;

    public Player() {
        this.name = "Ali";
        this.health = 100;
        this.level = 1;
        this.coins = 500;
    }
}