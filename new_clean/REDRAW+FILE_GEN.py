def redraw_graph(L, canvas, w, h):
    canvas.delete("all")
    L = [x for x in L if x[1] != "err" and x[1] != "alocat"]
    L.sort(key = lambda x: x[0])
    wa = w * 0.001
    ha = h * 0.999
    for el in L:
        #if float(el[1]) < 0.5:
        #    nh = h - 0.3 * float( el[ 1 ] ) * h
        #elif float(el[1]) < 10:
        #    nh = h - 0.3 * h - 0.03 * float( el[ 1 ] ) * h
        #else:
        #    nh = h - 0.6 * h - 0.1 * float(el[1]) * h
        #if float(el[0]) < 5000:
        #    nw = w - 0.00006 * float( el[ 0 ] ) * w
        #elif float(el[0]) < 400000:
        #    nw = w - 0.3 * w - 0.3 * float( el[ 0 ] )  * w / 35000
        #else:
        #    nw = w - 0.6 * w - 0.3 * float(el[0]) * w / 960000
        nh = h - 0.064 * float(el[1]) * h
        nw = (0.96 * el[0] * w) / 100000000 #* el[0]* w
        print(nh, nw)
        canvas.create_line( wa , ha , nw , nh , fill = "green" , width = 5 )
        wa = nw
        ha = nh

def file_gen(var, infile, exec, outfile) :
    mainfile = open("file_name.in", "w")
    mainfile.write(infile + " " + outfile + "\n")
    mainfile.close()
    n = random.randint( 1 , 10 ** 6)
    if var == "mic":
        x = random.randint( 0 , 2 )
    elif var == "mare":
        x = random.randint(3, 7)
    seconds = int(time.time()*1000)
    ifile = open( infile , "w" )
    ifile.write( f"{seconds}\n{n}\n{10 ** max_value[x]}" )
    #for y in range( n ) :
        #fradix.write( str( random.randint( 1 , 10 ** max_value[ x ] ) ) + "\n" )
    ifile.close( )
    # win32api.ShellExecute( 0 , "open" , "radix/radixs.exe" , None , "/" , 0 )
    os.system( exec )
    # subprocess.run("radix/radixs.exe")
    ofile = open( outfile , "r" )
    run_time = ofile.read( )
    if run_time != "alocat" and run_time != "err":
        run_time = str( float( run_time ) * (10 ** (-6)) )
    ofile.close( )
    return (run_time , n , x)

#EXEMPLU APEL
#(timp, numere, maxim) = file_gen("mic", 
#    nume_sortare + tip_sortare + ".in", nume_sortare)
