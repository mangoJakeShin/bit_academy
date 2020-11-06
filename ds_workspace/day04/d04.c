#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>

#pragma warning(disable:4996) 
#define SWAP(a,b)	do{ int t; t= a;a=b;b=t;}while(0)

#include<string.h>

//
#define Q_SIZE 5
//
//int queue[Q_SIZE];
//int front, rear;
//void put(int a);
//int get();
//void init_queue();
//main() {
//	int r;
//	init_queue();
//	put(1);
//	put(2);
//	put(36);
//
//	printf("%d\n", get());
//	printf("%d\n", get());
//	put(3);
//	put(36);
//
//
//	for(r = front;r!=rear;r=++r%5){
//		if (queue[r] != NULL)
//			printf("emp\t");
//	//for (r = 0;r < 5;r++) {
//		//if (queue[r] != NULL)
//		
//		
//			printf("%d\t", queue[r]);
//		}
//		
//
//}
//
//void init_queue(void) {
//	front = rear = 0;
//}
//
//void put(int data) {//rear 위치에 넣는다
//	if ((rear + 1) % 5 == front)
//	{
//		printf("data overflow\n");
//
//	}
//	else
//	{
//		if (rear == 4)
//		{
//			rear = 0;
//			queue[rear++] = data;
//			printf("%d put in rear %d\n ", queue[rear - 1], rear);
//		}
//		else
//		{
//			queue[rear++] = data;
//			printf("%d put in rear %d\n", queue[rear - 1], rear);
//		}
//	}
//
//
//}
//
//int get(void) {	//front 위치로부터 뺀다
//	int rlt;
//
//	if (front == rear)
//	{
//		printf("data underflow. Queue empty\n");
//		return -1;
//	}
//	rlt = queue[front];
//	front = ++front % 5;
//	return rlt;
//
//
//}

//********************************************
#define NDEBUG
#include<assert.h>
//
//void init_queue();
//
//typedef struct _tree Tree;
//void pre_order(Tree* t);
//void in_order(Tree* t);
//void post_order(Tree* t);
//void pre_order_stack(Tree * b);
//void stack_init();
//void push(Tree * data);
//Tree* pop();
//int stack_empty();
//void in_order_stack(Tree * b);
//void post_order_stack(Tree * b);
//#define STACK_SIZE 5
//int front, rear;
//int queue_empty();
//void level_order_queue(Tree * b);
//Tree* Stack[STACK_SIZE];
//int top;
//int queue[Q_SIZE];
//void put(Tree* data);

//typedef struct _tree {
//	int key;
//	Tree* left;
//	Tree* right;
//
//}Tree;
//
//main() {
//
//	Tree a1 = { 1,NULL,NULL };
//	Tree b2 = { 2,NULL,NULL };
//	Tree c3 = { 3,NULL,NULL };
//	Tree d4 = { 4,NULL,NULL };
//	Tree e5 = { 5,NULL,NULL };
//	Tree f6 = { 6,NULL,NULL };
//
//	c3.left = &a1;
//	a1.right = &b2;
//
//	c3.right = &d4;
//	d4.right = &e5;
//	e5.right = &f6;
//
//	//전위순회 (pre) 
//	//pre_order(&c3);
//	//puts("\n");
//	//in_order(&c3);
//	//puts("\n");
//	//post_order(&c3);
//
//	////pre_order_stack(&c3);
//	//puts("");
//	////in_order_stack(&c3);
//	//puts("");
//	level_order_queue(&c3);
//
//}
//
//
//
//void pre_order(Tree* p) {
//	if (p != NULL) {
//		printf("%d\n", p->key);
//		pre_order(p->left);
//		pre_order(p->right);
//	}
//}
//
//void in_order(Tree* p) {
//	if (p != NULL) {
//		in_order(p->left);
//		printf("%d\n", p->key);
//		in_order(p->right);
//	}
//}
//
//void post_order(Tree* p) {
//	if (p != NULL) {
//		post_order(p->left);
//		post_order(p->right);
//		printf("%d\n", p->key);
//	}
//}
//
//void pre_order_stack(Tree* a) {
//	//root 를 push 후 비어있지 않으면 pop + 출력, 후 우좌측 자식을 push
//	stack_init();
//
//	push(a);//root를 push
//	while (!stack_empty())//비어있지 않으면
//	{
//		a = pop();//pop 한 후
//		if (a != NULL)
//		{
//			push(a->right);
//			push(a->left);
//			printf("%d\t", a->key);
//
//		}
//	}
//
//}
//
//void in_order_stack(Tree* a) {
//	//왼쪽 자식이 없을때 까지 푸시
//	//비어있지 않으면 pop한 후 오른쪽 자식을 스택에 푸쉬(왼쪽자식이 없을때 까지)
//	stack_init();
//	while (1) {
//
//		while (a != NULL) {
//			push(a);
//			a = a->left;
//		}
//		if (!stack_empty())
//		{
//			a = pop();
//			printf("%d\t", a->key);
//			a = a->right;
//		}
//		else//stack empty
//			break;
//	}
//
//}
//
//
//
//
//void stack_init() {
//	top = -1;
//}
//void push(Tree* data) {
//
//	if (top >= STACK_SIZE -1){
//		puts("Stack overflow");
//		return;	
//	}
//	Stack[++top] = data;		
//
//}
//Tree* pop() {//데이터 추출
//	// 다 뺏은 상태에서 또 뺏을 때 에러 
//	if (top < 0) {
//		printf("stack empty");
//		return -1 ;//return null
//	}
//	else
//		return Stack[top--];
//}
//
//
//int stack_empty() {
//	if (top<0) {
//		puts("stack underflow\n");
//		return 1;
//	}
//	else
//		return 0;
//}
//
//
//
//
//void put(Tree* data) {//rear 위치에 넣는다
//	if ((rear + 1) % 5 == front)
//	{
//		printf("data overflow\n");
//
//	}
//	else
//	{
//		if (rear == 4)
//		{
//			rear = 0;
//			queue[rear++] = data;
//			//printf("%d put in rear %d\n ", queue[rear - 1], rear);
//		}
//		else
//		{
//			queue[rear++] = data;
//			//printf("%d put in rear %d\n", queue[rear - 1], rear);
//		}
//	}
//
//
//}
//
//int get(void) {	//front 위치로부터 뺀다
//	int rlt;
//
//	if (front == rear)
//	{
//		printf("data underflow. Queue empty\n");
//		return -1;
//	}
//	rlt = queue[front];
//	front = ++front % 5;
//	return rlt;
//
//
//}
//int queue_empty() {
//	if (front == rear) {
//		puts("queue underflow\n");
//		return 1;
//	}
//	else
//		return 0;
//}
//void level_order_queue(Tree* p) {
//	put(p);
//	while (!queue_empty()) {
//		p = get();	//뺀것의 좌우측 노드를 넣는다 
//		printf("%d\t", p->key);
//		if (p->left != NULL)
//			put(p->left);
//		if (p->right != NULL)
//			put(p->right);
//	}
//}//************************************************queue + tree
//
//typedef struct _tree {
//	int key;
//	Tree* left;
//	Tree* right;
//
//}Tree;
//
//
//int depth_tree(Tree* p, int dep)
//{
//	int l_dep, r_dep;
//	l_dep = r_dep = dep;
//	if (p->left != NULL)
//		l_dep = depth_tree(p->left, l_dep + 1);
//	if (p->right != NULL)
//		r_dep = depth_tree(p->right, r_dep + 1);
//
//	if (l_dep >= r_dep)
//		return l_dep;
//	else 
//		return r_dep;
//
//}
//Tree* balance(int n) {
//	int ln, rn;
//	Tree* r;
//	if (n > 0) {
//		ln = (n - 1) / 2;
//		rn = n - ln-1;
//		r = (Tree*)malloc(sizeof(Tree));
//		r->left = balance(ln);
//		r->key = sortArr[idx++];
//		r->right= balance(rn);
//		return r;
//
//	}
//	return NULL;
//}
//
//
//main() {
//
//	Tree a1 = { 1,NULL,NULL };
//	Tree b2 = { 2,NULL,NULL };
//	Tree c3 = { 3,NULL,NULL };
//	Tree d4 = { 4,NULL,NULL };
//	Tree e5 = { 5,NULL,NULL };
//	Tree f6 = { 6,NULL,NULL };
//	Tree g7 = { 6,NULL,NULL };
//	Tree h8 = { 6,NULL,NULL };
//
//	c3.left = &a1;
//	a1.right = &b2;
//
//	c3.right = &d4;
//	d4.right = &e5;
//	e5.right = &f6;
//	f6.right = &g7;
//	g7.right = &h8;
//
//	//전위순회 (pre) 
//	//pre_order(&c3);
//	//puts("\n");
//	//in_order(&c3);
//	//puts("\n");
//	//post_order(&c3);
//
//	////pre_order_stack(&c3);
//	//puts("");
//	////in_order_stack(&c3);
//	//puts("");
//	//level_order_queue(&c3);
//	int r = depth_tree(&c3, 0);
//	printf("depth %d\n", depth_tree(&c3, 0));
//	printf("depth %d\n", depth_tree(c3.left, 0));
//	printf("depth %d\n", depth_tree(c3.right, 0));
//
//}
//

//void findz(char(*a)[15], int n, char* c);
//void findz(char (*a)[15], int n, char* c) {
//	int r;
//	int k = n / 2;
//	char* cmp = a[k];
//	r = strcmp(cmp, c, 1);
//	if (r == 1)
//		findz(a, k, c);
//	else if (r == -1)
//		findz(a, (n + k), c);
//	else {
//		printf("in the list");
//		return;
//	}
//
//}
//
//
//main() {
//
//	char* name_arr[][15] = { "Alice", "Bill", "Carol", "David", "Elvis", "Fred", "Gabriel",
//		"Helen", "Isabel", "Jane", "Kuper", "Louic", "Mathilda", "Nadia", "Olive", "Pablo", " Queen", "Rambo", "Scarlet",
//		"Trisha", "Umberto", "Vincent", "Wily", "Xxx", "Yuki", "Zorro" };
//
//	char target[] = "Pablo";
//
//	findz(name_arr, 26, target);
//}


void findz(char(*a)[15], int n, char* c) {
	int r;
	int k = n / 2;
	char* cmp = a[k];
	r = strcmp(cmp, c, 1);
	if (r == 1)
		findz(a, k, c);
	else if (r == -1)
		findz(a, (n + k), c);
	else {
		printf("in the list");
		return;
	}

}


main() {

	char name_arr[][15] = { "Alice", "Bill", "Carol", "David", "Elvis", "Fred", "Gabriel",
		"Helen", "Isabel", "Jane", "Kuper", "Louic", "Mathilda", "Nadia", "Olive", "Pablo", " Queen", "Rambo", "Scarlet",
		"Trisha", "Umberto", "Vincent", "Wily", "Xxx", "Yuki", "Zorro" };

	char target[] = "Pablo";

	findz(name_arr, 26, target);
}































































