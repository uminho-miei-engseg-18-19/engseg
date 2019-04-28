/* Exemplo retirado de http://www.geeksforgeeks.org/memory-layout-of-c-program/ */
#include <stdio.h>

int global; /* Variável não inicializada guardada no bss*/

int main(void)
{
    static int i = 100; /* Variável inicializada guardada no ds */
    return 0;
}
