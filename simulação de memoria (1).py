#!/usr/bin/env python
# coding: utf-8

# In[10]:


#memoria de 6 bytes
a= "000000"
b= "000000"
c= "000000"
d= "000000"
e= "000000"
f= "000000"
g= "000000"
h= "000000"
temporario=""

while True:
    esc=input("coloque w para escrita, r para leitura, l para listagem de todos os blocos e qualquer letra para interrupção do programa")
    
    #escrita da memória
    if esc.lower() == "w":
        end = print('digite o endereçamento de 3 bits')
        if end == "000":
            temporario= input('coloque o dado de 6 bit')
            if len(temporario)<6 or len(temporario)>6:
                print('ERRO')
            else: 
                a=temporario
            
        elif end == "001":
            temporario= input('coloque o dado de 6 bit')
            if len(temporario)<6 or len(temporario)>6:
                print('ERRO')
            else: 
                b=temporario
                
        elif end == "010":
            temporario= input('coloque o dado de 6 bit')
            if len(temporario)<6 or len(temporario)>6:
                print('ERRO')
            else: 
                c=temporario
                
        elif end == "011":
            temporario= input('coloque o dado de 6 bit')
            if len(temporario)<6 or len(temporario)>6:
                print('ERRO')
            else:
                d=temporario
                
        elif end == "100":
            temporario= input('coloque o dado de 6 bit')
            if len(temporario)<6 or len(temporario)>6:
                print('ERRO')
            else:
                e=temporario
                
                 elif end == "101":
            temporario= input('coloque o dado de 6 bit')
            if len(temporario)<6 or len(temporario)>6:
                print('ERRO')
            else: 
                f=temporario
                
        elif end == "110":
            temporario= input('coloque o dado de 6 bit')
            if len(temporario)<6 or len(temporario)>6:
                print('ERRO')
            else:
                g=temporario
                
        elif end == "111":
            temporario= input('coloque o dado de 6 bit')
            if len(temporario)<6 or len(temporario)>6:
                print('ERRO')
            else: 
                h=temporario
                
#leitura por endereçamento de celula
    elif esc.lower=="r":
        end = input("coloque o endereço de 3 bits: ")
        if end == "000":
            print(a)
        elif end == "001":
            print(b)
        elif end == "010":
            print(c)
        elif end == "011":
            print(d)
        elif end == "100":
            print(e)
        elif end == "101":
            print(f)
        elif end == "110":
            print(g)
        elif end == "111":
            print(h)
#leitura de todas celulas da memoria
    elif esc.lower() == "l":
        print("Toda a lista:")
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print(g)
        print(h)
    else:
        break


# In[ ]:




