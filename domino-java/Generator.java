import java.util.Random;


public class Generator {

    private static Random random = new Random();


    public static Domino generateDomino() {

        int sideA = random.nextInt(1000);
        int sideB = random.nextInt(1000);

        return new Domino(sideA, sideB);
    }


    public static Set generateSet(int size) {

        Set set = new Set(size);
        for (int i=0; i<size; i++) {
            set.addDomino(generateDomino());
        }
        return set;
    }


    public static boolean[] generateKey(int num, int size) {

        boolean[] key = new boolean[size];
        String teste = String.format("%%%ds", size);
        String keyString = String.format(teste, Integer.toBinaryString(num)).replace(' ', '0');

        for (int j=0; j<size; j++) {
            if (keyString.charAt(j) == '1') {
                key[j] = true;
            }
            else {
                key[j] = false;
            }
        }

        return key;
    }


    public static void main(String[] args) {

    }
}
