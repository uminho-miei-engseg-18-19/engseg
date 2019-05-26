/* 
 * File:   InputValidation2.cpp
 * Author: jepm
 *
 * Created on November 13, 2014, 11:32 AM
 */

#include <iostream>
using namespace std;

void getNames(string[], int);
int getWhich();
string getName(int, string[],int);
const int SIZE=5;

int main()
{
  int which;
  string names[SIZE];
  getNames(names,SIZE);

  which =getWhich();
  string aName = getName(which,names,SIZE);
  cout << "Escolheu o nome: "  << aName;

  return 0;
}

void getNames(string names[],int sz)
{
  for (size_t i = 0; i < sz; i++ )
  {
    cout << "Introduza nome #" << i+1 <<": ";
    cin >> names[i];
  }
}

int getWhich()
{
  size_t x;
  cout << "Escolha o nome #: ";
  cin >> x;
  return x;
}

string getName(int n,string vals[],int sz)
{
    if (n >=1 && n <= sz)
      return vals[n-1];
    else
      return "";
}
