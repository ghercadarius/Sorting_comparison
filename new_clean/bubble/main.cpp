#include <iostream>
#include <fstream>
using namespace std;

#define f cin

int main(int argc, char* argv[]) {
    long long a, b, c;
    a = atoll(argv[1]);
    b = atoll(argv[2]);
    c = atoll(argv[3]);
    ofstream g("output.out");
    g << a << " " << b << " " << c;
    g.close();
    return 0;
}
