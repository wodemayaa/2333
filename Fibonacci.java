
public class Fibonacci {
	public static void main(String []args) {
	int a,b,temp;
	a=0;
	b=1;
	System.out.println("쳲��������е�ǰ20������Ϊ��");
	int[] numlist=new int[20];
	int i=0;
	//����ѭ����������
	for(int n=0;n<20;) 
	{
		temp=b;
		numlist[i]=b;
		b=a+b;
		a=temp;
		n++;
		i++;
    }
	//�������
	for(int k=numlist.length-1;k>=0;k--)
	{
		System.out.print(numlist[k]+" ");
	}
}
}
