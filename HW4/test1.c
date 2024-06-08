#define MYNUMBER 1004
#include <stdio.h>

struct myStruct{
	int (*f)(int);
};
int f1(){return 1;}
int facto(int n){
	if(n==1){ return 1; }
	int (*a)(int) = facto;
	return n*facto(n-1);
	facto(1);
	f1();
	a(1);
}

int main(){
	struct myStruct ms;
	ms.f = facto;
	printf("5! is : %d\n",ms.f(5));
	printf("6! is : %d\n",ms.f(6));
	return 0;

}
