#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ulises
"""

import pandas as pd
import matplotlib.pyplot as plt
import math as mt
import numpy as np

def percentil(lista, perc):
    pm = (len(lista)-1) *perc
    pl = mt.floor(pm)
    pu = mt.ceil(pm)
    return lista[pl]+(lista[pu]-lista[pl])*perc

def datos_basicos(lista):
    
    lista.sort()    
    lista2 = []
    for i in lista:
        if mt.isnan(i) == 0:
            lista2.append(i)
    if lista2:         
        mediana = percentil(lista2,0.5)
        pro = np.mean(lista2)
        des = 0
        for i in lista2:
            des += (i - pro)**2
            
        des = des/ (len(lista2))    
            
        print('Mediana: ', mediana)
        print('Promedio: ',pro)
        print('Desviacion Estandar: ', des)    
    
    else:
        print('No hay datos en la lista')
    return

def five_number_summary(lista):
    lista.sort()    
    lista2 = []
    for i in lista:
        if mt.isnan(i) == 0:
            lista2.append(i)
    if lista2:    
        mini = lista2[0]
        maxi = lista2[-1]
        
        mediana = percentil(lista2,0.5)
        fq = percentil(lista2, 0.25)
        tq = percentil(lista2, 0.75)
    
        des = 0
        pro = np.mean(lista2)
    
        for i in lista2:
            des += (i - pro)**2
        
        des = des/ (len(lista2))    
        
        print('Mínimo: ', mini)
        print('Máximo: ', maxi)
        print('Mediana: ', mediana)
        print('Promedio: ',pro)
        print('Cuartil 1: ', fq)
        print('Cuartil 3: ', tq)
        print('Desviacion Estandar: ', des)    
  
    else:
        print('No hay datos en la lista')
    return

def fun_uno(data):
    
    gen = data['Gender'].tolist()
    sal = data['ConvertedComp'].tolist()
    
    lista_hom = []
    lista_muj = []
    lista_des = []
    
    for i in range(0,len(gen)):
        if gen[i] == 'Man' and mt.isnan(sal[i]) == 0:
            lista_hom.append(sal[i])
        else:
            if gen[i] == 'Woman' and mt.isnan(sal[i]) == 0:
                lista_muj.append(sal[i])
            else:
                if mt.isnan(sal[i]) == 0:
                    lista_des.append(sal[i])
    
    print('Datos hombres con salario: \n')
    five_number_summary(lista_hom)
    print('Datos mujeres con salario: \n')
    five_number_summary(lista_muj)
    print('Datos genero desconocido con salario: \n')
    five_number_summary(lista_des)
    
    plt.boxplot(lista_hom)
    plt.boxplot(lista_muj)
    plt.boxplot(lista_des)
    return


def fun_dos(data):
    eth = data['Ethnicity'].tolist()
    sal = data['ConvertedComp'].tolist()
    lista_nom = []
    
    for i in range(0, len(eth)):
       lista_tem = eth[i]
       if pd.isnull(eth[i]) == 0:
           lista_tem = lista_tem.split(';')
           for a in lista_tem:
               tem = lista_nom.count(a)
               if tem == 0:
                   lista_nom.append(a)
    lista_nom.append('Unkown')             
    tot_nom = len(lista_nom)

    sal_tot = []
    for i in range(0,tot_nom):
        sal_tot.append([])
        
    for i in range(0,len(eth)):
        lista_tem = eth[i]
        if pd.isnull(eth[i]) == 0:
            lista_tem = lista_tem.split(';')
            for a in lista_tem:
                for b in lista_nom:
                    if a == b:  
                        ind = lista_nom.index(a)
                        if mt.isnan(sal[i]) == 0:
                            sal_tot[ind].append(sal[i])
        else:                   
            if mt.isnan(sal[i]) == 0:
                sal_tot[len(lista_nom) - 1].append(sal[i])
                
    for i in range(0,len(lista_nom)):           
        if sal_tot[i]:
            print('\nFive Number Summary de ',lista_nom[i])   
            five_number_summary(sal_tot[i]) 
            plt.boxplot(sal_tot[i])
        else:
            print('\nNo hay datos en la lista de ', lista_nom[i])
                                   
    return

def fun_tres(data):
    dt = data['DevType'].tolist()
    sal = data['ConvertedComp'].tolist()
    lista_nom = []
    
    for i in range(0, len(dt)):
       lista_tem = dt[i]
       if pd.isnull(dt[i]) == 0:
           lista_tem = lista_tem.split(';')
           for a in lista_tem:
               tem = lista_nom.count(a)
               if tem == 0:
                   lista_nom.append(a)
    lista_nom.append('Unkown')             
    tot_nom = len(lista_nom)

    sal_tot = []

    for i in range(0,tot_nom):
        sal_tot.append([])
        
    for i in range(0,len(dt)):
        lista_tem = dt[i]

        if pd.isnull(dt[i]) == 0:
            lista_tem = lista_tem.split(';')
            for a in lista_tem:
                for b in lista_nom:
                    if a == b:
            
                        ind = lista_nom.index(a)
                        if mt.isnan(sal[i]) == 0:
                            sal_tot[ind].append(sal[i])
        else:                   
            if mt.isnan(sal[i]) == 0:
                sal_tot[len(lista_nom) - 1].append(sal[i])
                
    for i in range(0,len(lista_nom)):           
        if sal_tot[i]:
            print('\nFive Number Summary de ',lista_nom[i])   
            five_number_summary(sal_tot[i]) 
            plt.boxplot(sal_tot[i])
        else:
            print('\nNo hay datos en la lista de ', lista_nom[i])
                    
    return

def fun_cuatro(data):
    pais = data['Country'].tolist()
    sal = data['ConvertedComp'].tolist()
    lista_nom = []
    
    for i in range(0, len(pais)):
       lista_tem = pais[i]
       if pd.isnull(pais[i]) == 0:
           lista_tem = lista_tem.split(';')
           for a in lista_tem:
               tem = lista_nom.count(a)
               if tem == 0:
                   lista_nom.append(a)
    lista_nom.append('Unkown')             
    tot_nom = len(lista_nom)

    sal_tot = []
    for i in range(0,tot_nom):
        sal_tot.append([])
        
    for i in range(0,len(pais)):
        lista_tem = pais[i]
        if pd.isnull(pais[i]) == 0:
            lista_tem = lista_tem.split(';')
            for a in lista_tem:
                for b in lista_nom:
                    if a == b:
                        ind = lista_nom.index(a)
                        if mt.isnan(sal[i]) == 0:
                            sal_tot[ind].append(sal[i])
        else:                   
            if mt.isnan(sal[i]) == 0:
                sal_tot[len(lista_nom) - 1].append(sal[i])
                
    for i in range(0,len(lista_nom)):           
        if sal_tot[i]:
            print('\nFive Number Summary de ',lista_nom[i])   
            five_number_summary(sal_tot[i]) 
            plt.boxplot(sal_tot[i])
        else:
            print('\nNo hay datos en la lista de ', lista_nom[i])
                                   
    return   

def fun_cinco(data):
    dt = data['DevType'].tolist()
    lista_nom = []
    
    for i in range(0, len(dt)):
       lista_tem = dt[i]
       if pd.isnull(dt[i]) == 0:
           lista_tem = lista_tem.split(';')
           for a in lista_tem:
               tem = lista_nom.count(a)
               if tem == 0:
                   lista_nom.append(a)
    lista_nom.append('Unkown')             
    tot_nom = len(lista_nom)

    res_tot = [0] * tot_nom
    for i in range(0,tot_nom):
        res_tot[i] = 0
        
    for i in range(0,len(dt)):
        lista_tem = dt[i]
        if pd.isnull(dt[i]) == 0:
            lista_tem = lista_tem.split(';')
            for a in lista_tem:
                for b in lista_nom:
                    if a == b:
                        ind = lista_nom.index(a)
                        res_tot[ind]+=1
        else:                   
            res_tot[len(lista_nom) - 1]+=1
            
    print(lista_nom)    
    y_pos = np.arange(len(lista_nom)) 
    plt.bar(y_pos, res_tot)    
    plt.xticks(y_pos, lista_nom) 
    plt.show()
    return

def fun_seis(data):
    gen = data['Gender'].tolist()
    ae = data['YearsCode'].tolist()
     
    bins_hom = []
    bins_muj = []
    bins_des = []
    
    
    for i in range(0,len(gen)):
        if gen[i] == 'Man':
            if pd.isnull(ae[i]) or ae[i] == 'Less than 1 year' or ae[i] == '1' or ae[i] == '2' or ae[i] == '3' or ae[i] == '4':
                bins_hom.append(3)
            if ae[i] == '5' or ae[i] == '6' or ae[i] == '7' or ae[i] == '8' or ae[i] == '9':
                bins_hom.append(8) 
            if ae[i] == '10' or ae[i] == '11' or ae[i] == '12' or ae[i] == '13' or ae[i] == '14':
                bins_hom.append(12)  
            if ae[i] == '15' or ae[i] == '16' or ae[i] == '17' or ae[i] == '18' or ae[i] == '19':
                bins_hom.append(17)  
            if ae[i] == '20' or ae[i] == '21' or ae[i] == '22' or ae[i] == '23' or ae[i] == '24':
                bins_hom.append(22)   
            if ae[i] == '25' or ae[i] == '26' or ae[i] == '27' or ae[i] == '28' or ae[i] == '29':
                bins_hom.append(27)   
            if ae[i] == '30' or ae[i] == '31' or ae[i] == '32' or ae[i] == '33' or ae[i] == '34':
                bins_hom.append(32)   
            if ae[i] == '35' or ae[i] == '36' or ae[i] == '37' or ae[i] == '38' or ae[i] == '39':
                bins_hom.append(37)   
            if ae[i] == '40' or ae[i] == '41' or ae[i] == '42' or ae[i] == '43' or ae[i] == '44':
                bins_hom.append(42)        
            if ae[i] == '45' or ae[i] == '46' or ae[i] == '47' or ae[i] == '48' or ae[i] == '49' or ae[i] == 'More than 50 year':
                bins_hom.append(47)        
        else:
            if gen[i] == 'Woman':
                if pd.isnull(ae[i]) or ae[i] == 'Less than 1 year' or ae[i] == '1' or ae[i] == '2' or ae[i] == '3' or ae[i] == '4':
                    bins_muj.append(3)
                if ae[i] == '5' or ae[i] == '6' or ae[i] == '7' or ae[i] == '8' or ae[i] == '9':
                    bins_muj.append(8) 
                if ae[i] == '10' or ae[i] == '11' or ae[i] == '12' or ae[i] == '13' or ae[i] == '14':
                    bins_muj.append(12)  
                if ae[i] == '15' or ae[i] == '16' or ae[i] == '17' or ae[i] == '18' or ae[i] == '19':
                    bins_muj.append(17)  
                if ae[i] == '20' or ae[i] == '21' or ae[i] == '22' or ae[i] == '23' or ae[i] == '24':
                    bins_muj.append(22)   
                if ae[i] == '25' or ae[i] == '26' or ae[i] == '27' or ae[i] == '28' or ae[i] == '29':
                    bins_muj.append(27)   
                if ae[i] == '30' or ae[i] == '31' or ae[i] == '32' or ae[i] == '33' or ae[i] == '34':
                    bins_muj.append(32)   
                if ae[i] == '35' or ae[i] == '36' or ae[i] == '37' or ae[i] == '38' or ae[i] == '39':
                    bins_muj.append(37)   
                if ae[i] == '40' or ae[i] == '41' or ae[i] == '42' or ae[i] == '43' or ae[i] == '44':
                    bins_muj.append(42)        
                if ae[i] == '45' or ae[i] == '46' or ae[i] == '47' or ae[i] == '48' or ae[i] == '49' or ae[i] == 'More than 50 year':
                    bins_muj.append(47)
            else:
                if pd.isnull(ae[i]) or ae[i] == 'Less than 1 year' or ae[i] == '1' or ae[i] == '2' or ae[i] == '3' or ae[i] == '4':
                    bins_des.append(3)
                if ae[i] == '5' or ae[i] == '6' or ae[i] == '7' or ae[i] == '8' or ae[i] == '9':
                    bins_des.append(8) 
                if ae[i] == '10' or ae[i] == '11' or ae[i] == '12' or ae[i] == '13' or ae[i] == '14':
                    bins_des.append(12)  
                if ae[i] == '15' or ae[i] == '16' or ae[i] == '17' or ae[i] == '18' or ae[i] == '19':
                    bins_des.append(17)  
                if ae[i] == '20' or ae[i] == '21' or ae[i] == '22' or ae[i] == '23' or ae[i] == '24':
                    bins_des.append(22)   
                if ae[i] == '25' or ae[i] == '26' or ae[i] == '27' or ae[i] == '28' or ae[i] == '29':
                    bins_des.append(27)   
                if ae[i] == '30' or ae[i] == '31' or ae[i] == '32' or ae[i] == '33' or ae[i] == '34':
                    bins_des.append(32)   
                if ae[i] == '35' or ae[i] == '36' or ae[i] == '37' or ae[i] == '38' or ae[i] == '39':
                    bins_des.append(37)   
                if ae[i] == '40' or ae[i] == '41' or ae[i] == '42' or ae[i] == '43' or ae[i] == '44':
                    bins_des.append(42)        
                if ae[i] == '45' or ae[i] == '46' or ae[i] == '47' or ae[i] == '48' or ae[i] == '49' or ae[i] == 'More than 50 year':
                    bins_des.append(47)    

    plt.hist(bins_hom, bins = 10)
    plt.show()
    plt.hist(bins_muj, bins = 10)
    plt.show()
    plt.hist(bins_des, bins = 10)
    plt.show()                    
    return

def fun_siete(data):
    dt = data['DevType'].tolist()
    ht = data['WorkWeekHrs'].tolist()
    lista_nom = []
    
    for i in range(0, len(dt)):
       lista_tem = dt[i]
       if pd.isnull(dt[i]) == 0:
           lista_tem = lista_tem.split(';')
           for a in lista_tem:
               tem = lista_nom.count(a)
               if tem == 0:
                   lista_nom.append(a)
    lista_nom.append('Unkown')             
    tot_nom = len(lista_nom)

    hr_tot = []
    for i in range(0,tot_nom):
        hr_tot.append([])
        
    for i in range(0,len(dt)):
        lista_tem = dt[i]
        if pd.isnull(dt[i]) == 0:
            lista_tem = lista_tem.split(';')
            for a in lista_tem:
                ind = lista_nom.index(a)
                if mt.isnan(ht[i]) == 0:
                    hr_tot[ind].append(ht[i])
        else:                   
            if mt.isnan(ht[i]) == 0:
                hr_tot[len(lista_nom) - 1].append(ht[i])
    
    for i in range(0,tot_nom):
        print('Histograma de ',lista_nom[i])
        plt.hist(hr_tot[i], bins = 10)
        plt.show()            
    return

def fun_ocho(data):
    gen = data['Gender'].tolist()
    edad = data['Age'].tolist()
    
    lista_hom = []
    lista_muj = []
    lista_des = []
    
    for i in range(0,len(gen)):
        if gen[i] == 'Man' and mt.isnan(edad[i]) == 0:
            lista_hom.append(edad[i])
        else:
            if gen[i] == 'Woman' and mt.isnan(edad[i]) == 0:
                lista_muj.append(edad[i])
            else:
                if mt.isnan(edad[i]) == 0:
                    lista_des.append(edad[i])
                    
    print('Histograma de Hombres')
    plt.hist(lista_hom, bins = 10)
    plt.show() 
    print('Histograma de Mujeres')
    plt.hist(lista_muj, bins = 10)
    plt.show() 
    print('Histograma de Genero desconocido')
    plt.hist(lista_des, bins = 10)
    plt.show() 
   
    return

def fun_nueve(data):
    pl = data['LanguageWorkedWith'].tolist()
    edad = data['Age'].tolist()
    lista_nom = []
    
    for i in range(0, len(pl)):
       lista_tem = pl[i]
       if pd.isnull(pl[i]) == 0:
           lista_tem = lista_tem.split(';')
           for a in lista_tem:
               tem = lista_nom.count(a)
               if tem == 0:
                   lista_nom.append(a)
    lista_nom.append('Unkown')             
    tot_nom = len(lista_nom)

    edad_tot = []

    for i in range(0,tot_nom):
        edad_tot.append([])
        
    for i in range(0,len(pl)):
        lista_tem = pl[i]
        if pd.isnull(pl[i]) == 0:
            lista_tem = lista_tem.split(';')
            for a in lista_tem:
                ind = lista_nom.index(a)
                if mt.isnan(edad[i]) == 0:
                    edad_tot[ind].append(edad[i])
        else:                   
            if mt.isnan(edad[i]) == 0:
                edad_tot[len(lista_nom) - 1].append(edad[i])
                
    for i in range(0,len(lista_nom)):           
        if edad_tot[i]:
            print('\nDatos de ',lista_nom[i])   
            datos_basicos(edad_tot[i]) 
        else:
            print('\nNo hay datos en la lista de ', lista_nom[i])                   
    return

def fun_diez(data):
    sal = data['ConvertedComp'].tolist()
    ae = data['YearsCode'].tolist()
    lista_sal = []
    lista_ae = []
      
    for i in range(0,len(ae)):
        if ae[i] == 'Less than 1 year' and mt.isnan(sal[i]) == 0:
            lista_sal.append(sal[i])
            lista_ae.append(0.5)
        else:    
            if ae[i] == 'More than 50 years' and mt.isnan(sal[i]) == 0:
                lista_sal.append(sal[i])
                lista_ae.append(50.5)
            else: 
                if pd.isnull(ae[i]) == 0 and mt.isnan(sal[i]) == 0:
                    lista_sal.append(sal[i])
                    lista_ae.append(int(ae[i]))
    
    pro_sal = np.mean(lista_sal)
    pro_ae = np.mean(lista_ae)
    
    sum1 = 0
    sum2 = 0
    sum3 = 0
    
    for i in range(0,len(lista_sal)):
        sum1 += (lista_sal[i]-pro_sal)*(lista_ae[i]-pro_ae)
        sum2 += (lista_sal[i]-pro_sal)**2
        sum3 += (lista_ae[i]-pro_ae)**2
    
    sum2 = mt.sqrt(sum2)
    sum3 = mt.sqrt(sum3)
    
    print('Correlacion entre años de experiencia y salario: ', sum1/(sum2*sum3))   
      
    return

def fun_once(data):
    sal = data['ConvertedComp'].tolist()
    edad = data['Age'].tolist()
    lista_sal = []
    lista_edad = []
    
    for i in range(0,len(sal)):
        if mt.isnan(sal[i]) == 0 and mt.isnan(edad[i]) == 0:
            lista_sal.append(sal[i])
            lista_edad.append(edad[i])
    
    pro_sal = np.mean(lista_sal)
    pro_edad = np.mean(lista_edad)
    
    sum1 = 0
    sum2 = 0
    sum3 = 0
    
    for i in range(0,len(lista_sal)):
        sum1 += (lista_sal[i]-pro_sal)*(lista_edad[i]-pro_edad)
        sum2 += (lista_sal[i]-pro_sal)**2
        sum3 += (lista_edad[i]-pro_edad)**2
    
    sum2 = mt.sqrt(sum2)
    sum3 = mt.sqrt(sum3)
    
    print('Correlacion entre edad y salario: ', sum1/(sum2*sum3))     
    
    return

def fun_doce(data):
    edl = data['EdLevel'].tolist()
    sal = data['ConvertedComp'].tolist()
    lista_nom = []
    edl2 = []
    sal2 = []
    
    for i in range(0, len(edl)):
       lista_tem = edl[i]
       if pd.isnull(edl[i]) == 0:
           lista_tem = lista_tem.split(';')
           for a in lista_tem:
               tem = lista_nom.count(a)
               if tem == 0:
                   lista_nom.append(a)
    
    lista_nom.append('Unkown')             
    tot_nom = len(lista_nom)
    sal_tot = []
    for i in range(0,tot_nom):
        sal_tot.append([])
   
    for i in range(0,len(edl)):
        lista_tem = edl[i]
        if pd.isnull(edl[i]) == 0:
            lista_tem = lista_tem.split(';')
            for a in lista_tem:
                ind = lista_nom.index(a)
                if mt.isnan(sal[i]) == 0:
                    edl2.append(ind + 1)
                    sal2.append(sal[i])
                    
        else:                   
            if mt.isnan(sal[i]) == 0:
                edl2.append(len(lista_nom))
                sal2.append(sal[i])
    
    pro_sal = np.mean(sal2)
    pro_edl = np.mean(edl2)
    
    sum1 = 0
    sum2 = 0
    sum3 = 0
    
    for i in range(0,len(sal2)):
        sum1 += (sal2[i]-pro_sal)*(edl2[i]-pro_edl)
        sum2 += (sal2[i]-pro_sal)**2
        sum3 += (edl2[i]-pro_edl)**2
    
    sum2 = mt.sqrt(sum2)
    sum3 = mt.sqrt(sum3)
    
    print('Correlacion entre salario y nivel de educacion: ', sum1/(sum2*sum3))     
       
    return

def fun_trece(data):
    pl = data['LanguageWorkedWith'].tolist()
    lista_nom = []
    
    for i in range(0, len(pl)):
       lista_tem = pl[i]
       if pd.isnull(pl[i]) == 0:
           lista_tem = lista_tem.split(';')
           for a in lista_tem:
               tem = lista_nom.count(a)
               if tem == 0:
                   lista_nom.append(a)

    lista_nom.append('Unkown')             
    tot_nom = len(lista_nom)

    freq_len = []

    for i in range(0,tot_nom):
        freq_len.append(0)
        
    for i in range(0,len(pl)):
        lista_tem = pl[i]
        if pd.isnull(pl[i]) == 0:
            lista_tem = lista_tem.split(';')
            for a in lista_tem:
                ind = lista_nom.index(a)
                freq_len[ind] += 1 
        else:                   
            freq_len[len(lista_nom) - 1] += 1
                              
    y_pos = np.arange(len(lista_nom))    
    plt.bar(y_pos,freq_len)
    plt.show()
    
    return

i_f = 'survey_results_public.csv'
data = pd.read_csv(i_f,encoding = 'utf-8')
#fun_uno(data)
#fun_dos(data)
#fun_tres(data)
#fun_cuatro(data)
#fun_cinco(data)
#fun_seis(data)
#fun_siete(data)
#fun_ocho(data)
#fun_nueve(data)
#fun_diez(data)
#fun_once(data)
#fun_doce(data)
#fun_trece(data)