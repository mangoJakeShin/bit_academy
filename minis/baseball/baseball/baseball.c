#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>

#pragma warning(disable:4996) 
#define SWAP(a,b)	do{ int t; t= a;a=b;b=t;}while(0)

#include<string.h>



typedef struct {
	int first;	//100�� �ڸ� ��
	int second;	//10�� �ڸ� ��
	int third;	//1�� �ڸ� �� 

}randnum;
typedef struct {
	int strike;
	int ball;


}outcount;

randnum* r;
outcount* o;
void _initrand(randnum* r);
void _initout(outcount* o);

void firstrand(randnum* numb);
void secondrand(randnum* numb);
void thirdrand(randnum* numb);
void usernum(int* user);




main() {
	_initrand(r);
	_initout(o);
	int userinput[3];
	usernum(userinput);


}

void usernum(int user[3]) {

	int i;
	for (i = 0;i < 3;i++) {
		scanf("%d", &user[i]);
		printf("%d\n", user[i]);
	}

}
void _initout(outcount* out) {
	out->ball = 0;
	out->strike= 0;
}

void _initrand(randnum* r) {		//�̴ϼȶ����� : Ÿ�� ����

	r = (randnum*)malloc(sizeof(randnum));

	srand(time(NULL));
	firstrand(r);
	secondrand(r);
	thirdrand(r);	//���� ����


}

void firstrand(randnum* r) {
	int base = rand() % 10;
	r->first = base;
}

void secondrand(randnum* r) {
	int base = rand() % 10;
	r->second = base;
	if (r->first == base)	//1�������� ������ �����
		secondrand(r);

}

void thirdrand(randnum* r) {
	int base = rand() % 10;
	r->third = base;
	if (base == r->first || base == r->second)	//1�� ���� or 2�� ������ ������ �����
		thirdrand(r);
}