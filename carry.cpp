#include<cstdio>
using namespace std;
int main()
{
	long long int x,y;
	scanf("%lld%lld",x,y);
	printf("%lld",x+2*y);
	return 0;
}

#include<cstdio>
using namespace std;
int main()
{
	long long int x,y,m=1,sum=0;
	scanf("%lld%lld",&x,&y);
    while(x!=0 || y!=0){
		sum+=((x%10+y%10)%10)*m;
		x/=10;
		y/=10;
		m*=10;	
	} 
	printf("%lld",sum);
	return 0;
}
