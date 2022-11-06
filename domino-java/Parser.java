import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Parser {

    public static Domino makeDomino(String line) {

        String[] arr = line.split(" ", 2);
        int a = Integer.parseInt(arr[0]);
        int b = Integer.parseInt(arr[1]);

        return new Domino(a, b);
    }


    public static Set parseInput(String file) {

        Set set = new Set(37);

        try {
            BufferedReader reader = new BufferedReader(new FileReader(file));
            try {
                for (int i=0; i<37; i++) {
                    String line = reader.readLine();
                    set.addDomino(makeDomino(line));
                }
            }
            catch (IOException e) {
                e.printStackTrace();
            }
            try {
                reader.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        return set;
    }


    public static void main(String[] args) {

    }
}