%{
#include <stdio.h>
int ary[9] = {0,0,0,0,0,0,0,0,0};
%}
%%
"//".*\n	{comment++;}
"/*"(.*[\n].*)*"*/" {comment++;}
#include.*\n	{preprocessor++;}
#define.*\n	{preprocessor++;}
0[0-7]*	{octal_num++;}
-[0-9]+	{neg++;}
[0-9]+	{pos++;}
"+"|"-"|"*"|"/"|"%"	{operator++;}
"&&"|"||"|"!"	{operator++;}
"<"|">"|"<="|">="|"=="|"!="	{operator++;}
"++"|"--"	{operator++;}
","	{operator++;}
"&"|"*&"|"."	{operator++;}
"="	{equ++;}
"{"	{b_left++;}
"}"	{b_right++;}
([a-oA-O]|[q-zQ-Z])*"pp"([a-oA-O]|[q-zQ-Z])*	{wordcase1++;}
e[a-zA-Z]*m	{wordcase2++;}
[a-zA-Z]+	{word++;}
.|\n	{mark++;}
%%

int main(){
	yylex();
	printf("preprocessor = %d\n", preprocessor);
	printf("octal number = %d\n", octal_num);
	printf("negative decimal number = %d\n", neg);
	printf("positive decimal number = %d\n", pos);
	printf("operator = %d\n", operator);
	printf("comment = %d\n", comment);
	printf("'=' = %d\n", equ);
	printf("'{' = %d\n", b_left);
	printf("'}' = %d\n", b_right);
	printf("wordcase1 = %d\n", wordcase1);
	printf("wordcase2 = %d\n", wordcase2);
	printf("word = %d\n", word);
	printf("mark = %d\n", mark);
	return 0;
}

int yywrap(){
	return 1;
}
