public class Main {

    public static void main(String[] args) {
        // Set set = Parser.parseInput("files/minhaentrada.txt");
        Set set = new Set(4);
        set.addDomino(new Domino(1,4));
        set.addDomino(new Domino(2,9));
        set.addDomino(new Domino(2,1));
        set.addDomino(new Domino(0,4));

        Set set2 = new Set(3);
        set2.addDomino(new Domino(6,3));
        set2.addDomino(new Domino(1,2));
        set2.addDomino(new Domino(3,1));

        Set set3 = new Set(2);
        set3.addDomino(new Domino(8,1));
        set3.addDomino(new Domino(9,4));

        Api.verify(set3);
    }
}