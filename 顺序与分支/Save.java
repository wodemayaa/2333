import java.util.Scanner;
public class Save {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int[] a=new int[12];
		for(int i=0;i<12;i++)//����
		{
			a[i]=input.nextInt();
		}
		int k=0,n=0;//�����
		int m=1;
		for(int i=0;i<12;i++)//�·����뿪ʼ
		{	
			n+=300;
			n=n-a[i];
			if(n<0) 
			{
				break;
			}
			m+=1;
			k=k+n/100;
			n=n%100;
			}
		if(n<0) 
		{
			System.out.println(-m);
		}
		else
		{
			n=k*120+n;
			System.out.println(n);
		}	
		}

}
