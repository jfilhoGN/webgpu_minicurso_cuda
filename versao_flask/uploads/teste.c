#include <stdio.h>

int main(int argc, char const *argv[])
{
	int vetor[14] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13};
	int i, j, aux=0;
	for (i = 0; i < 8; i++){
		printf("entrou 1: %d\n", vetor[i]);
		aux = i+1;
		
	}
	printf("\n");
	for(aux;aux<14;aux++ ){
			printf("entrou 2: %d\n", vetor[aux] );
	}
	return 0;
}