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

void shell_sort(){
    for (long long interval = numbers.size() / 2; interval > 0; interval /= 2) {
        for (long long i = interval; i < numbers.size(); i += 1) {
            long long aux = numbers[i];
            long long j;
            for (j = i; j >= interval && numbers[j - interval] > aux; j -= interval) {
                cont += 1;
                if(cont % 1000 == 0)
                    cout<<"!";
                numbers[j] = numbers[j - interval];
            }
            numbers[j] = aux;
        }
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
    shell_sort();
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