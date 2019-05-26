#include <stdio.h>

int main(int argc, char **argv) {
        char buf[64], c;
        FILE *fp;

        if(argc == 1) {
                errx(1, "please specify an argument\n");
        }

        snprintf(buf, sizeof(buf), "%s.txt", argv[1]);
        fp = fopen(buf,"r");
        if (fp == NULL) {
                errx(1, "file not existent\n");
        }
        while((c=fgetc(fp))!=EOF) {
                printf("%c",c);
        }
        fclose(fp);
}

