import numpy
import socket
import os



L = []
pos_worker1 = 0
pos_worker2 = 0
pos_worker3 = 0
pos_worker4 = 0


flag_1 = 0
flag_2 = 0
flag_3 = 0
flag_4 = 0
flag_5 = 0
flag_6 = 0
flag_8 = 0
flag_7 = 0

def chief(a,b,c,d):
    
    global flag_1
    global flag_2
    global flag_3
    global flag_4
    global flag_5
    global flag_6
    global flag_7
    global flag_8

    i=[['S',' ',' ',' ',' '],['.',' ',' ',' ',' '],['#',' ',' ',' ',' '],['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['#',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '], 
       ['.',' ',' ',' ',' '],['.',' ',' ',' ',' '],['.',' ',' ',' ',' '],['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['#',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '], 
       ['#',' ',' ',' ',' '],['.',' ',' ',' ',' '],['.',' ',' ',' ',' '],['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['#',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '], 
       ['.',' ',' ',' ',' '],['.',' ',' ',' ',' '],['.',' ',' ',' ',' '],['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '], 
       ['.',' ',' ',' ',' '],['.',' ',' ',' ',' '],['.',' ',' ',' ',' '],['.',' ',' ',' ',' '] , ['#',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '], 
       ['.',' ',' ',' ',' '],['.',' ',' ',' ',' '],['#',' ',' ',' ',' '],['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['#',' ',' ',' ',' '], 
       ['.',' ',' ',' ',' '],['.',' ',' ',' ',' '],['.',' ',' ',' ',' '],['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '], 
       ['.',' ',' ',' ',' '],['#',' ',' ',' ',' '],['.',' ',' ',' ',' '],['.',' ',' ',' ',' '] , ['#',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '], 
       ['.',' ',' ',' ',' '],['#',' ',' ',' ',' '],['.',' ',' ',' ',' '],['#',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['#',' ',' ',' ',' '], 
       ['#',' ',' ',' ',' '],['.',' ',' ',' ',' '],['.',' ',' ',' ',' '],['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['.',' ',' ',' ',' '] , ['E',' ',' ',' ',' ']]
    

    global pos_worker1
    global pos_worker2
    global pos_worker3
    global pos_worker4
    pos_worker1 += a
    pos_worker2 += b
    pos_worker3 += c
    pos_worker4 += d
    if(pos_worker1 < 99):
        while(pos_worker1!=0):
            if i[pos_worker1][0] == '#':
                pos_worker1 = pos_worker1-8
                if pos_worker1 < 0:
                    pos_worker1 = 0
            else:
                break
    if(pos_worker2 < 99):
        while(pos_worker2!=0):
            if i[pos_worker2][0] == '#':
                pos_worker2 = pos_worker2-8
                if pos_worker2 < 0:
                    pos_worker2 = 0
            else:
                break
    if(pos_worker3 < 99):
        while(pos_worker3!=0):
            if i[pos_worker3][0] == '#':
                pos_worker3 = pos_worker3-8
                if pos_worker3 < 0:
                    pos_worker3 = 0
            else:
                break
    if(pos_worker4 < 99):
        while(pos_worker4!=0):
            if i[pos_worker4][0] == '#':
                pos_worker4 = pos_worker4-8
                if pos_worker4 < 0:
                    pos_worker4 = 0
            else:
                break

    if(0<pos_worker1 < 99):
        for k in range(4):
            if i[pos_worker1][k] == '.':
                i[pos_worker1][k] = 'A'
                break
            if i[pos_worker1][k] == ' ':
                i[pos_worker1][k] = 'A'
                break
    if(0<pos_worker2 < 99):
        for k in range(4):
            if i[pos_worker2][k] == '.':
                i[pos_worker2][k] = 'B'
                break
            if i[pos_worker2][k] == ' ':
                i[pos_worker2][k] = 'B'
                break
    if(0<pos_worker3 < 99):
        for k in range(4):
            if i[pos_worker3][k] == '.':
                i[pos_worker3][k] = 'C'
                break
            if i[pos_worker3][k] == ' ':
                i[pos_worker3][k] = 'C'
                break
    if(0<pos_worker4 < 99):
        for k in range(4):
            if i[pos_worker4][k] == '.':
                i[pos_worker4][k] = 'D'
                break
            if i[pos_worker4][k] == ' ':
                i[pos_worker4][k] = 'D'
                break
    
    for n in range(10):
        for y in range(10):
            for h in range(5):
                if(n%2 != 0):
                    print(i[(9-n)*10+y][h], end='')
                else:
                    print(i[(9-n)*10+9-y][h], end='')
        print('\n')
    print('..............')

    if(pos_worker1 >= 99):
        if(flag_1 == 0):
            L.append(1)
            flag_1 = 1
            flag_5 = 1
    if(pos_worker2 >= 99):
        if(flag_2 == 0):
            L.append(2)
            flag_2 = 1
            flag_6 = 1
    if(pos_worker3 >= 99):
        if(flag_3 == 0):
            L.append(3)
            flag_3 = 1
            flag_7 = 1
    if(pos_worker4 >= 99):
        if(flag_4 == 0):
            L.append(4)
            flag_4 = 1
            flag_8 = 1
    
    if (flag_5==1):
        flag_5=2
        os.system('start cmd /k echo player one escaped')
    if (flag_6==1):
        flag_6=2
        os.system('start cmd /k echo player two escaped')
    if (flag_7==1):
        flag_7=2
        os.system('start cmd /k echo player three escaped')
    if (flag_8==1):
        flag_8=2
        os.system('start cmd /k echo player four escaped')



while(pos_worker1<99 or pos_worker2<99 or pos_worker3<99 or pos_worker4<99):  
    st = [0,0,0,0]
    for i in range(4):
        s = socket.socket()         
        host = socket.gethostname() 
        port = 1245                
        s.bind((host, port))        

        s.listen(1)                 

        c, addr = s.accept()     
        st[i] = c.recv(1024)
        st[i] = st[i].decode("utf-8")
        st[i] = (int)(st[i])
        c.send('0'.encode("utf-8"))
        s.close()
    chief(st[0],st[1],st[2],st[3])
s = socket.socket()         
host = socket.gethostname() 
port = 1245                
s.bind((host, port))        
s.listen(1)                 
c, addr = s.accept() 
c.send('1'.encode("utf-8"))
s.close()

print('They escaped in order ',end='')
for i in range(4):
    if i >0:
        print(',', end='')
    print(L[i], end='')
