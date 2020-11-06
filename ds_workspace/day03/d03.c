#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>

#pragma warning(disable:4996) 
#define SWAP(a,b)	do{ int t; t= a;a=b;b=t;}while(0)

#include<string.h>
//
//typedef struct _sales
//{
//    char itemname[20];
//    int unitprice;
//    int count;
//    int amount;
//}Sales;
//int item_name(const void* a, const void* b)
//{
//    //return strcmp((char*)a, (char*)b);
//    return strcmp(((Sales*)a)->itemname, ((Sales*)b)->itemname);
//
//}
//int total_sales(const void* a, const void* b) {
//    return ((((Sales*)a)->amount) - ((Sales*)b)->amount);
//        
//}
//
//main()
//{
//    Sales prd[5] = {
//     {"ccc", 10,90,900},
//     {"ddd", 20,80,1600},
//     {"aaa", 30,70,2100},
//     {"eee", 40,60,2400},
//     {"bbb", 50,50,2500}
//    };
//    int dx;
//
//    //qsort(prd, 5, sizeof(prd[0]), item_name);
//
//    //for (dx = 0; dx < 5; dx++)
//    //    printf("%s %d %d %d\n", prd[dx].itemname,
//    //        prd[dx].unitprice, prd[dx].count, prd[dx].amount);
//
//    qsort(prd, 5, sizeof(prd[0]), total_sales);
//
//    for (dx = 0; dx < 5; dx++)
//        printf("%s %d %d %d\n", prd[dx].itemname,
//            prd[dx].unitprice, prd[dx].count, prd[dx].amount);
//
//
//}

//
//typedef struct _node node;
//struct _node {
//    char name[10];
//    struct _node* next;
//};
////int gg = 0;
//int cmp_name(const void* a, const void* b)
//{
//    return strcmp(((node*)b)->name, ((node*)a)->name);//왜 b-a를 해야 a,b,c 순으로 출력?
//}
//int cmp_node(const void* a, const void* b) {    //***포인터 위치로 정렬**** 
//
//
//    return (int)(&((node*)a))-(int)(&((node*)b));
//
//}
//
//node* p, * q;
//main()
//{
//    node* k[4];
//
//    p = (node*)malloc(sizeof(node));
//    strcpy(p->name, "ccc");
//    p->next = NULL;
//    q = (node*)malloc(sizeof(node));
//    strcpy(q->name, "aaa");
//    q->next = NULL;
//
//
//    k[0] = p;
//    k[1] = q;
//    k[2] = (node*)malloc(sizeof(node));
//    strcpy(k[2]->name, "bbb");
//
//    printf("%x\n", (k[0]));
//    printf("%x\n", (k[1]));
//    printf("%x\n", (k[2]));
//
//    puts("\n-----");
//    printf("%s\n", k[0]->name);
//    printf("%s\n", k[1]->name);
//    printf("%s\n", k[2]->name);
//
//    qsort(k, 3, sizeof(int), cmp_node);
//
//    puts("\n-----");
//    printf("%x\n", (k[0]));
//    printf("%x\n", (k[1]));
//    printf("%x\n", (k[2]));
//
//    puts("\n-----");
//    printf("%s\n", k[0]->name);
//    printf("%s\n", k[1]->name);
//    printf("%s\n", k[2]->name);
//
//
//}


//
////#include <stdarg.h>
//typedef char* va_list;
//#define _INTSIZEOF(n)   ( (sizeof(n) + sizeof(int) - 1) & ~(sizeof(int) - 1) )
//#define va_start(ap,v)  ( ap = (va_list)&v + _INTSIZEOF(v) )
//#define va_arg(ap,t)    ( *(t *)((ap += _INTSIZEOF(t)) - _INTSIZEOF(t)) )
//#define va_end(ap)      ( ap = (va_list)0 )
//
//main()
//{
//	float x;
//	x = average(10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
//	printf("first avg is %f\n", x);
//	x = average(5, 2, 2, 2, 2, 2);
//	printf("second avg is %f", x);
//	return(0);
//}
//
//float average(int num, ...)
//{
//	va_list arg_ptr;
//	int cnt, total = 0;
//	va_start(arg_ptr, num);
//	for (cnt = 0; cnt < num; cnt++)
//		total += va_arg(arg_ptr, int);
//	va_end(arg_ptr);
//	return ((float)total / num);
//}

#define Q_SIZE 5

int queue[Q_SIZE];
int front, rear;

void init_queue(void) {
	front = rear = 0;
}

void put(int data) {//rear 위치에 넣는다
	if ((rear+1)%5 == front)
	{
		printf("data overflow");
	
	}
	else 
	{
		if (rear == 4)
		{
			rear = 0;
			queue[rear++] = data;
			printf("%d put in rear %d\n ", queue[rear-1], rear);
		}
		else
			queue[rear++] = data;
			printf("%d put in rear %d\n", queue[rear-1],rear);
	
	}


}

int get(void) {	//front 위치로부터 뺀다

	
}

main() {

	init_queue();
	put(1);
	put(2);
	put(3);
	put(4);
	put(4);

	


}

































































