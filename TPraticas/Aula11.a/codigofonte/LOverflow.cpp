#include <iostream>

using namespace std;

int main(void) {
    int importantData = 1;
    int  buffer[10];

    for (int i =0; i < 500; i++) {  
      buffer[i] = 7;
      cout << "i = " << i << endl;
    }

    cout << "after buffer overflow " << endl;
    cout << "Important data  = " << importantData << endl;

    return 0;
}

