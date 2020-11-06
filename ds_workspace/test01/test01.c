#include <stdio.h>
#pragma warning(disable:4996) 
#include <stdlib.h>
#include <time.h>
#define swap(a,b) do{int t; t = a;a=b;b=t;}while(0)


//typedef struct _list List;
//void insert_list(int data);
//void new_list();
//void init_list();
//void view_list();
//void find_list(int data);
//void del_list(int data);
//void ordered_insert(int data);
//void movetofront(int data);
//void inserttofront(int data);
//
//main() {
//	init_list();
//	//insert_list(155);
//	//insert_list(717);
//	//insert_list(87);
//	//insert_list(7);
//	//view_list();
//	puts("");
//	find_list(7);
//	del_list(77);
//	puts("");
//	view_list();
//	ordered_insert(13);
//	ordered_insert(9);
//	ordered_insert(192);
//	ordered_insert(169);
//	puts("");
//	view_list();
//	movetofront(169);
//	view_list();
//}
//
//
//struct _list {
//	int key;
//	struct _list* next;	// node 생성 
//
//};//struct _list end
//
//List* head, * tail;		//양쪽 기둥 이름 
//
//void init_list(void) {
//	head = (List*)malloc(sizeof(List));
//	tail = (List*)malloc(sizeof(List));
//	head->next = tail;
//	tail->next = tail;
//
//}//init_list end
//
//
//void insert_list(int data) {
//	List* nw;
//	nw = (List*)malloc(sizeof(List));
//	nw->key = data;
//	nw->next = head->next;
//	head->next = nw;
//
//}
//
//void view_list() {
//	List* wk;
//	wk = head->next;
//	
//	/*wk = head->next;
//	printf("%d\n", wk->key);
//	wk = wk->next;
//	printf("%d\n", wk->key);*/
//
//	while (wk != tail) {
//		printf("%d\n", wk->key);
//
//		wk = wk->next;
//
//	}
//}
//void find_list(int data) {
//	List* wk;
//	wk = head->next;
//
//	/*while (wk != tail) {
//		if (wk->key == data)
//		{
//			printf("data exist\n");
//			break;
//		}wk = wk->next;
//	}
//	if (wk == tail)
//		printf("no data\n");
//*/
//	while (wk -> key != data && wk != tail) {
//		wk = wk->next;
//	}
//	if (wk == tail)
//		printf("no data\n");
//	else
//		printf("%d exists\n", data);
//
//}
//
//void del_list(int data) {
//	List* wk;
//	List* del;
//	//wk = head->next;
//	wk = head;
//	while (wk->next->key != data && wk->next != tail) {
//		wk = wk->next;
//	}
//	if (wk->next == tail) {
//		printf("%d does not exist\n",data);
//	}
//	else
//	{
//		del = wk->next;
//		wk->next = wk->next->next;
//		free(del);
//		printf("%d delete complete\n", data);
//
//
//	}
//
//
//	//while (wk != tail) {
//	//	if (wk->key == data)
//	//	{
//	//		wk->key = wk->next->key;
//	//		wk->next = wk->next->next;
//	//		printf("delete complete\n");
//	//		break;
//	//	}
//	//	else
//	//	{
//	//		printf("nono data\n");
//	//	}
//	//		wk = wk->next;
//
//	//} tail 전 값일 경우 tail 주소값 출력됨
//	
//
//}
//
//void ordered_insert(int data) {
//	List* wk;
//	List* pre;
//	List* nw;
//	pre = head;
//	wk = head->next;
//	while (wk->key <= data && wk != tail)
//	{
//		pre = pre->next;
//		wk = wk->next;
//	}
//	nw = (List*)malloc(sizeof(List));
//	nw->key = data;
//	nw->next = wk;
//	pre->next = nw;
//
//}
//
//void inserttofront(int data) {	//데이터 맨 앞에 삽입
//	List* wk;
//	List* nw;
//	wk = head;
//	nw = (List*)malloc(sizeof(List));
//	nw->next = wk->next;
//	wk->next = nw;
//	nw->key = data;
//
//}
//
//void movetofront(int data) {	//찾은 데이터를 맨앞으로 이동
//	List* wk;
//	wk = head->next;
//
//	List* move;
//
//	while (wk->next->key != data && wk->next != tail) {
//		wk = wk->next;
//	}
//	if (wk->next == tail) {
//		printf("%d does not exist\n", data);
//	}
//	else
//	{
//		move = wk->next;
//		wk->next = wk->next->next;
//		move->next = head->next;
//		head -> next = move;
//		printf("%d moved to front\n", data);
//
//
//	}
//}


main() {
	int a = 8;
	int b = 0;
	int c;
	while (1) {
		scanf("%d", &b);
		if (b % 8 != 0) {
			c = ((b / 8) + 1) * 8;
			printf("%d\n", c);
		}
	}
}