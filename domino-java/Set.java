import java.util.ArrayList;

public class Set {

    private ArrayList<Domino> set;


    public Set(ArrayList<Domino> set) {

        this.set = set;
    }


    public Set(int size) {

        this.set = new ArrayList<Domino>(size);
    }


    public ArrayList<Domino> getSet() {

        return this.set;
    }


    public Domino getDomino(int index) {

        return this.set.get(index);
    }


    public void addDomino(Domino dom) {

        this.set.add(dom);
    }


    public void removeDomino(int index) {

        this.set.remove(index);
    }


    public int getSumSideA() {

        int sum = 0;
        for (Domino domino : this.set) {
            sum += domino.getSideA();
        }
        return sum;
    }


    public int getSumSideB() {

        int sum = 0;
        for (Domino domino : this.set) {
            sum += domino.getSideB();
        }
        return sum;
    }


    public int getSize() {

        return this.set.size();
    }


    public boolean sumsAreEqual() {
        if (this.getSumSideA() == this.getSumSideB()) {
            return true;
        }
        return false;
    }


    public String toString() {

        return this.set.toString();
    }


    public static void main(String[] args) {

    }
}