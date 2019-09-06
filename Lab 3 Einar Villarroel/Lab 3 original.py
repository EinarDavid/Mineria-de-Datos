# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:30:32 2019

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
r7y=[];
r7x=[];
r8y=[];
r8x=[];
arrayx=[];
arrayotro=[];
segundos=0;
minutos=0;
rango=500;
cont=0;
cont2=0;
cont3=0;
cont4=0;
cont5=0;
cont6=0;
cont7=0;
cont8=0;
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
P2=desviaciones*3;

for f in range(1,rango-1):
    if(array[j]>=promedio+P2):        
        r4y.append(array[f]);
        r4x.append(arrayx[f]);
        cont3+=1;
        if(cont3>=3):
             print(str(cont3)+" PATRON 5 DETECTADO EN EL AREA A+");
             ptl.plot(r4x,r4y, "c.");
             ptl.plot(r4x,r4y, "-c");
    else:
        cont3=0;
        r4y.clear();
        r4x.clear();
    if( array[j]<=promedio-P2):
        r5y.append(array[f]);
        r5x.append(arrayx[f]);
        cont4+=1;
        if(cont4>=3):
             print(str(cont4)+" PATRON 5 DETECTADO EN EL AREA A-");
             ptl.plot(r5x,r5y, "c.");
             ptl.plot(r5x,r5y, "-c");
    else:
        cont4=0;
        r5y.clear();
        r5x.clear();
for g in range(1,rango-1):
    if(array[g]>=promedio+desviaciones):        
        r6y.append(array[g]);
        r6x.append(arrayx[g]);
        cont5+=1;
        if(cont5>=5):
             print(str(cont5)+" PATRON 6 DETECTADO EN EL AREA B+");
             ptl.plot(r6x,r6y, "k.");
             ptl.plot(r6x,r6y, "-k");
    else:
        cont5=0;
        r6y.clear();
        r6x.clear();
    if(array[g]<=promedio-desviaciones):
        r7y.append(array[g]);
        r7x.append(arrayx[g]);
        cont6+=1;
        if(cont6>=5):
             print(str(cont6)+" PATRON 6 DETECTADO EN EL AREA B-");
             ptl.plot(r7x,r7y, "k.");
             ptl.plot(r7x,r7y, "-k");
    else:
        cont6=0;
        r7y.clear();
        r7x.clear();  
        
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
        if(cont>=15):
            print(str(cont)+"  PATRON DETECTADO Nº7 DENTRO LA ZONA C-");
            ptl.plot(r2x,r2y, "b.");
            ptl.plot(r2x,r2y, "-b");
           
    else:
        cont=0;
        r2y.clear();
        r2x.clear();
    
    if(array[j]<=promedio+desviaciones and array[j]>=promedio):
        r3y.append(array[j]);
        r3x.append(arrayx[j]);
        cont2+=1;
        if(cont2>=15):
            print(str(cont2)+"  PATRON DETECTADO Nº7 DENTRO LA ZONA C+");
            ptl.plot(r3x,r3y, "b.");
            ptl.plot(r3x,r3y, "-b");
    else:
       cont2=0;
       r3y.clear();
       r3x.clear();        
for H in range(1,rango-1):
    if(array[H]>=promedio+desviaciones or array[H]<=promedio-desviaciones):        
        r8y.append(array[H]);
        r8x.append(arrayx[H]);
        cont7+=1;
        if(cont7>=8):
             print(str(cont7)+" PATRON 8 DETECTADO ");
             ptl.plot(r8x,r8y, "g.");
             ptl.plot(r8x,r8y, "-g");
    else:
        cont7=0;
        r5y.clear();
        r5x.clear();
    
       

       
ptl.plot(r1x,r1y, "g.");
    
ptl.show();