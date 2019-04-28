#include <stdio.h>
#include <string.h>

void debug() {
   printf("Palavras-chave:\n");
   printf("root: ola123\n");
   printf("admin: 3eLdf75\n");
}

void store(char *valor) {
   char buf[10];
   strcpy(buf, valor);
}

int main(int argc, char **argv) {
   printf("Endereco da funcao debug: %p\n", &debug);
   store(argv[1]);
}
