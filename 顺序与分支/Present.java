import java.util.Scanner;
public class Present {
	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		int a[]=new int[3];//一包a支
		int p[]=new int[3];//一包p元
		int b[]=new int[3];//需要b包
		int pf[]=new int[3];//总共pf元
		int n;
		n=input.nextInt();
		for(int i=0;i<3;i++) //读入数据
		{
			a[i]=input.nextInt();
			p[i]=input.nextInt();
			if(n%a[i]==0) 
			{
				b[i]=n/a[i];
			}
			else 
			{
				b[i]=n/a[i]+1;
			}
			pf[i]=p[i]*b[i];
		} 
		int pl;
		if(pf[0]<pf[1])
		{
			pl=pf[0];
		}
		else 
		{
			pl=pf[1];
		}
		if(pl<pf[2]) 
		{
			System.out.println(pl);
		}
		else 
		{
			System.out.println(pf[2]);
		}
		
	}

}
