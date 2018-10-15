import java.util.Scanner;
public class fish {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int h1 = input.nextInt();
		int m1 = input.nextInt();
		int h2 = input.nextInt();
		int m2 = input.nextInt();
		int minutes = h2*60+m2-h1*60-m1;
		int h3=minutes/60;
		int m3=minutes%60;
		System.out.print(h3+" "+m3);
	}

}
