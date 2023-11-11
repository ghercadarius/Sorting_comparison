#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <stdlib.h>
#include <cstring>
using namespace std;
using namespace std::chrono;

vector <unsigned long long> numbers;

void count_sort(){
    unsigned long long maxi = 0;
    for(auto i:numbers){
        if(i > maxi)
            maxi = i;
    }
    vector<unsigned long long> a;
    a.reserve(maxi+1);
    for(int i = 0;i <= maxi; i++)
        a[i] = 0;
    int cap = numbers.size();
    for(auto i:numbers){
        a[i]++;
    }
    numbers.clear();
    int opc = 0;
    for(unsigned long long i = 0; i <= maxi;i++){
        while(a[i] > 0){
            numbers.push_back(i);
            opc++;
            if(opc % 100000 == 0)
                cout<<"!";
            a[i]--;
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
    count_sort();
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