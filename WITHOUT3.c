#include<stdio.h>
int main()
{
    int n,rem,sum=0,temp,count=0;
    printf("Enter a number");
    scanf("%d",&n);
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
    printf("%d",count);
}
