#include<cstdio>
using namespace std;
int main()
{
	long long int x,y;
	scanf("%lld%lld",x,y);
	printf("%lld",x+2*y);
	return 0;
}

int f(int x,int y){
	int x1,y1,sum;
	if(x!=0 || y!=0)
	return 0;
	x1=x%10;
	y1=y%10;
	sum=f(x/10,y/10)*10+(x1+y1)%10;
	return sum;
}
#include<cstdio>
using namespace std;
int main()
{
	int x,y,sum=0;
	int x1,y1;
	scanf("%d%d",x,y);
/*	while(x!=0 || y!=0){
		
		x1=x%10;
		y1=y%10;
		sum=sum*10+(x1+y1)%10;
		x/=10;
		y/=10;	
	
	}  */
	printf("%d",f(x,y)
	
	
	return 0;
}
