
public class Fibonacci {
	public static void main(String []args) {
	int a,b,temp;
	a=0;
	b=1;
	System.out.println("斐波那契数列的前20项倒序输出为：");
	int[] numlist=new int[20];
	int i=0;
	//数列循环存入数组
	for(int n=0;n<20;) 
	{
		temp=b;
		numlist[i]=b;
		b=a+b;
		a=temp;
		n++;
		i++;
    }
	//倒序输出
	for(int k=numlist.length-1;k>=0;k--)
	{
		System.out.print(numlist[k]+" ");
	}
}
}
