#include<stdio.h>
#include"left.h"
#include"right.h"

/*
left 와 right 헤더에서 passbook을 extern 해주는 one의 헤더를 인클루드 함
left.c 에서는 get_bank()를 생성해놓았고 right.c에서는 set_bank()를 생성해놓았음. 
그래서 main.c에서는 left와 right를 include하는것으로 passbook의 기능을 사용할 수 있음. 

함수는 .c에 구현을 하고 다른 c 파일에서 쓰려면 헤더에 작성한 후 include 시켜야 함
구조체의 경우는 메모리를 배정받는 형태가 아니므로 헤더에 만들어 놓은 후 include 시켜야 함 

*/

int main() {
	int withdraw;
}