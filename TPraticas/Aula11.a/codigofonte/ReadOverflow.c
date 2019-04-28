#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    char buf[100], *p;
    int i, len;

    while (1) {
        printf("Insira numero de caracteres: ");
        p = fgets(buf, sizeof(buf), stdin);
        len = atoi(p);
        printf("Insira frase: ");
        p = fgets(buf, sizeof(buf), stdin);
        printf("ECO: |");
        for (i=0; i<len; i++) {
            if (!iscntrl(buf[i])) putchar(buf[i]);
            else putchar('.');
        }
        printf("|\n");
    }
}

