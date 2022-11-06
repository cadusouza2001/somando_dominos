public class Domino {

    private int sideA;
    private int sideB;


    public Domino() {
    }


    public Domino(int sideA, int sideB) {

        this.sideA = sideA;
        this.sideB = sideB;
    }


    public int getSideA() {

        return this.sideA;
    }


    public int getSideB() {

        return this.sideB;
    }


    public void setSideA(int sideA) {

        this.sideA = sideA;
    }


    public void setSideB(int sideB) {

        this.sideB = sideB;
    }


    public void turn() {

        int x = this.sideA;
        this.sideA = this.sideB;
        this.sideB = x;
    }


    public String toString() {

        return String.format("[ %d | %d ]", this.sideA, this.sideB);
    }

    public static void main(String[] args) {
        Domino dom = new Domino(10,30);
        System.out.println(dom);
        dom.turn();
        System.out.println(dom);
    }
}