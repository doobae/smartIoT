#include <iostream>
using namespace std;
int main() {
long fact = 1;
int n;
cout << "input number: ";
cin >> n;
for(int i=1; i<=n; i++) {
fact = fact*i;
}
cout << n << "! = " << fact << endl;
return 0;
}
