#include<stdio.h>
#pragma warning(disable:4996) 
#include<stdlib.h>
#include <time.h>

/*
const int * p : * 기준 왼편 const : 포인터를 이용하여 값을 변경할 수 없음
int const * p : 
int * const p: * 기준 오른편 const: 주소를 변경할 수 없음

int num = 20;
const int * ptr = &num; 

*ptr = 30; -> 주소를 이용한 변경이 불가함(에러)
num = 40; -> 변수를 이용한 접근은 가능
---------

int num1 = 20;
int num2 = 40;

int * const p = &num1; => p의 주소값은 num1으로 고정시킴

p = &num2 -> p에 num2 주소값을 할당하려 하면 에러 발생
*p = 40 -> 주소값을 이용한 변수값 변경 가능

--------
int num1 = 20
const int * const p = &num1 -> 조회만 가능


int a[2][3]

a	= a[0][0]~[0][2]	+1 => 다음 행 이동
&a[0] = a[0]~a[0][2]	+1 => 다음 행 이동
a[0] = a[0][0]			+1 => 옆칸 이동 : *(a[0] + 2) => a[0][2]
&a[0][0] = a[0][0]		+1 => 옆칸 이동
&a = [0][0]~[1][2]

*/


/*main() {
	int i, j, k;
	k = 1;
	int a[10][10];
	for (i = 0;i < 10;i++) {
		for (j = 0;j < 10;j++)
		{
			a[i][j] = k++;
			printf("%d\t", a[i][j]);
		}printf("\n");
	}
}*/
//
//main() {
//	int a[2][3] = { 1,2,3,4,5,6 };
//	int rx, cx,k;
//	k = 0;
//	int ro_size = sizeof(a) / sizeof(a[0]);
//	int co_size = sizeof(a[0]) / sizeof(a[0][0]);
//	int col_sum[3]= { 0 };
//	int row_sum[2] = { 0 };
//	for (rx = 0;rx < ro_size;rx++) {
//		for (cx = 0;cx < co_size;cx++) {
//			row_sum[rx] += a[rx][cx];
//			//printf("%d\t", a[i][j]);
//			col_sum[cx] += a[rx][cx];
//		}
//		//printf("\n");
//		//printf("\n%d\t", col_sum[i]);
//	}
//	for (rx = 0; rx < ro_size;rx++)
//	{
//		for (cx = 0;cx < co_size;cx++) {
//			printf("%d ", a[rx][cx]);
//		}
//		printf("+ %d", row_sum[rx]);
//		printf("\n");
//	}
//}

/*
int a = 7
int *p = &a	= 100
int **k = &p	= 200
&k = 300


		a	p	k
7		a	*p	**k
100		&a	p	*k
200		x	&p	k
300		x	x	&k

*/

//
//main() {
//	int a;
//	int* p;
//	int** k;
//	p = &a;
//	k = &p;
//
//	**k = 10;
//	printf("%d", a);
//	printf("%d", *p);
//	
//
//}
//last(int** k) {
//	**k = 500;
//}
//middle(int* p)
//{
//	last(&p);	//싱글포인터의 주소
//}
//main() {
//	int a = 7;
//	middle(&a);	//변수의 주소
//	printf("%d", a);
//}


//last(int* k) {
//	*k = 500;	//싱글포인터의 값
//}
//middle(int* p)
//{
//	last(&p);	//싱글포인터의 주소
//}
//main() {
//	int a = 7;
//	middle(&a);	//변수의 주소
//	printf("%d", a);
//}
//둘 다 a의 값은 바뀜

//void connect(int *a, int** p) {
//	*p = a;
//}
//
//main() {
//	int a = 7;
//	int* p = NULL;
//	connect(&a,&p);	//a와 p를 연결 
//	printf("%d", *p);
//}
//
//void swap1(int* p1, int* p2) {
//	int tmp = 0;
//	tmp = *p1;
//	*p1 = *p2;
//	*p2 = tmp;
//}	//변수에 &를 추가하지 않아야 값이 바뀜 
//
//void swap2(int** p1, int** p2) {
//
//	int temp = 0;
//	temp = **p1;
//	**p1 = **p2;
//	**p2 = temp;
//}	//변수에 &를 추가해야 두개 값이 바뀜
//
//
//void middle(int*p1,int*p2) {
//
//	swap2(&p1, &p2);
//
//}
//
//main() {
//	int num1 = 10;
//	int num2 = 20;
//
//	
//	printf("1 %d\t%d\n", num1, num2);
//	middle(&num1,&num2);
//	printf("2 %d\t%d", num1, num2);
//
//}

/*
int *p[3] = array of pointer(포인터 배열)
=> 배열 한칸 한칸을 가르키는 포인터
int(*p)[3] = pinter to an array(배열의 포인터)
=> 배열 자체를 가르키는 포인터

	
변수 선언(만듦)			주소 표현(던짐)			포인터 표현(주소를 받는 메모리)(받음)
1. int a					&a							int *p = int p[], int p[1000]

2. int a[3]				a, &a[0]						int *p = int p[], int p[1000]

3. int a[2][3]			a, &a[0]							int(*p)[3] = int p[1000][3] = int p[][3]
						a[0], &a[0][0]					int *p = int p[], intp[1000]

4. int*a					&a							int**p = int *p[], int *p[1000]

5. int *p[3]			a,&a[0]							int**p = int *p[], int *p[1000]

func(int *p) {//받음				/func(int (*p)[3]) 

}

main() {

	//선언
	int a;							/int a[2][3]
	func(&a);//호출 : 던짐(사용)	/func(a)
}

*/
//
//void func(char *p[1000]) {
//	//cd 출력
//	printf("%s\n", p[0] + 2);
//	//k출력
//	printf("%c\n", **(p+1));
//	//b출력
//	printf("%c\n", *(*(p + 2) + 1));	//p[2][1]
//	
//}
//
//main() {
//	char* a[3] = { "abcd","kbs","sbs" };
//	func(a);
//
//}

/*
a[0] == *(a+0)		== *(a)		== *a
a[1] == *(a+1)
a[2] == *(a+2)

a[0][2] -> a[0] == t
== t[2]
== *(t+2)
== *(a[0]+2)
== *(*(a+0)+2

a[0][2] 
== (a[0])[2]
== *(*(a+0)+2) 
== (*a)[2]
== *(*a+2)

*/
char* d_1[1] = { "물" };
char* d_2[1] = { "콜라" };
char* d_3[1] = { "환타" };
char* d_4[1] = { "사이다" };
char* d_5[1] = { "비타민" };
char* d_6[1] = { "울트라" };
char** d_list[6] = { d_1,d_2,d_3,d_4,d_5,d_6 };
int p_list[6] = { 800,1000,1100,1200,1500,2000 };
int balance = 0;
int select = 0;

void change_d() {
	int i;
	int a;
	int b;
	printf("변경하실 음료를 선택해주세요\n");
	for (i = 0;i < 6;i++) {
		printf("%d. %s  ", i + 1, *d_list[i]);
		printf("%d\n", p_list[i]);
		}

	scanf("%d", &a);
	b = a - 1;

	char np[10] = { 0 };
	char* npp[1] = { np };
	printf("%s 선택\n", *d_list[b]);
	scanf("%s", &np);
	printf("%s\n", *npp);
	
	d_list[b] = npp;
	
	printf("%s로 변경\n", *d_list[b]);

}
void change_p() {
	int a = 0;
	int i;
	int c_price;
	printf("가격을 변경하실 음료를 선택해주세요\n");

		for (i = 0;i < 6;i++) {
			printf("%d. %s  ", i + 1, *d_list[i]);
			printf("%d\n", p_list[i]);
		}
		scanf("%d", &a);

			if (a > 0 && a < 7) {
				int b = a - 1;
				printf("%s 선택 \n", *d_list[b]);
				printf("변경하실 가격을 입력해주세요\n");
				scanf("%d", &c_price);
				p_list[b] = c_price;
				printf("%d로 변경 완료\n", p_list[b]);

			}
			else
				printf("잘못 선택하셨습니다. 1~6까지 골라주세요.\n");
}


void admin_menu() {
	int a;
	printf("관리자 메뉴 선택\n");
	printf("1. 음료 변경 / 2. 가격 변경 / 3. 종료\n");
	scanf("%d", &a);
	
		if (a == 1)
			change_d();
		else if (a == 2)
			change_p();
			
		else
			printf("잘못 선택하셨습니다.");
	

}

void select_drink(int sel_num) {
	int a = sel_num - 1;
	if (balance >= p_list[a]) {
		printf("%s, %d원 지급 완료\n", *d_list[a],p_list[a]);
		balance -= p_list[sel_num-1];
		printf("현재 잔액 : %d\n", balance);
	}
	else
		printf("잔액 부족. 현재 잔액 %d 원\n", balance);
}


void addbalance(int new_bal) {
	balance += new_bal;
	printf("현재 잔액: %d \n", balance);
}




void user_select() {
	int a;
	scanf("%d", &a);
	printf("%d 선택\n", a);
	if (a <= 6)
		select_drink(a);
	else if (a == 1000)
		addbalance(a);
	else if (a == 500)
		addbalance(a);
	else if (a == 100)
		addbalance(a);
	else if (a == 7)
		select += 7;
	else if (a == 8)
		admin_menu();
	else
		printf("wrong number\n");
}


void menu_print(int a) {
	int i;
	
	printf("구매 가능 목록\n");
	for (i = 0;i < a;i++) {
		printf("%d. %s  ", i+1,*d_list[i]);
		printf("%d\n", p_list[i]);
	}
}

void menu() {
	int i;
		printf("잔액을 추가하거나 음료를 골라주세요\n");
		printf("금액은 100/500/1000원만 추가 가능합니다\n");
		printf("7을 누르시면 종료됩니다. \n");
		user_select();
		if (balance >= 2000)
			menu_print(6);
		else if (balance >= 1500)
			menu_print(5);
		else if (balance >= 1200)
			menu_print(4);
		else if (balance >= 1100)
			menu_print(3);
		else if (balance >= 1000)
			menu_print(2);
		else if (balance >= 800)
			menu_print(1);
	}
	


main() {
	
	while(select!=7)
		menu();
	}

















