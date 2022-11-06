import java.util.ArrayList;


public class Api {

    public static Set copySet(Set set) {

        ArrayList<Domino> newList = new ArrayList<Domino>(set.getSize());
        for (int i=0; i<set.getSize(); i++) {
            Domino dom = new Domino(set.getDomino(i).getSideA(), set.getDomino(i).getSideB());
            newList.add(dom);
        }

        return new Set(newList);
    }


    public static Domino removeOne(Set set, int index) {

        Domino removed = new Domino(set.getDomino(index).getSideA(), set.getDomino(index).getSideB());
        set.removeDomino(index);

        return removed;
    }


    public static Set arrange(Set set, boolean[] keys) {

        Set newSet =  copySet(set);

        for (int i=0; i<newSet.getSize(); i++) {
            if (keys[i]) newSet.getDomino(i).turn();
        }

        return newSet;
    }


    public static int verifyNoRemoval(Set set) {

        int size = set.getSize();
        int numKeys = (int)Math.pow(2, size) / 2;

        for (int i=0; i<numKeys; i++) {
            boolean[] key = Generator.generateKey(i, size);
            Set arangedSet = Api.arrange(set, key);
            if (arangedSet.sumsAreEqual()) {
                return arangedSet.getSumSideA();
            }
        }

        return -1;
    }


    public static int verifyWithRemoval(Set set) {

        int biggestSum = -1;
        Domino removed = null;

        for (int i=0; i<set.getSize(); i++) {
            Set copy = copySet(set);
            Domino x = removeOne(copy, i);
            int result = verifyNoRemoval(copy);
            if (result > -1  &&  result > biggestSum) {
                biggestSum = result;
                removed = x;
            }
        }

        if (removed != null)
            System.out.println(removed);

        return biggestSum;
    }


    public static void verify(Set set) {

        int sum = verifyNoRemoval(set);

        if (sum > -1) {
            System.out.println(sum);
            System.out.println("Sem remocao");
        }
        else {
            sum = verifyWithRemoval(set);
            if (sum > -1) {
                System.out.println(sum);
            }
            else {
                System.out.println("Impossivel");
            }
        }
    }


    public static void main(String[] args) {

    }
}
