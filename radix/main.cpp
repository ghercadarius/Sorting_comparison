#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <stdlib.h>
using namespace std;
using namespace std::chrono;


// A function to do counting sort of arr[] according to
// the digit represented by exp.
void countSort(vector <unsigned long long> *arr, unsigned long long n, unsigned long long exp)
{
    vector <unsigned long long> output; // output array
    output.reserve(n+2);
    long long i, count[12];
    for(int i = 0; i <= 11; i++)
    {
        count[i] = 0;
    }
    // Store count of occurrences in count[]
    for (i = 0; i < n; i++){
        long long aux = (*arr)[i] / exp;
        aux = aux % 10;
        count[aux]++;
    }
    // Change count[i] so that count[i] now contains actual
    //  position of this digit in output[]
    for (i = 1; i < 10; i++)
        count[i] += count[i - 1];

    // Build the output array
    for (i = n - 1; i >= 0; i--) {
        output[count[((*arr)[i] / exp) % 10] - 1] = (*arr)[i];
        count[((*arr)[i] / exp) % 10]--;
    }

    // Copy the output array to arr[], so that arr[] now
    // contains sorted numbers according to current digit
    for (i = 0; i < n; i++)
        (*arr)[i] = output[i];
}

// The main function to that sorts arr[] of size n using
// Radix Sort
void radixsort(vector <unsigned long long> *arr, long long n)
{
    // Find the maximum number to know number of digits
    long long m = -1;
    for (auto i:*arr){
        m = max(m, (long long)i);
    }
    // Do counting sort for every digit. Note that instead
    // of passing digit number, exp is passed. exp is 10^i
    // where i is current digit number
    for (long long exp = 1; m / exp > 0; exp *= 10){
        countSort(arr, n, exp);
    }
}

bool verif(vector <unsigned long long> v){
    unsigned long long i = 1;
    while(i < v.size() && v[i-1] <= v[i]){
        i++;
    }
    if(i == v.size())
        return true;
    return false;
}

int main()
{
    vector <unsigned long long> v;
    ofstream g("rsmare.out");
    g<<"alocat";
    g.close();
    ifstream f("rsmare.in");
    long long seconds;
    f>>seconds;
    srand(seconds);
    long long n;
    f>>n;
    long long max_number;
    f>>max_number;
    f.close();
    for(long long i = 1; i <= n; i++){
        v.push_back(rand() % max_number);
    }
    /*for(auto i:v){
        cout<<i<<"\n";
    }*/
    g.open("rsmare.out");
    g<<"err";
    g.close();
    auto start = high_resolution_clock::now();
    radixsort(&v, n);
    auto stop = high_resolution_clock::now();
    g.open("rsmare.out");
    if(!verif(v)){
        g<<"inf";
        g.close();
    }
    else{
        auto duration = duration_cast <microseconds> (stop - start);
        g<<duration.count();
        g.close();
    }
    v.clear();
    return 0;
}
