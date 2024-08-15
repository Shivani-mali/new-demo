#include <iostream>
using namespace std;

int main() {
    char operation;
    float num1, num2;

    // Ask the user to enter the operation they want to perform
    cout<< "Enter an operator (+, -, *, /): ";
    cin >> operation;

    // Ask the user to enter two numbers
    cout << "Enter two numbers: ";
    cin >> num1 >> num2;

    switch(operation) {
        case '+':
            cout << num1 << " + " << num2 << " = " << num1 + num2 << endl;
            break;
        case '-':
            cout << num1 << " - " << num2 << " = " << num1 - num2 << endl;
            break;
        case '*':
            cout << num1 << " * " << num2 << " = " << num1 * num2 << endl;
            break;
        case '/':
            if (num2 != 0)
                cout << num1 << " / " << num2 << " = " << num1 / num2 << endl;
            else
                cout << "Error! Division by zero." << endl;
            break;
        default:
            cout << "Error! Invalid operator." << endl;
            break;
    }


    return 0;
}
