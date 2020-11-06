#include <stdio.h>

int get_bank();

void set_bank();

int main() {

	int withdraw;
	set_bank();

	withdraw = get_bank();

	printf("%d\n", withdraw);
}