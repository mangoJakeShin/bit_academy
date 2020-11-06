#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>

#pragma warning(disable:4996) 
#define SWAP(a,b)	do{ int t; t= a;a=b;b=t;}while(0)

#include<string.h>

typedef struct _list list;
int rand_maker(void);
void addtofront(int a);
void init_list();
list* head, * tail;
int comparelist(int a);
void nodemaker(int a);
void newmaker(int a);
void listview();


int main(void) {
	srand(time(NULL));
	init_list();
	int r;
	while (1) {
		r = rand_maker();
		comparelist(r);
		printf("comparelist end\n");
		listview();
	}
}//main end

struct _list {
	int name;
	int data;
	struct _list* front;
	struct _list* back;

};//struct define end

void init_list() {
	head = (list*)malloc(sizeof(list));
	tail = (list*)malloc(sizeof(list));
	head->data = NULL;
	tail->data = 11;
	head->back = tail;
	head->front = tail;
	tail->front = head;
	tail->back = head;

}//init_list end



int rand_maker(void) {
	int r = 0;
	r = rand() % 10;
	printf("\n%d generated\n", r+1);
	return r+1;

}//rand maker end

void addtofront(list* wk, int a) {
	list* node= (list*)malloc(sizeof(list));
	node->data = NULL;
	node->back= NULL;
	node->front = NULL;

	if (wk != head&&wk!=tail) {
		node->front = wk->front;
		node->back = wk;
		node->data = a;
		//list* a;
		wk->front->back= node;
		wk->front = node;
	}
	else if (wk == tail) {
		node->data = a;
		node->front = tail->front;
		tail->front->back = node;
		tail->front = node;
		node->back = tail;
		printf("*******************************************");
	}
	else {
		node->data = head->data;
		node->back = head->back;
		node->front = head;
		head->back = node;
		head->data = a;
		tail->front= node;
	}

}//addtofront end

void addtoback(list* a) {


}

void newmaker(int a) {
	head->data = a;
	printf("%d insert complete \n", head->data);
}


int comparelist(int b) {
	printf("cmplist initiated\n");
	list* wk;
	wk = head;
	do{
		if (wk->data == NULL) {
			newmaker(b);
		}

		else if (b == wk->data)
			break;
		else
		{
			if (b <= (wk->data))
				wk = wk->back;
			else 
			{
				addtofront(wk, b);
				break;
			}
		}
	
	}
		while (wk != tail);



}//comparelist end

void listview() {
	list* wk;
	int i=0;
	wk = head;
	printf("Ãâ·Â: ");
	while (wk != tail)
	{
		printf("%d  ", wk->data);
		wk = wk->back;
		i++;

	}
			printf("\n");
	//printf("%d\n", i);
	printf("%d", wk->front->data);

}




























