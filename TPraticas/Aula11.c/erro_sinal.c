#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int MAX_SIZE = 2048;


void vulneravel (char *origem, size_t tamanho) {
        int tamanho_real;
        char *destino;
        if (tamanho > 1) {
                tamanho_real = tamanho - 1; // Não copiar \0 de origem para destino
                if (tamanho_real < MAX_SIZE) {
                        destino = (char *) malloc(tamanho_real);
                        memcpy(destino, origem, tamanho_real);
                }
        }
}

int main() {
}
