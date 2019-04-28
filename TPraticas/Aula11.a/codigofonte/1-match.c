// compile 
// gcc 1-match.c -o 1-match 

#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
  int control;
  char buffer[64];

  if(argc == 1) {
      errx(1, "please specify an argument\n");
  }

  printf("You win this game if you can change variable control to the value 0x61626364'\n");

  control = 0;
  strcpy(buffer, argv[1]);

  if(control == 0x61626364) {
      printf("Congratulations, you win!!! You correctly got the variable to the right value\n");
  } else {
      printf("Try again, you got 0x%08x\n, instead of 0x61626364", control);
  }
}
