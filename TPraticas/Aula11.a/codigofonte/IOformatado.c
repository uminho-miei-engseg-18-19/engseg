
#include <stdio.h>

// Função de leitura segura
void segura() {
    char buf[80];
    if (fgets(buf, sizeof(buf), stdin) == NULL)
        return;
    printf("ECO |%s", buf);
}

// Função de leitura vulneravel
void vulneravel() {
    char buf[80];
    if (fgets(buf, sizeof(buf), stdin) == NULL)
        return;
    printf(buf);
}

int main () {
    printf("Leitura segura: ");
    segura();
    printf("Leitura vulneravel: ");
    vulneravel();
}