// compile 
// gcc 3-return.c -o 3-return 

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
  char buffer[64];

  printf("You win this game if you are able to call the function win.'\n");
  
  gets(buffer);
}
