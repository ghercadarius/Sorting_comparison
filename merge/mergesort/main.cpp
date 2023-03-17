#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <stdlib.h>
#include <cstring>
using namespace std;
using namespace std::chrono;

void interclasare(vector <unsigned long long> &v,long long st,long long dr)
{
    vector <unsigned long long> aux(v.size());
    long long m=(st+dr)/2;
    long long i=st,j=m+1,k=st;
    while(i<=m && j<=dr)
    {
        if(v[i]<=v[j])
        {
            aux[k++]=v[i++];
        }
        else
        {
            aux[k++]=v[j++];
        }
    }
    while(i<=m)
    {
        aux[k++]=v[i++];
    }
    while(j<=dr)
    {
        aux[k++]=v[j++];
    }
    for(k=st;k<=dr;k++)
    {
        v[k]=aux[k];
    }
}

void merge_sort(vector <unsigned long long> &v,long long st,long long dr)
{
    if(st==dr)
    {
        return;
    }
    int m=(st+dr)/2;
    merge_sort(v,st,m);
    merge_sort(v,m+1,dr);
    interclasare(v,st,dr);
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
    merge_sort(v, 0, v.size() - 1);
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
