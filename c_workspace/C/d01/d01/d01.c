#include <stdio.h>
#pragma warning(disable:4996) 
#include<stdlib.h>
#include <time.h>
// f10 : debugging  / shift f5 => 종료
// f9 : break pointer : 표시점에서 멈춤
// f5  :중단점 이동(debugging 자동 실행)
//main() {
//	float a = 12.0f;	//f = float, 생략시 double
//	float b = 6.0f;
//	int c = 0x12345678; 
//}
/* 1100 :2
*	000000001100	
	0000110000000000
*				
* 6*0110 = 1.10*2^2+127
* 0100 0 0001 1 00000000000
* 
* /
*/ 
//
//main() {
//	printf("my name is %s\n","abdec");
//	printf("i am %d years old", 22);
//	
//}


//main() {
//
//	char a = 'z';
//	char b = 65;
//	/*printf("%c %d", a, a);
//	printf("%c %d", b, b);*/
//	printf("%d", a);
//
//	if (a > 64 && a < 97) {
//		a += 32;
//		printf("%c", a);
//		printf("대문자");
//	}
//	else if (a > 96 && a < 123) {
//		a -= 32;
//		printf("소문자\n");
//		printf("%c\n", a);
//	}
//
//	if ('a' <= a && a <= 'z') {
//		printf("up -> low (%c)\n", a - 'a' + 'a');
//	}
//	else {
//		printf("low => up (%c)\n", a - 'a' + "a");
//	}
//
//	printf("%c\n", (a ^ 32)^32);
//}


//
//main() {
//	
//	printf("%d\n", sizeof('a'));
//	int num = 129;
//	printf("%d\n", sizeof(num));
//	char ch = num;
//	printf("%d\n", sizeof(ch));
//
//}

//main() {
//
//	int i = 0;
//	while (i <= 100) {
//		if (i % 2 == 0) {
//			printf("%d\n", i);
//		}	i++;
//	}
//}
//
//main() {
//	int i = 0;
//	while (i <= 5) {
//		printf("*****\n");
//		i++;
//	}
//
//}

//main() {
//
//	int a, b;
//	a = 0;
//	
//	while (a < 5) {
//		b = 0;
//		while (b < 5) {
//		
//			if (a == b) {
//				printf("-");
//			}
//			else 
//				printf("*");
//			b++;
//		}a++;
//			printf("\n");
//
//	}
//
//
//
//}


/*main() {*//*
	int i = 3;
	int pw = 1234;
	int ipass;
	while (i > 0) {
		printf("input password");
		scanf_s("%d", &ipass);
			i--;
		if (ipass != pw)
		{
			printf("%d번의 기회 남음", i);
		}
		else
		{
			printf("pass");
			break;
		}
	}printf("cop");*/
//
//int get_passwd(void) {
//	int passwd;
//	printf("input password: ");
//	scanf("%d", &passwd);
//	return passwd;
//
//}
//
//void chance(int cnt) {
//	if(cnt != 0)
//	printf("%d 번의 기회가 남음 \n", cnt);
//
//}
//
//int compare(int a, int b) {
//	return a == b;
//}
//void police(int cnt) {
//	if (cnt == 0)
//		printf("Police!");
//}
//
//main(){
//
//	int pwd = 1234;//기존에 정해둔 패스워드
//	int get_pwd; //받을 패스워드
//	int cnt = 3; //기회는 3번 뿐
//	do {
//		get_pwd = get_passwd();//패스워드 받아 옴 
//
//		if (compare(pwd, get_pwd)) //두변수 같은지 같으면 1 다르면 0을 리턴한다.
//		{
//			puts("통과");
//			break;
//		}
//		else {
//			chance(--cnt); //기회를 보여주는 함수
//		}
//	} while (cnt); //cnt!=0
//
//	police(cnt); //경찰을 부르는 함수 cnt가 0이면 결찰을 부르는 함수
//
//
//
//
//
////}
//main() {
//	srand(time(NULL));	//seed함수 위치 변경
//	int dx;
//	int rnd;
//	for (dx = 0; dx < 5;dx++)
//	{
//		rnd = rand();
//		printf("%d\n", rnd);
//	}
//}

int input_age() {//나이 입력
	int age = 0;
	printf("input age : \n");
	scanf("%d", &age);
	return age;
}

int compare_age(int a, int b) {	// 나이 비교 함수
	if (a > b)
		return 1;
	else if (a < b)
		return -1;
	else
		return 0;
}				//타겟 나이보다 입력 나이가 적으면 1, 많으면 -1, 같으면 0 반환

void print_bingo(int a) {	//빙고 출력 함수 : 비교 함수의 반환값으로 수행
	if (a == 1)
	{
		printf("input bigger num\n");
		
	}
	else if (a == -1)
	{
		printf("input smaller num\n");
		
	}
		
}

void check_input(int a, int b, int c) {
	if ((a == 1) && (compare_age(b, c) == 1))
		printf("INPUT BIGGER NUMBER\n");
	else if ((a == -1) && (compare_age(b, c) == -1))
		printf("input SMALLER number\n");
}


main() {
	int tgt_age;
	srand(time(NULL));
	int age = rand();
	tgt_age = age % 100;
	int ipt_age = input_age();
	int i = 1;
	int oage;
	while (tgt_age != ipt_age) {
		int cp_age = compare_age(tgt_age, ipt_age);
		print_bingo(cp_age);
		oage = ipt_age;
		ipt_age = input_age();
		check_input(cp_age, oage, ipt_age);

		//printf("oage %d, n_age %d\n", oage, ipt_age);
		i++;
	}
	printf("bingo! %d times tried", i);
}


















































