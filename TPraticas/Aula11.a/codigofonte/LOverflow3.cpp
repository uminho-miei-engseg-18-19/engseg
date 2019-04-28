/* 
 * File:   Overflow3.cpp
 * Author: jepm
 *
 * Created on November 13, 2014, 12:40 PM
 */

#include <iostream>
using namespace std;

int main(void)
{
  int vals[10];
  size_t count;
  size_t which;

  cout << "Quantos valores quer guardar no array? ";
  cin >> count;

  for (size_t i = 0; i < count; i++) {
    vals[i] = count-i;
  }

  cout << "Que valor deseja recuperar? ";
  cin >> which;

  cout << "O valor é " << vals[which] << endl;

  return 0;
}
