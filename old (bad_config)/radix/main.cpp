#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <stdlib.h>
#include <cstring>
using namespace std;
using namespace std::chrono;

void radix_sort(vector <unsigned long long> &a){
    int pwr = 1, maxi=-1;
    for(auto i:a)
        maxi = max(maxi, int(i));
    vector <int> buk[10];
    while(maxi/pwr != 0){
        for(auto i:a){
            int c = (i/pwr)%10;
            buk[c].push_back(i);
        }
        a.clear();
        for(int i = 0; i <= 9;i++){
            for(auto j:buk[i]){
                a.push_back(j);
            }
            buk[i].clear();
        }
        pwr = pwr * 10;
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
    string ffile, gfile;
    ifstream r("file_name.in");
    r >> ffile >> gfile;
    vector <unsigned long long> v;
    ofstream g(gfile);
    g<<"alocat";
    g.close();
    ifstream f(ffile);
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
    g.open(gfile);
    g<<"err";
    g.close();
    auto start = high_resolution_clock::now();
    radix_sort(v);
    auto stop = high_resolution_clock::now();
    g.open(gfile);
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
