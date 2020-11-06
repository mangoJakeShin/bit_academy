#include <stdio.h>
#pragma warning (disable:4996)
#include<stdlib.h>
#include <time.h>

//
//void func(void) {
//	puts("test");
//}
//
//main() {
//
//	void(*p)(void);	//void형 void함수를 가르키는 포인터 p // int (*p)[3] : 인트형 포인터 [3]
//	p = func;
//	p();
//	func();	//함수에도 주소가 있음 -> 대신 호출에 &를 붙일 필요는 없음
//}

//int add(int a, int b) {
//	return a + b;
//}int sub(int a, int b) {
//	return a - b;
//}int mul(int a, int b) {
//	return a * b;
//}int dvv(int a, int b) {
//	return a / b;
//}
//
//main() {
//
//	int(*p[4])(int, int) = { add, sub, mul,div };
//	//함수의 타입 (포인터배열 자리 수)(함수의 매개변수) = { 함수명, 함수명, ...}
//
//	int i;
//	for (i = 0;i < 4;i++) {
//		printf("%d\n", p[i](10, 5));
//	}
//
//	/*int (*p)(int, int) = add;
//	printf("%d\n", p(10, 5));
//	p = sub;
//	int (*p)(int, int) = add;
//	printf("%d\n", p(10, 5));
//	p = mul;
//	int (*p)(int, int) = add;
//	printf("%d\n", p(10, 5));*/
//
//
//
//}

//void cold(void) {//client
//	puts("cold");
//}
//void hot(void) {//client
//	puts("hot");
//}
//
//void aircon(void(*p)(void)) {//server code
//	p();//call back
//}
//main() {//client code
//	aircon(hot);//call
//}
//
//temp(int(*p)(int,int), int a, int b) {
//	
//
//	return p(a, b);
//}
//
//int add(int a, int b) {
//	return a + b;//leaf function call
//}
//
//main() {
//	int a = 10, b = 5;
//	printf("%d\n", temp(add, a, b));
//
//}

//main()
//{
//	//void //형이 없는 포인터 : char, int long, float, double
//	void* p; 
//
//	char ch = 'A';
//	p = &ch;
//
//	printf("%c\n", *(char*)p);	//void 포인터 캐스팅 : void형 포인트에는 캐스팅이 필요
//
//}
//
//void test() {
//	puts("Test");
//}
//main() {
//	char* a = "Hello";
//	void* p;
//	p = a;
//	printf("%s\n", (char*)p);
//	printf("%c\n", *(char*)p);
//
//	p = test;
//	((void(*)(void))p)();
//	//캐스팅 : 선언문에서 본인(p) 제거한거와 비슷한 형식 : void(*p)void 에서 p를 뺌
//	//
//}


//void func(int argc, char** argv) {
//	int dx;
//	for (dx = 0;dx < argc;dx++) {
//		printf("%s\n", argv[dx]);
//	}
//
//}

/*int main(매개변수, 매개변수...){
}//디버그 -> 속성 -> 디버깅 -> 명령 인수 -> 입력 /  전달해놓을 시 별도로 배열을 만들지 않아도 출력을 해줌. 
void main(빈칸) 형태를 쓸 때에는 배열을 만들고 호출하는 함수를 만들어야 가능했던 형태를 간소화
즉, 메인 함수를 통한 인자의 전달이 가능
}
*/
//		//int a	,	char** b 가능
//int main(int argc, char** argv) {
//	int dx;
//	for (dx = 0;dx < argc;dx++) {
//		printf("%s\n", argv[dx]);
//	}
//
//}
//
//int main(void) {
//	int ch;
//	while (1) {
//		ch = getchar();
//		if (ch == EOF)
//			break;
//		putchar(ch);
//
//	}
//	return 0;
//}
//int find(char** p, char* find) {
//
//	int i = 0;
//	while (1) {
//		if (p[i] == find) {
//			break;
//		}
//		else if (i == 7)
//			break;
//		else
//			i++;
//	}
//	printf("%d 번", i + 1);
//
//	int dx;
//	for (dx = 0;dx < 7;dx++) {
//		if (0 == strcmp(p[dx], find))
//		{
//			printf("%d %s \n", dx, p[dx]);
//		};
//	}
//}
//main() {
//	char* a[] = {"aaa","bbb","ccc","ddd","eee","fff","ggg"};
//
//	find(a, "ggg");
//}

//
//main() {
//	char a[3][10] = {
//		"aaa","Bbb","ccccc"
//	};
//	char tmp[10];
//	//push(a, 1);
//		//위 2차원 배열을 한칸씩 아래로 밀리게 구현.
//	strcpy(tmp, a[2]);
//	strcpy(a[2], a[1]);
//	strcpy(a[1], a[0]);
//	strcpy(a[0], tmp);
//	puts(a[0]);
//	puts(a[1]);
//	puts(a[2]);
//}

//typedef struct person newman;
//
//struct person{
//	char name[20];
//	char tel[20];
//	int age;
//	float eye;
//
//
//};//구조체 선언 (java/python class와 유사)
//
//
//main() {
//	newman man1 = { "jake shin",	"01022169171",28,0.2f };
//
//	printf("%s\n", man1.name);
//
//	newman man2;
//	man2 = man1; // man1의 내용이 그대로 복사됨
//	
//	//scanf("%d" ,&man1.age);
//	printf("%d\n", man1.age);
//
//	scanf("%s", man1.name);
//	printf("%s", man1.name);
//}
//
//struct num{
//	int fir;
//	int sec;
//};
//
//void func1(int a, int b) {
//	printf("%d",a + b);
//	}
//
//void func2(struct num* p) {
//	printf("%d", p->fir * p->sec);
//
//}
//void func3(struct num* p) {
//	int sz;
//
//	int i;
//	int sum = 0;
//	//for (i = 0;i < sz;i++) {
//	//	sum += (p + i)->fir;
//	//	printf("%d", (p + i)->fir);
//	//	sum += (p + i)->sec;
//	//}
//	sum += (p->fir + p->sec + (p + 1)->fir + (p + 1)->sec);
//	printf("%d", sum);
//
//}
//
//
//
//main() {
//	struct num a = { 1,2 }, b = { 3,4 }, c[8] = { 5,6,7,8,9,10,11,12 };
//
//	//구조체멤버 각각 던져서 합
//	func1(a.fir, a.sec);
//
//	//구조체 변수 주소 던져서 곱
//	func2(&b);
//
//	//구조체 배열 주소 던져서 합
//	func3(c);
//
//
//
//}

//중첩구조체에서 주소연산자로 들어갔으면 애로우 연산자로 호출해야함.


struct subject {
	int subname[5];
};

struct info {
	char name[10];
	float avg;
	struct subject sub;
};


void name_in(struct info *mans, int a) {
	printf("%d번째 사람 이름: ", a + 1);
	scanf("%s",mans[a].name);
	printf("%s check\n",mans[a].name);
}

void kor_in(struct info* mans,int a) {
	int i = 0;
	printf("국어 점수 : ");
	scanf("%d", &i);
	mans[a].sub.subname[0] = i;
}
void eng_in(struct info* mans,int a) {
	int i = 0;
	printf("영어 점수 : ");
	scanf("%d", &i);
	mans[a].sub.subname[1] = i;
}
void math_in(struct info* mans,int a) {
	int i = 0;
	printf("수학 점수 : ");
	scanf("%d", &i);
	mans[a].sub.subname[2] = i;
}

void info_in(struct info* mans) {
	int i;
	for (i = 0;i < 3;i++) {
		name_in(mans, i);
		kor_in(mans,i);
		eng_in(mans,i);
		math_in(mans,i);
	}

}
void tot_cal(struct info* mans) {
	int i;
	int j;
	int sum;
	for (i = 0;i < 3;i++) {
		sum = 0;
		for (j = 0;j < 3;j++) {
			sum += mans[i].sub.subname[j];
		} mans[i].sub.subname[3] = sum;
		printf("%d\n",mans[i].sub.subname[3]);
	}

}
void avg_cal(struct info* mans) {
	int i;
	for (i = 0;i < 3;i++) {
		mans[i].avg = mans[i].sub.subname[3] / 3.0;
	}

}

void rank_cal(struct info* mans) {
	int a = 3, b = 3, c = 3;
	int at, bt, ct;
	at = mans[0].sub.subname[3];
	bt = mans[1].sub.subname[3];
	ct = mans[2].sub.subname[3];
	if (at > bt) {
		a -= 1;
		if (bt > ct) {
			b -= 1;
			a -= 1;
		}
		else if (ct > at) {
			c -= 2;
		}

	}
	else if(at<bt){
		b -= 1;
		if (bt > ct) {
			b -= 1;
		}
		else if (bt < ct) {
			c -= 2;
		}
	}
	mans[0].sub.subname[4] = a;
	mans[1].sub.subname[4] = b;
	mans[2].sub.subname[4] = c;
	
	printf("1번 평균 %f점 %d 등\n", mans[0].avg, mans[0].sub.subname[4]);
	printf("2번 평균 %f점 %d 등\n", mans[1].avg, mans[1].sub.subname[4]);
	printf("3번 평균 %f점 %d 등\n", mans[2].avg, mans[2].sub.subname[4]);


	
}

main() {
	int i = 0;
	struct info man[3] = { 0 };

	//scanf("%d", &i);
	//man[0].sub.subname[0] = i;
	//printf("%d", man[0].sub.subname[0]);

	info_in(man);
	tot_cal(man);
	avg_cal(man);
	rank_cal(man);
}


































