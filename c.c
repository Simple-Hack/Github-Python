#include<stdio.h>
int main(){
    int i,j,line;
    scanf("%d",&line);
    for(i=line;i>=1;i--){
        for(j=i;j<line;j++){
            printf(" ");
        }
        for(j=2*(i-1)+1;j>0;j--){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}