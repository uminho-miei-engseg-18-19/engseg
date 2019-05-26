/* 
 * File:   InputValidation.cpp
 * Author: jepm
 *
 * Created on November 12, 2014, 7:54 PM
 */

#include <iostream>

using namespace std;
int main(void)
{
  unsigned int vals[10];
  size_t which;
  unsigned int square;

  for (size_t i = 0; i < 10; i++ )
    vals[i] = (i+1)*(i+1);

  cout << "Insira um número: ";
  cin >> which;

  square = vals[which-1];
  cout << "O quadrado de " << which << " é " << square << endl;
  return 0;
}
