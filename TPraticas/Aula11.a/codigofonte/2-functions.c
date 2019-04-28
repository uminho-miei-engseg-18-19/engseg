// compile 
// gcc 2-functions.c -o 2-functions 

#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void win()
{
  printf("Congratulations, you win!!! You successfully changed the code flow\n");
}

int main(int argc, char **argv)
{
  int (*fp)();
  char buffer[64];

  fp = 0;

  printf("You win this game if you are able to call the function win.'\n");

  gets(buffer);

  if(fp) {
      printf("calling function pointer, jumping to %p\n", fp);
      fp();
  }
}
