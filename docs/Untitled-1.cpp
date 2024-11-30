#include <iostream>
#include <bitset>
int main() {
    int a = 2047;
    int b = 6;
    std::bitset<15> x(a);
    std::bitset<4> y(b);
    std::cout << x << " " << y;
    return 0;
}