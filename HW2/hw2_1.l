%{
#include <stdio.h>
int count = 0;
%}
%%
([Ll]ove)	{count++;}
.|\n	;
%%

int main(){
	yylex();
	printf("number of love=%d\n",count);
	return 0;
}

int yywrap(){
	return 1;
}