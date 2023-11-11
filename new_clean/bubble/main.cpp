#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <stdlib.h>
#include <cstring>
using namespace std;
using namespace std::chrono;

vector <unsigned long long> numbers;

void bubblesort(){
    bool ok = 0;
    int progress = 0;
    do{
        progress++;
        if(progress % 10000 == 0){
            cout << ".";
        }
        ok = 1;
        for(int i = 0; i < numbers.size() - 1; i++){
            if(numbers[i] > numbers[i + 1]){
                swap(numbers[i], numbers[i + 1]);
                ok = 0;
            }
        }
    }while(!ok);
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
    bubblesort();
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