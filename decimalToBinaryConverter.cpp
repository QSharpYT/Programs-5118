#include <list>
#include <iostream>

using namespace std;

int main() {
    int dec;
    int answer;
    list<int> binary;

    cout << "Decimal to Binary Converter\n";
    cout << "Please enter a decimal to convert to binary: ";
    cin >> dec;

    // If input is 0, binary is also 0
    if (dec == 0) {
        binary.push_front(0);
    } else {
        while (dec > 0) {
            int remainder = dec % 2;
            answer = dec / 2;
            binary.push_front(remainder);
            dec = answer;
        }
    }

    cout << "Binary: ";
    for (int bit : binary) {
        cout << bit;
    }
    cout << endl;

    return 0;
}
