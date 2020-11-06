#include<stdio.h>
#pragma warning(disable:4996) 
#include<stdlib.h>
#include <time.h>

/*
메모리에서 밖으로 나간다 -> 출력
write : 메모리에서 파일에 쓴다 -> 출력 
=> printf? 메모리에있는 내용을 화면으로 내보낸다(나간다) 고로 출력

scanf, getc, ... : 무언가를 메모리 밖에서 메모리에 전달함 : '입력' -> 밖에서 메모리로 들어옴

*/
//
//main() {
//	FILE* fp;
//	//fp = fopen("aws iot.txt", "w");	//파일이 없으면 자동생성, 있으면 내용 삭제하고 생성
//	//
//	//fprintf(fp, "%d, %s \n", 1, "aaa");	//내용 적는법
//
//	//fclose(fp);//쓰여지는것을 보장
//	
//	//int num;
//	//char str[100];
//	//fp = fopen("aws iot.txt", "r"); //파일이 없으면 에러
//	//fscanf(fp, "%d, %s\n", &num, str);
//	//fclose(fp);
//	//printf("%d %s\n, num, str");
//
//	//fprintf(stdout, "%d, %s\n", num, str);
//	int num; char str[100];
//	fp = fopen("a.txt", "r");
//	while (1) {
//		fscanf(fp, "%d %s", &num, str);
//		if (feof(fp)!=0)
//		{
//			break;
//		}
//		printf("%d, %s\n", num, str);
//	}
//	fclose(fp);
//	//파일 열람 코드
//
//}
//
//main() {
//
//	FILE* wp, *rp;
//	int cnt;
//		rp = fopen("1.jpg", "rb");
//		wp = fopen("2.jpg", "wb");
//		int tot = 0;
//
//	while (1) {
//		cnt = fread(buff, sizeof(char), 100, rp);
//		if (feof(rp) != 0)
//		{
//			fwriter(buff, sizeof(char), cnt, wp);
//			puts("복사 완료");
//			fread(buff, sizeof(char), 100, rp);
//		}
//		else
//			puts("실패");
//		fclose(rp);
//		fclose(wp);
//	}
//}
//

//main() {
//	int* p;
//	char* c;
//
//	p = (int*)malloc(sizeof(int));
//	c = (char*)malloc(sizeof(char)*4);
//
//	c[0] = 'a';
//	c[1] = 'b';
//	c[2] = '\0';
//	puts(c);
//
//	free(p);
//	free(c);
//}


//main() {
//// 집수소를 입력해서 길이만큼 힙을 만들고 힙에 주소를 넣은 후 출력
//	char buff[100];
//	int len;
//	char* ad;
//
//	gets(buff); //할당된 메모리 버프에 문자를 받음
//	
//	len = strlen(buff);
//
//	ad = (char*)malloc(sizeof(len) * len+1);	//4칸짜리 문자열 생성
//
//	strcpy(ad, buff);//버프에 있는 문자들을 ad문자열에 넣어줌 
//	puts(ad);
//	free(ad);
//
//	//free(ad) 넣을 시 에러 발생: 캐릭터로 3칸을 배정했으나 strcpy에서는 ad문장 뒤에 널값까지 4칸을 받음. 고로 heap corruption error 발생
//	// 방지하기 위해서는 ad 에 한칸을 더 넣어야 함
//
//}
//
//main() {//더블포인터 이용  예제
//// 집수소를 입력해서 길이만큼 힙을 만들고 힙에 주소를 넣은 후 출력
//	char buff[100];
//	int len;
//	char* ad;
//	char** myad; //double pointer
//	
//	gets(buff);
//	len = strlen(buff);
//
//	
//	myad = (char**)malloc(sizeof(char*));//메모리 동적할당
//	*myad = (char*)malloc(sizeof(char*) * len + 1);//myad 내부의 포인터에 4칸짜리 문자열 메모리 생성(전의 ad에 해당)
//	strcpy(*myad, buff);
//	puts(*myad);
//	
//	ad = (char*)malloc(sizeof(len) * len+1);	//4칸짜리 문자열 생성
//
//	free(myad);
//	free(ad);	//free를 할 시 값을 기억하는 메모리를 날려주면 값이 떠다니게 됨. 그래서 바깥의 더블포인터 메모리를 먼저 날려야함
//
//}
//
//main() {
//	int i;
//	int num_b[1];
//	int cnt;
//	char buff[100];
//	char* in_str;
//
//	printf("문장의 갯수?\n");
//	scanf("%d", num_b);
//	cnt = num_b[0];
//
//	char** a[] = (char**)malloc(sizeof(char*)*cnt+1);
//	
//
//	for (i = 0;i < cnt;i++) {
//
//	}
//
//}

//main() {
//	int cnt;
//	char buff[100];
//	char** p;
//	int dx;
//	int len;
//
//	scanf("%d", &cnt);
//	getchar();	//입력 오버플로우(첫번째 입력이 씹힘
//
//	p = (char**)malloc(sizeof(char*) * cnt);
//
//	for (dx = 0;dx < cnt;dx++) {
//		printf("%d번째 문장?", dx+1);
//		gets(buff);
//		len = strlen(buff);
//		p[dx] = (char*)malloc(sizeof(char*) * len + 1);
//		strcpy(p[dx], buff);
//		puts(p[dx]);
//		
//	}
//	for (dx = 0;dx < cnt;dx++) {
//		free(p[dx]);
//	}
//
//}

/*
malloc : 4칸짜리를 만들면 안이 쓰레기값으로 채워짐
calloc : 4칸짜리를 만들면 안이 0으로 초기화됨
realloc : 메모리의 공간을 새로운곳에 만드는것


*/

//#define square(X) ((X)*(X))
//#define PR(X) printf("%d",X)
//#define abss(x) if (x > 0) printf("%d", x); else printf("%d", -(x))
//#define three_max(a,b,c) if (a > b) { if (b > c) { printf(a); } else if (c > a) { printf("%d", c); } }else if (a < b) {if (b > c) {printf("%d", b);}else if (b < c) {	printf("%d", c);}}
////							a>b? (a?c?a:c) : (b>c?b:c) 
//#define SWAP(x,y) do {int t; t=x;x=y;y=t;} while(0)
//
//
//main() {
//	int a = 123, b = 111, c = 324;
//	printf("%d \n", (25 / square(5)));
//	// sqare(3+2) : 3 + 2 * 3 + 2 의 형태로 처리함 -> 자연적으로 2*3을 먼저 수행해서 11을 반환
//	PR(14);
//	abss(-15);
//	three_max(15, 118, 19);
//	if (a > b)
//		SWAP(a, b);
//	else
//		SWAP(b, c);
//}
//
//#define PI 3.14
////(#define RED		//아무것도 주지 않아도 전처리 지시 가능)없다고 가정하고 ifndef 생각하기
//
//#ifndef RED		//RED가 define 되어 있지 않다면 아래를 수행
//#define RED
//#endif
////RED가 없어서 입장을 한 후 RED 생성
//
////같은 ifndef가 있다면 이번에는 RED가 define되어있으므로 들어가지 않음
//#ifndef RED //RED가 define이 되어있다면 아래를 수행
//
//#endif

main() {
	
	int x = 4, y, z;
	x *= 3 + 2;
	printf("%d", x);
	x *= x = 2;
	printf("%d", x);

}











































































































































