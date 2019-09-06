# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:04:59 2019

@author: Usuario
"""

import random
import matplotlib.pyplot as ptl
import numpy as np
import time

def arreglo(largo,min,max):
    rand=np.random.rand(largo);
    retorno=[];
    for num in rand:
        retorno.append(num*(max-min)+min)
    return retorno;
def agrupar(lista,cantidad):
    textos=[]
    i=0;
    paso = len(lista)/cantidad
    for t in lista:
        i+=1;
        if(i%paso<1):
            textos.append(t)
    return textos;
        

array=[];
r1y=[];
r1x=[];
r2y=[];
r2x=[];
r3y=[];
r3x=[];
r4y=[];
r4x=[];
r5y=[];
r5x=[];
r6y=[];
r6x=[];
arrayx=[];
arrayotro=[];
segundos=0;
minutos=0;
rango=50;
cont=0;
cont2=0;
cont3=0;
cont4=0;
for i in range(1,rango):    
    
    y=random.uniform(2000,4000);  
    array.append(y);   
    if(segundos==60):
        segundos=0;
        minutos=minutos+1;     

    x=" 00:"+"0"+str(minutos)+":"+str(segundos);    
    arrayx.append(x);
    segundos=segundos+1;
    
print(time.strftime("%d/%m/%y"));
promedio=np.sum(array)/len(array);
print("Media: "+str(promedio)+"\t");
desviaciones=np.std(array);
print("Des Estandar: "+str(desviaciones)+"\t");
varianza=(desviaciones*desviaciones);
print("Varianza: "+str(varianza)+"\t");
asd=(agrupar(arrayx, 6))
ptl.plot(arrayx,array, "-y");
ptl.plot(arrayx,array, "r.");
ptl.plot( [0,rango],[promedio,promedio],"g--", label="Media");
ptl.plot( [0,rango],[promedio+desviaciones,promedio+desviaciones],"k--", label="Desviacion Estandar");
ptl.plot( [0,rango],[promedio-desviaciones,promedio-desviaciones],"k--");
ptl.plot( [0,rango],[promedio-(desviaciones * 2),promedio-(desviaciones * 2)],"r--");
ptl.plot( [0,rango],[promedio+(desviaciones * 2),promedio+(desviaciones * 2)],"r--");
ptl.plot( [0,rango],[promedio-(desviaciones * 3),promedio-(desviaciones * 3)],"c--");
ptl.plot( [0,rango],[promedio+(desviaciones * 3),promedio+(desviaciones * 3)],"c--");
ptl.plot( [0,rango],[promedio-(desviaciones * 4),promedio-(desviaciones * 4)],"m--");
ptl.plot( [0,rango],[promedio+(desviaciones * 4),promedio+(desviaciones * 4)],"m--");
ptl.xticks(asd);
ptl.grid();
P1=desviaciones*4;
for j in range(1,rango-1):
    if(array[j]>=promedio+P1 or array[j]<=promedio-P1):
        r1y.append(array[j]);
        r1x.append(arrayx[j]);
        #print(r1y[j]);
        #print(str(r1x));<<
    if(array[j]>=promedio-desviaciones and array[j]<=promedio):
        r2y.append(array[j]);
        r2x.append(arrayx[j]);
        cont+=1;        
        if(cont>=9):
            print(str(cont)+" PUNTOS CONTINUOS DENTRO LA ZONA C-");
            ptl.plot(r2x,r2y, "c.");     
    else:
        cont=0;
        r2y.clear();
        r2x.clear();
    if(array[j]<=promedio+desviaciones and array[j]>=promedio):
        r3y.append(array[j]);
        r3x.append(arrayx[j]);
        cont2+=1;
        if(cont2>=9):
            print(str(cont2)+" PUNTOS CONTINUOS DENTRO LA ZONA C+");
            ptl.plot(r3x,r3y, "b.");
    else:
       cont2=0;
       r3y.clear();
       r3x.clear();
for f in range(1,rango-2):
    if(array[f]<=array[f+1]):        
        r4y.append(array[f]);
        r4x.append(arrayx[f]);
        cont3+=1;
        if(cont3>=6):
             print(str(cont3)+" PUNTOS CONTINUOS ACENDENTES");
             ptl.plot(r4x,r4y, "k.");
    else:
        cont3=0;
        r4y.clear();
        r4x.clear();
        
    if(array[f]>=array[f+1]):
        r5y.append(array[f]);
        r5x.append(arrayx[f]);
        cont4+=1;
        if(cont4>=6):
             print(str(cont4)+" PUNTOS CONTINUOS DECENDENTES");
             ptl.plot(r5x,r5y, "b.");
    else:
        cont4=0;
        r5y.clear();
        r5x.clear();
        

    
       

       
ptl.plot(r1x,r1y, "g.");
    
ptl.show();