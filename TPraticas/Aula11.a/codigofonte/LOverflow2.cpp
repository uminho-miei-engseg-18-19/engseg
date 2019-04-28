

#include <iostream>

using namespace std;

int main(void) {
    int test = 1;
    int  tests[10];
    int num_elems;

   cout << "Quantos números? ";
   cin >> num_elems;
   
    for (int i = 0; i < num_elems; i++) {  
      cout << "Insira número: ";
      cin >> test;
      tests[i] = test;
    }

    return 0;
}


