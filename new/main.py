import tkinter, win32api, random, os, subprocess, time
from tkinter import *
from win32api import GetSystemMetrics
from datetime import datetime


max_value = [1, 2, 4, 6, 9, 12, 15, 18]
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

def window_exit():
    root.destroy()

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

def radix_afis_mic_main():
    radix_mic = Tk()
    radix_mic.title("Radix nr mici")
    radix_mic.configure( bg="#C0C0C0" )
    radix_mic.geometry(f"{width}x{height}")
    radix_mic_gf = Frame( radix_mic )
    radix_mic_gf.pack( )
    radix_mic_canvas = tkinter.Canvas( radix_mic_gf , bg="#A9A9A9" , width=0.8 * width , height=0.8 * height )
    canvw = 0.8 * width
    canvh = 0.8 * height
    table = [ ]
    radix_mic_canvas.create_line( 0.02 * canvw , 0.98 * canvh , 0.9 * canvw , 0.1 * canvh , fill="green" , width=5 )
    radix_mic_canvas.pack( )
    def radixafis_mic() :
        (radix_time , n , x) = file_gen("mic", "rsmic.in", "radixs.exe", "rsmic.out")
        debug_file = open( "random_tests.txt" , "a" )
        debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {radix_time}\n\n" )
        debug_file.close( )
        radix_mic_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {radix_time}" )
        table.append((n, radix_time))
        redraw_graph(table, radix_mic_canvas, canvw, canvh)
        radix_mic_label.after( 100 , radixafis_mic )

    radix_mic_label = tkinter.Label( radix_mic , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    radexit = Button( radix_mic , text="exit" , command=radix_mic.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    radexit.place( x=width - 0.07 * width , y=0.05 * height )
    radix_mic_label.pack()
    radixafis_mic()
    radix_mic.mainloop()

def radix_afis_mare_main():
    radix_mare = Tk()
    radix_mare.title("Radix nr mari")
    radix_mare.configure( bg="#C0C0C0" )
    radix_mare.geometry( f"{width}x{height}" )
    radix_mare_gf = Frame( radix_mare )
    radix_mare_gf.pack( )
    radix_mare_canvas = tkinter.Canvas( radix_mare_gf , bg="#A9A9A9" , width = 0.8 * width, height = 0.8 * height)
    canvw = 0.8 * width
    canvh = 0.8 * height
    table = []
    radix_mare_canvas.create_line( 0.02 * canvw , 0.98 * canvh , 0.9 * canvw , 0.1 * canvh , fill = "green" , width = 5 )
    radix_mare_canvas.pack( )
    def radixafis_mare() :
        (radix_time , n , x) = file_gen( "mare", "rsmare.in", "radixs.exe", "rsmare.out" )
        debug_file = open( "random_tests.txt" , "a" )
        debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {radix_time}\n\n" )
        debug_file.close( )
        radix_mare_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {radix_time}" )
        table.append((n, radix_time))
        redraw_graph(table, radix_mare_canvas, canvw, canvh)
        radix_mare_label.after( 100 , radixafis_mare)

    radix_mare_label = tkinter.Label( radix_mare , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    radix_mare_label.pack( )
    radexit = Button( radix_mare , text="exit" , command=radix_mare.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    radexit.place(x=width - 0.07 * width , y=0.05 * height )
    radixafis_mare()
    radix_mare.mainloop( )

def radixS():
    img_radix = Tk()
    img_radix.title("Radix")
    img_radix.configure( bg="#C0C0C0" )
    img_radix.geometry(f"{width}x{height}")
    btn_radix_mic = Button(img_radix, text = "Numere mici (<= 10^4)", command = radix_afis_mic_main,
                           font = ("Arial", int(0.012 * width)))
    btn_radix_mic.place(x = 0.2 * width, y = 0.3 * height)
    btn_radix_mare = Button(img_radix, text = "Numere mari (>=10^4 si <=10^18)", command = radix_afis_mare_main,
                            font = ("Arial", int(0.012 * width)))
    btn_radix_mare.place(x = 0.4 * width, y = 0.3 * height)
    #def radixafis_mic() :
        #(radix_time , n , x) = radix_gen("mic")
        #debug_file = open( "random_tests.txt" , "a" )
        #debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {radix_time}\n\n" )
        #debug_file.close( )
        #radix_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {radix_time}" )
        #radix_label.after( 100 , radixafis_mic() )
    #def radixafis() :
     #   (radix_time , n , x) = radix_gen( )
      #  debug_file = open( "random_tests.txt" , "a" )
       # debug_file.write(f"\n{datetime.now()}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {radix_time}\n\n")
       # debug_file.close()
       # radix_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {radix_time}" )
       # radix_label.after( 100 , radixafis)

    #radix_label = tkinter.Label( img_radix , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    radexit = Button( img_radix , text="exit" , command=img_radix.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    radexit.place( x=width - 0.07 * width , y=0.05 * height )
    #radix_label.pack( )
    #radixafis()
    img_radix.mainloop()

def merge_afis_mic_main():
    merge_mic = Tk()
    merge_mic.title("Merge nr mici")
    merge_mic.configure( bg="#C0C0C0" )
    merge_mic.geometry(f"{width}x{height}")
    merge_mic_gf = Frame( merge_mic )
    merge_mic_gf.pack( )
    merge_mic_canvas = tkinter.Canvas( merge_mic_gf , bg="#A9A9A9" , width=0.8 * width , height=0.8 * height )
    canvw = 0.8 * width
    canvh = 0.8 * height
    table = [ ]
    merge_mic_canvas.create_line( 0.02 * canvw , 0.98 * canvh , 0.9 * canvw , 0.1 * canvh , fill="green" , width=5 )
    merge_mic_canvas.pack( )
    def mergeafis_mic() :
        (merge_time , n , x) = file_gen("mic", "mergmic.in", "merges.exe", "mergmic.out")
        debug_file = open( "random_tests.txt" , "a" )
        debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {merge_time}\n\n" )
        debug_file.close( )
        merge_mic_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {merge_time}" )
        table.append((n, merge_time))
        redraw_graph(table, merge_mic_canvas, canvw, canvh)
        merge_mic_label.after( 100 , mergeafis_mic )

    merge_mic_label = tkinter.Label( merge_mic , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    mergexit = Button( merge_mic , text="exit" , command=merge_mic.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    mergexit.place( x=width - 0.07 * width , y=0.05 * height )
    merge_mic_label.pack()
    mergeafis_mic()
    merge_mic.mainloop()

def merge_afis_mare_main():
    merge_mare = Tk()
    merge_mare.title("Merge nr mari")
    merge_mare.configure( bg="#C0C0C0" )
    merge_mare.geometry( f"{width}x{height}" )
    merge_mare_gf = Frame( merge_mare )
    merge_mare_gf.pack( )
    merge_mare_canvas = tkinter.Canvas( merge_mare_gf , bg="#A9A9A9" , width = 0.8 * width, height = 0.8 * height)
    canvw = 0.8 * width
    canvh = 0.8 * height
    table = []
    merge_mare_canvas.create_line( 0.02 * canvw , 0.98 * canvh , 0.9 * canvw , 0.1 * canvh , fill = "green" , width = 5 )
    merge_mare_canvas.pack( )
    def mergeafis_mare() :
        (merge_time , n , x) = file_gen( "mare", "rsmare.in", "merges.exe", "rsmare.out" )
        debug_file = open( "random_tests.txt" , "a" )
        debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {merge_time}\n\n" )
        debug_file.close( )
        merge_mare_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {merge_time}" )
        table.append((n, merge_time))
        redraw_graph(table, merge_mare_canvas, canvw, canvh)
        merge_mare_label.after( 100 , mergeafis_mare)

    merge_mare_label = tkinter.Label( merge_mare , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    merge_mare_label.pack( )
    mergexit = Button( merge_mare , text="exit" , command=merge_mare.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    mergexit.place(x=width - 0.07 * width , y=0.05 * height )
    mergeafis_mare()
    merge_mare.mainloop( )

def mergeS():
    img_merge = Tk()
    img_merge.title("Merge")
    img_merge.configure( bg="#C0C0C0" )
    img_merge.geometry(f"{width}x{height}")
    btn_merge_mic = Button(img_merge, text = "Numere mici (<= 10^4)", command = merge_afis_mic_main,
                           font = ("Arial", int(0.012 * width)))
    btn_merge_mic.place(x = 0.2 * width, y = 0.3 * height)
    btn_merge_mare = Button(img_merge, text = "Numere mari (>=10^4 si <=10^18)", command = merge_afis_mare_main,
                            font = ("Arial", int(0.012 * width)))
    btn_merge_mare.place(x = 0.4 * width, y = 0.3 * height)
    #def mergeafis_mic() :
        #(merge_time , n , x) = merge_gen("mic")
        #debug_file = open( "random_tests.txt" , "a" )
        #debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {merge_time}\n\n" )
        #debug_file.close( )
        #merge_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {merge_time}" )
        #merge_label.after( 100 , mergeafis_mic() )
    #def mergeafis() :
     #   (merge_time , n , x) = merge_gen( )
      #  debug_file = open( "random_tests.txt" , "a" )
       # debug_file.write(f"\n{datetime.now()}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {merge_time}\n\n")
       # debug_file.close()
       # merge_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {merge_time}" )
       # merge_label.after( 100 , mergeafis)

    #merge_label = tkinter.Label( img_merge , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    mergexit = Button( img_merge , text="exit" , command=img_merge.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    mergexit.place( x=width - 0.07 * width , y=0.05 * height )
    #merge_label.pack( )
    #mergeafis()
    img_merge.mainloop()

def shell_afis_mic_main():
    shell_mic = Tk()
    shell_mic.title("shell nr mici")
    shell_mic.configure( bg="#C0C0C0" )
    shell_mic.geometry(f"{width}x{height}")
    shell_mic_gf = Frame( shell_mic )
    shell_mic_gf.pack( )
    shell_mic_canvas = tkinter.Canvas( shell_mic_gf , bg="#A9A9A9" , width=0.8 * width , height=0.8 * height )
    canvw = 0.8 * width
    canvh = 0.8 * height
    table = [ ]
    shell_mic_canvas.create_line( 0.02 * canvw , 0.98 * canvh , 0.9 * canvw , 0.1 * canvh , fill="green" , width=5 )
    shell_mic_canvas.pack( )
    def shellafis_mic() :
        (shell_time , n , x) = file_gen("mic", "shellmic.in", "shells.exe", "shellmic.out")
        debug_file = open( "random_tests.txt" , "a" )
        debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {shell_time}\n\n" )
        debug_file.close( )
        shell_mic_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {shell_time}" )
        table.append((n, shell_time))
        redraw_graph(table, shell_mic_canvas, canvw, canvh)
        shell_mic_label.after( 100 , shellafis_mic )

    shell_mic_label = tkinter.Label( shell_mic , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    shellexit = Button( shell_mic , text="exit" , command=shell_mic.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    shellexit.place( x=width - 0.07 * width , y=0.05 * height )
    shell_mic_label.pack()
    shellafis_mic()
    shell_mic.mainloop()

def shell_afis_mare_main():
    shell_mare = Tk()
    shell_mare.title("shell nr mari")
    shell_mare.configure( bg="#C0C0C0" )
    shell_mare.geometry( f"{width}x{height}" )
    shell_mare_gf = Frame( shell_mare )
    shell_mare_gf.pack( )
    shell_mare_canvas = tkinter.Canvas( shell_mare_gf , bg="#A9A9A9" , width = 0.8 * width, height = 0.8 * height)
    canvw = 0.8 * width
    canvh = 0.8 * height
    table = []
    shell_mare_canvas.create_line( 0.02 * canvw , 0.98 * canvh , 0.9 * canvw , 0.1 * canvh , fill = "green" , width = 5 )
    shell_mare_canvas.pack( )
    def shellafis_mare() :
        (shell_time , n , x) = file_gen( "mare", "shellmare.in", "shells.exe", "shellmare.out" )
        debug_file = open( "random_tests.txt" , "a" )
        debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {shell_time}\n\n" )
        debug_file.close( )
        shell_mare_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {shell_time}" )
        table.append((n, shell_time))
        redraw_graph(table, shell_mare_canvas, canvw, canvh)
        shell_mare_label.after( 100 , shellafis_mare)

    shell_mare_label = tkinter.Label( shell_mare , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    shell_mare_label.pack( )
    shellexit = Button( shell_mare , text="exit" , command=shell_mare.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    shellexit.place(x=width - 0.07 * width , y=0.05 * height )
    shellafis_mare()
    shell_mare.mainloop( )

def shellS():
    img_shell = Tk()
    img_shell.title("shell")
    img_shell.configure( bg="#C0C0C0" )
    img_shell.geometry(f"{width}x{height}")
    btn_shell_mic = Button(img_shell, text = "Numere mici (<= 10^4)", command = shell_afis_mic_main,
                           font = ("Arial", int(0.012 * width)))
    btn_shell_mic.place(x = 0.2 * width, y = 0.3 * height)
    btn_shell_mare = Button(img_shell, text = "Numere mari (>=10^4 si <=10^18)", command = shell_afis_mare_main,
                            font = ("Arial", int(0.012 * width)))
    btn_shell_mare.place(x = 0.4 * width, y = 0.3 * height)
    #def shellafis_mic() :
        #(shell_time , n , x) = shell_gen("mic")
        #debug_file = open( "random_tests.txt" , "a" )
        #debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {shell_time}\n\n" )
        #debug_file.close( )
        #shell_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {shell_time}" )
        #shell_label.after( 100 , shellafis_mic() )
    #def shellafis() :
     #   (shell_time , n , x) = shell_gen( )
      #  debug_file = open( "random_tests.txt" , "a" )
       # debug_file.write(f"\n{datetime.now()}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {shell_time}\n\n")
       # debug_file.close()
       # shell_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {shell_time}" )
       # shell_label.after( 100 , shellafis)

    #shell_label = tkinter.Label( img_shell , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    shellexit = Button( img_shell , text="exit" , command=img_shell.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    shellexit.place( x=width - 0.07 * width , y=0.05 * height )
    #shell_label.pack( )
    #shellafis()
    img_shell.mainloop()
def quick_afis_mic_main():
    quick_mic = Tk()
    quick_mic.title("quick nr mici")
    quick_mic.configure( bg="#C0C0C0" )
    quick_mic.geometry(f"{width}x{height}")
    quick_mic_gf = Frame( quick_mic )
    quick_mic_gf.pack( )
    quick_mic_canvas = tkinter.Canvas( quick_mic_gf , bg="#A9A9A9" , width=0.8 * width , height=0.8 * height )
    canvw = 0.8 * width
    canvh = 0.8 * height
    table = [ ]
    quick_mic_canvas.create_line( 0.02 * canvw , 0.98 * canvh , 0.9 * canvw , 0.1 * canvh , fill="green" , width=5 )
    quick_mic_canvas.pack( )
    def quickafis_mic() :
        (quick_time , n , x) = file_gen("mic", "quickmic.in", "quicks.exe", "quickmic.out")
        debug_file = open( "random_tests.txt" , "a" )
        debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {quick_time}\n\n" )
        debug_file.close( )
        quick_mic_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {quick_time}" )
        table.append((n, quick_time))
        redraw_graph(table, quick_mic_canvas, canvw, canvh)
        quick_mic_label.after( 100 , quickafis_mic )

    quick_mic_label = tkinter.Label( quick_mic , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    quickexit = Button( quick_mic , text="exit" , command=quick_mic.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    quickexit.place( x=width - 0.07 * width , y=0.05 * height )
    quick_mic_label.pack()
    quickafis_mic()
    quick_mic.mainloop()

def quick_afis_mare_main():
    quick_mare = Tk()
    quick_mare.title("quick nr mari")
    quick_mare.configure( bg="#C0C0C0" )
    quick_mare.geometry( f"{width}x{height}" )
    quick_mare_gf = Frame( quick_mare )
    quick_mare_gf.pack( )
    quick_mare_canvas = tkinter.Canvas( quick_mare_gf , bg="#A9A9A9" , width = 0.8 * width, height = 0.8 * height)
    canvw = 0.8 * width
    canvh = 0.8 * height
    table = []
    quick_mare_canvas.create_line( 0.02 * canvw , 0.98 * canvh , 0.9 * canvw , 0.1 * canvh , fill = "green" , width = 5 )
    quick_mare_canvas.pack( )
    def quickafis_mare() :
        (quick_time , n , x) = file_gen( "mare", "quickmare.in", "quicks.exe", "quickmare.out" )
        debug_file = open( "random_tests.txt" , "a" )
        debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {quick_time}\n\n" )
        debug_file.close( )
        quick_mare_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {quick_time}" )
        table.append((n, quick_time))
        redraw_graph(table, quick_mare_canvas, canvw, canvh)
        quick_mare_label.after( 100 , quickafis_mare)

    quick_mare_label = tkinter.Label( quick_mare , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    quick_mare_label.pack( )
    quickexit = Button( quick_mare , text="exit" , command=quick_mare.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    quickexit.place(x=width - 0.07 * width , y=0.05 * height )
    quickafis_mare()
    quick_mare.mainloop( )

def quickS():
    img_quick = Tk()
    img_quick.title("quick")
    img_quick.configure( bg="#C0C0C0" )
    img_quick.geometry(f"{width}x{height}")
    btn_quick_mic = Button(img_quick, text = "Numere mici (<= 10^4)", command = quick_afis_mic_main,
                           font = ("Arial", int(0.012 * width)))
    btn_quick_mic.place(x = 0.2 * width, y = 0.3 * height)
    btn_quick_mare = Button(img_quick, text = "Numere mari (>=10^4 si <=10^18)", command = quick_afis_mare_main,
                            font = ("Arial", int(0.012 * width)))
    btn_quick_mare.place(x = 0.4 * width, y = 0.3 * height)
    #def quickafis_mic() :
        #(quick_time , n , x) = quick_gen("mic")
        #debug_file = open( "random_tests.txt" , "a" )
        #debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {quick_time}\n\n" )
        #debug_file.close( )
        #quick_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {quick_time}" )
        #quick_label.after( 100 , quickafis_mic() )
    #def quickafis() :
     #   (quick_time , n , x) = quick_gen( )
      #  debug_file = open( "random_tests.txt" , "a" )
       # debug_file.write(f"\n{datetime.now()}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {quick_time}\n\n")
       # debug_file.close()
       # quick_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {quick_time}" )
       # quick_label.after( 100 , quickafis)

    #quick_label = tkinter.Label( img_quick , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    quickexit = Button( img_quick , text="exit" , command=img_quick.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    quickexit.place( x=width - 0.07 * width , y=0.05 * height )
    #quick_label.pack( )
    #quickafis()
    img_quick.mainloop()
def count_afis_mic_main():
    count_mic = Tk()
    count_mic.title("count nr mici")
    count_mic.configure( bg="#C0C0C0" )
    count_mic.geometry(f"{width}x{height}")
    count_mic_gf = Frame( count_mic )
    count_mic_gf.pack( )
    count_mic_canvas = tkinter.Canvas( count_mic_gf , bg="#A9A9A9" , width=0.8 * width , height=0.8 * height )
    canvw = 0.8 * width
    canvh = 0.8 * height
    table = [ ]
    count_mic_canvas.create_line( 0.02 * canvw , 0.98 * canvh , 0.9 * canvw , 0.1 * canvh , fill="green" , width=5 )
    count_mic_canvas.pack( )
    def countafis_mic() :
        (count_time , n , x) = file_gen("mic", "countmic.in", "counts.exe", "countmic.out")
        debug_file = open( "random_tests.txt" , "a" )
        debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {count_time}\n\n" )
        debug_file.close( )
        count_mic_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {count_time}" )
        table.append((n, count_time))
        redraw_graph(table, count_mic_canvas, canvw, canvh)
        count_mic_label.after( 100 , countafis_mic )

    count_mic_label = tkinter.Label( count_mic , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    countexit = Button( count_mic , text="exit" , command=count_mic.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    countexit.place( x=width - 0.07 * width , y=0.05 * height )
    count_mic_label.pack()
    countafis_mic()
    count_mic.mainloop()

def count_afis_mare_main():
    count_mare = Tk()
    count_mare.title("count nr mari")
    count_mare.configure( bg="#C0C0C0" )
    count_mare.geometry( f"{width}x{height}" )
    warning_text = tkinter.Label(count_mare,  text = "\n\nSTD:: Bad alloc() - Counting sort nu functioneaza pe numere mai mari de 10^ 8 \n" +
                                        "Explicatia este faptul ca 10^9 elemente de tipul unsigned long long ocupa peste " +
                                        "7 gb ram", font=("Arial" , int( 0.015 * width )))
    warning_text.pack()
    countexit = Button( count_mare , text="exit" , command=count_mare.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    countexit.place(x=width - 0.07 * width , y=0.05 * height )
    count_mare.mainloop( )

def countS():
    img_count = Tk()
    img_count.title("count")
    img_count.configure( bg="#C0C0C0" )
    img_count.geometry(f"{width}x{height}")
    btn_count_mic = Button(img_count, text = "Numere mici (<= 10^4)", command = count_afis_mic_main,
                           font = ("Arial", int(0.012 * width)))
    btn_count_mic.place(x = 0.2 * width, y = 0.3 * height)
    btn_count_mare = Button(img_count, text = "Numere mari (>=10^4 si <=10^18)", command = count_afis_mare_main,
                            font = ("Arial", int(0.012 * width)))
    btn_count_mare.place(x = 0.4 * width, y = 0.3 * height)
    countexit = Button( img_count , text="exit" , command=img_count.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    countexit.place( x=width - 0.07 * width , y=0.05 * height )
    img_count.mainloop()
def bubble_afis_mic_main():
    bubble_mic = Tk()
    bubble_mic.title("bubble nr mici")
    bubble_mic.configure( bg="#C0C0C0" )
    bubble_mic.geometry(f"{width}x{height}")
    bubble_mic_gf = Frame( bubble_mic )
    bubble_mic_gf.pack( )
    bubble_mic_canvas = tkinter.Canvas( bubble_mic_gf , bg="#A9A9A9" , width=0.8 * width , height=0.8 * height )
    canvw = 0.8 * width
    canvh = 0.8 * height
    table = [ ]
    bubble_mic_canvas.create_line( 0.02 * canvw , 0.98 * canvh , 0.9 * canvw , 0.1 * canvh , fill="green" , width=5 )
    bubble_mic_canvas.pack( )
    def bubbleafis_mic() :
        (bubble_time , n , x) = file_gen("mic", "bubblemic.in", "bubbles.exe", "bubblemic.out")
        debug_file = open( "random_tests.txt" , "a" )
        debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {bubble_time}\n\n" )
        debug_file.close( )
        bubble_mic_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {bubble_time}" )
        table.append((n, bubble_time))
        redraw_graph(table, bubble_mic_canvas, canvw, canvh)
        bubble_mic_label.after( 100 , bubbleafis_mic )

    bubble_mic_label = tkinter.Label( bubble_mic , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    bubbleexit = Button( bubble_mic , text="exit" , command=bubble_mic.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    bubbleexit.place( x=width - 0.07 * width , y=0.05 * height )
    bubble_mic_label.pack()
    bubbleafis_mic()
    bubble_mic.mainloop()

def bubble_afis_mare_main():
    bubble_mare = Tk()
    bubble_mare.title("bubble nr mari")
    bubble_mare.configure( bg="#C0C0C0" )
    bubble_mare.geometry( f"{width}x{height}" )
    bubble_mare_gf = Frame( bubble_mare )
    bubble_mare_gf.pack( )
    bubble_mare_canvas = tkinter.Canvas( bubble_mare_gf , bg="#A9A9A9" , width = 0.8 * width, height = 0.8 * height)
    canvw = 0.8 * width
    canvh = 0.8 * height
    table = []
    bubble_mare_canvas.create_line( 0.02 * canvw , 0.98 * canvh , 0.9 * canvw , 0.1 * canvh , fill = "green" , width = 5 )
    bubble_mare_canvas.pack( )
    def bubbleafis_mare() :
        (bubble_time , n , x) = file_gen( "mare", "bubblemare.in", "bubbles.exe", "bubblemare.out" )
        debug_file = open( "random_tests.txt" , "a" )
        debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {bubble_time}\n\n" )
        debug_file.close( )
        bubble_mare_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {bubble_time}" )
        table.append((n, bubble_time))
        redraw_graph(table, bubble_mare_canvas, canvw, canvh)
        bubble_mare_label.after( 100 , bubbleafis_mare)

    bubble_mare_label = tkinter.Label( bubble_mare , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    bubble_mare_label.pack( )
    bubbleexit = Button( bubble_mare , text="exit" , command=bubble_mare.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    bubbleexit.place(x=width - 0.07 * width , y=0.05 * height )
    bubbleafis_mare()
    bubble_mare.mainloop( )

def bubbleS():
    img_bubble = Tk()
    img_bubble.title("bubble")
    img_bubble.configure( bg="#C0C0C0" )
    img_bubble.geometry(f"{width}x{height}")
    btn_bubble_mic = Button(img_bubble, text = "Numere mici (<= 10^4)", command = bubble_afis_mic_main,
                           font = ("Arial", int(0.012 * width)))
    btn_bubble_mic.place(x = 0.2 * width, y = 0.3 * height)
    btn_bubble_mare = Button(img_bubble, text = "Numere mari (>=10^4 si <=10^18)", command = bubble_afis_mare_main,
                            font = ("Arial", int(0.012 * width)))
    btn_bubble_mare.place(x = 0.4 * width, y = 0.3 * height)
    #def bubbleafis_mic() :
        #(bubble_time , n , x) = bubble_gen("mic")
        #debug_file = open( "random_tests.txt" , "a" )
        #debug_file.write( f"\n{datetime.now( )}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {bubble_time}\n\n" )
        #debug_file.close( )
        #bubble_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {bubble_time}" )
        #bubble_label.after( 100 , bubbleafis_mic() )
    #def bubbleafis() :
     #   (bubble_time , n , x) = bubble_gen( )
      #  debug_file = open( "random_tests.txt" , "a" )
       # debug_file.write(f"\n{datetime.now()}\nNumere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {bubble_time}\n\n")
       # debug_file.close()
       # bubble_label.config( text=f"Numere: {n} de {int( max_value[ x ] )} cifre\nTimp in secunde: {bubble_time}" )
       # bubble_label.after( 100 , bubbleafis)

    #bubble_label = tkinter.Label( img_bubble , font=("Arial" , int( 0.02 * width )) , background="#C0C0C0" )
    bubbleexit = Button( img_bubble , text="exit" , command=img_bubble.destroy , width=int( 0.005 * width ) , height=int( 0.003 * height ) ,
                      background="#CD5C5C" , font=("Arial" , int( 0.01 * width )) )
    bubbleexit.place( x=width - 0.07 * width , y=0.05 * height )
    #bubble_label.pack( )
    #bubbleafis()
    img_bubble.mainloop()

root = Tk()
root.title("Sortari")
root.configure(bg="#C0C0C0")
random.seed()
root.geometry( f"{width}x{height}")
name = tkinter.Label(text="Sortari", font = ("Arial", int(0.02*width)), background="#C0C0C0", height = 2)
name.pack()
exit = Button( root , text = "exit", command = window_exit, width = int(0.005 * width), height = int(0.003 * height),
               background = "#CD5C5C", font = ("Arial", int(0.01*width)))
exit.place( x = width - 0.07 * width, y = 0.05 * height)
btn_radix = Button( root , text="Radix Sort" , command = radixS , font = ("Arial", int(0.012 * width)))
btn_radix.place( x = 0.05 * width , y = 0.2 * height )
btn_merge = Button( root , text="Merge Sort" , command = mergeS , font = ("Arial", int(0.012 * width)))
btn_merge.place( x = 0.20 * width , y = 0.2 * height )
btn_shell = Button( root , text="Shell Sort" , command = shellS , font = ("Arial", int(0.012 * width)))
btn_shell.place( x = 0.35 * width , y = 0.2 * height )
btn_quick = Button( root , text="Quick Sort" , command = quickS , font = ("Arial", int(0.012 * width)))
btn_quick.place( x = 0.5 * width , y = 0.2 * height )
btn_counting = Button( root , text="Counting Sort" , command = countS , font = ("Arial", int(0.012 * width)))
btn_counting.place( x = 0.65 * width , y = 0.2 * height )
btn_bubble = Button( root , text="Bubble Sort" , command = bubbleS , font = ("Arial", int(0.012 * width)))
btn_bubble.place( x = 0.8 * width , y = 0.2 * height )
root.mainloop( )
