#include <stdio.h>

int main(int argc, char **argv) {
        char buf[64];

        if(argc == 1) {
                errx(1, "please specify an argument\n");
        }
        snprintf(buf, sizeof(buf), "file %s", argv[1]);
        system(buf);
}
