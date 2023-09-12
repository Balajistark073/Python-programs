#include<stdio.h>
int main()
{
    int n,t,temp,rem,ans,count=0;
    scanf("%d",&n);
    t=n;
    while(n>0)
    {
        temp=n;
        while(temp>0)
        {
            rem=temp%10;
            if(rem==3)
            {
                count++;
                break;
            }
            temp=temp/10;
        }
        n--;
    }
    ans=t-count;
    printf("%d",ans);
    }