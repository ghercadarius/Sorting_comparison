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

void radix_sort(){
    int pwr = 1, maxi=-1;
    for(auto i:numbers)
        maxi = max(maxi, int(i));
    vector <int> buk[10];
    while(maxi/pwr != 0){
        for(auto i:numbers){
            cont++;
            if(cont % 1000 == 0)
                cout<<"!";
            int c = (i/pwr)%10;
            buk[c].push_back(i);
        }
        numbers.clear();
        for(int i = 0; i <= 9;i++){
            for(auto j:buk[i]){
                cont += 1;
                if(cont % 10000 == 0)
                    cout<<"!";
                numbers.push_back(j);
            }
            buk[i].clear();
        }
        pwr = pwr * 10;
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
    radix_sort();
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