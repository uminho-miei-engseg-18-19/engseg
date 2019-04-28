/* Exemplo adaptado de http://knavite.blogspot.in/2014/07/linux-memory-layout-test-through-c.html */

#include<stdio.h>
#include<stdlib.h>
#pragma GCC optimize ("O0")
 
// Variáveis não inicializadas
int g1;
int g2;
 
// Variáveis inicializadas 
int g3=5;
int g4=7;
 
// Funções para testar a stack
void func2(int i, int j) {
	int var1;
	int var2;
	printf("Stack - função func2:\t\t\t %p %p %p %p\n",&i, &j, &var1,&var2);
}
 
void func(int i, int j) {
	int var1;
	int var2;
	printf("Stack - função func:\t\t\t %p %p %p %p\n",&i, &j, &var1,&var2);
	func2(2,2);
}
 
int main(int argc, char* argv[], char* evnp[]) {
	
	// Argumentos de linha de comando
	printf("Variáveis de comando linha e ambiente:\t %p %p %p\n",&argc,argv,evnp);
	
        // Variáveis locais vão para a stack e stack cresce para baixo 
	int var1;
	int var2;
	printf("Stack - função main:\t\t\t %p %p\n",&var1,&var2);
	func(1,1);
	
	// Memória dinâmica vai para a Heap, que cresce para cima
	void *arr1 = malloc(5);
	void *arr2 = malloc(5);
	printf("Heap:\t\t\t\t\t %p\n",arr2);
	printf("Heap:\t\t\t\t\t %p\n",arr1);
	free(arr1);
	free(arr2);
	
	// Variáveis globais inicializadas e não inicializadas
	printf("Variável global não inicializada:\t %p %p\n",&g1,&g2);
	printf("Variável global inicializada:\t\t %p %p\n",&g3,&g4);
	
	//Código executável vai para o segmento de texto
	printf("Text Data:\t\t\t\t %p %p %p\n",main,func,func2);
	return 0;
}

