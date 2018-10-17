import java.util.Scanner;
public class electricity {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int n = input.nextInt();
		double money;
		if(n<=150) {
			money = n*0.4463;
		}
		else if(150<n && n<=400) {
			money = 150*0.4463+(n-150)*0.4663;
		}
		else {
			money = 150*0.4463+250*0.4663+(n-400)*0.5663;
		}
		System.out.print(String.format("%.1f",money));
			
	}

}
