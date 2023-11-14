#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <stdlib.h>
#include <cstring>
using namespace std;
using namespace std::chrono;

vector <unsigned long long> numbers;
int cont = 0;

void quicks(long long st, long long dr){
    cont++;
    if(cont % 1000 == 0){
        cout << "!";
    }
    if(st<dr){
        long long i = st - 1, j = st, piv = numbers[dr];
        while(j < dr){
            if(numbers[j] < piv){
                i++;
                swap(numbers[i], numbers[j]);
            }
            j++;
        }
        swap(numbers[dr], numbers[i+1]);
        quicks(st, i);
        quicks(i+2, dr);
    }
}

int main(int argc, char* argv[]) {
    long long seconds, nr_numbers, max_number;
    seconds = atoll(argv[1]);
    nr_numbers = atoll(argv[2]);
    max_number = atoll(argv[3]);
    srand(seconds);
    for(int i = 1; i <= nr_numbers; i++){
        if(i % 10000 == 0){
            cout << ".";
        }
        numbers.push_back(rand() % max_number);
    }
    cout << "GEN\n";
    auto start = high_resolution_clock::now();
    quicks(0, numbers.size() - 1);
    auto stop = high_resolution_clock::now();
    cout << "END\n";
    ofstream g("output.out", ios::ate);
    while(!g.is_open()){
        g.open("output.out", ios::ate);
    }
    auto duration = duration_cast <microseconds> (stop - start);
    g << duration.count() << "\n";
    g.close();
    return 0;
}
/// call example: bubble.exe 12943234 1000 100