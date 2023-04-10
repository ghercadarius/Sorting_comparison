import os, random, time, subprocess, io
sdf = {}
def file_gen(nr_num, nrcif, seconds, exec, outfile) :

    return retcal
print(int(time.time()*1000))
n = int(input("nr teste:"))
nr_cif = int(input("nr cifre:"))
nr_numere = int(input("nr numere:"))
sdf["bubble"] = ("bubblesort.exe", "bubble.txt")
sdf["counting"] = ("countingsort.exe", "counting.txt")
sdf["merge"] = ("mergesort.exe", "merge.txt")
sdf["quick"] = ("quicksort.exe", "quick.txt")
sdf["radix"] = ("nradix_seed.exe", "radix.txt")
sdf["shell"] = ("shellsort.exe", "shell.txt")
#sdf[""]
os.chdir('sort_data')
print(os.getcwd())
for t in range(n):
    seconds = int(time.time()*1000)
    x = random.randint( 10 ** nr_cif , 10 ** (nr_cif + 1) )
    n = random.randint( nr_numere , 10 * nr_numere )
    for i in sdf.keys():
        #retcal = file_gen(n, x, seconds, sdf[i][0], sdf[i][1])
        print(i + " start")
        param = str(seconds) + "\n" + str(n) + "\n" + str(x) + "\n"
        #input_data = io.StringIO( param )
        print(param)
        exec = sdf[i][0]
        proc = subprocess.run( [ exec ], input = param, text = True, shell = True)
        print(i + " end")