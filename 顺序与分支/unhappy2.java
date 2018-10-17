import java.util.Scanner;
public class unhappy2 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int[] unhappyday= new int[7];
		int[] m = new int[7];
		int[] a = new int[7];		
		for( int n=0;n<=6;n++ ) //输入并存入数组
		{
			m[n] = input.nextInt();
			a[n] = input.nextInt();
		}
		int k = 0;
		for( int i=0;i<=6;i++ ) 
		{	
			if(m[i]+a[i]>8) 
				{
					unhappyday[k]=i+1;
					k++;
				}		
		}
		System.out.println(unhappyday[0]);
	}
}
