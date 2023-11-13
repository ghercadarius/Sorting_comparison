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
void interclasare(long long st,long long dr)
{
    vector <unsigned long long> aux(numbers.size());
    long long m=(st+dr)/2;
    long long i=st,j=m+1,k=st;
    while(i<=m && j<=dr)
    {
        if(numbers[i]<=numbers[j])
        {
            aux[k++]=numbers[i++];
        }
        else
        {
            aux[k++]=numbers[j++];
        }
    }
    while(i<=m)
    {
        aux[k++]=numbers[i++];
    }
    while(j<=dr)
    {
        aux[k++]=numbers[j++];
    }
    for(k=st;k<=dr;k++)
    {
        numbers[k]=aux[k];
    }
}

void merge_sort(long long st,long long dr)
{   cont++;
    if(cont % 1000 == 0)
        cout << "!";
    if(st==dr)
    {
        return;
    }
    int m=(st+dr)/2;
    merge_sort(st,m);
    merge_sort(m+1,dr);
    interclasare(st,dr);
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
    merge_sort(1, numbers.size() - 1);
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