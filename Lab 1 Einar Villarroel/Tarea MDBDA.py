# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 10:36:04 2019

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
arrayx=[];
arrayotro=[];
segundos=0;
minutos=0;
rango=500;
cont=0;
cont2=0;
for i in range(1,rango):
    #x= time.strftime("%H:%M:%S");
    
    y=random.uniform(2000,4000);
    #arrayx.apprend(x);
    array.append(y);
    #print(str(x)+"\t");
    if(segundos==60):
        segundos=0;
        minutos=minutos+1;
        
    #print(time.strftime("%d/%m/%y") +" 00:"+"0"+str(minutos)+":"+str(segundos));
    x=" 00:"+"0"+str(minutos)+":"+str(segundos);
    #x=time.strftime("%d/%m/%y") +" 00:"+"0"+str(minutos)+":"+str(segundos);
    arrayx.append(x);
    segundos=segundos+1;

#datos=arreglo(rango,2000,4000);    
#repe=agrupar(datos, 3);
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
        #print(cont);
    else:
        cont=0;
        r2y.clear();
        r2x.clear();
        #print(cont);
    if(cont>=9):
        #print(cont);
        cont=0;
        print("9 PUNTOS CONTINUOS DENTRO LA ZONA C-");
        #print("9 PUNTOS CONTINUOS DENTRO LA ZONA C-"+ str(r2x));
        ptl.plot(r2x,r2y, "m.");
        
        
    if(array[j]>=promedio and array[j]<=promedio+desviaciones ):
        r3y.append(array[j]);
        r3x.append(arrayx[j]);
        cont2+=1;
        #print(cont2);
    else:
        cont2=0;
        r3y.clear();
        r3x.clear();
        #print(cont2);
    if(cont2>=9):
        #print(cont2);
        cont2=0;
        print("9 PUNTOS CONTINUOS DENTRO LA ZONA C+");
        #print("9 PUNTOS CONTINUOS DENTRO LA ZONA C+"+ str(r3x));
        ptl.plot(r3x,r3y, "b.");
       
        
        
ptl.plot(r1x,r1y, "g.");
    
ptl.show();