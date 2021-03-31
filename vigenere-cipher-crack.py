from __future__ import division
from fractions import gcd
import string
import numpy as np
from prettytable import PrettyTable
def LeftShift(left_shift,position): 
    return left_shift[position:] + left_shift[:position]
    
    
source=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
coincidence=0
buffer_coincidences=[]
displacement_range = 1

table_of_keys = PrettyTable()
table_of_keys.field_names = ["No. of Shift", "Coincidence"]

table_of_coincidences = PrettyTable()
table_of_coincidences.field_names = ["Coincidence index","Length"]

possible_key_length = PrettyTable()
possible_key_length.field_names = ["Possible Key length from Available keys"]

input=raw_input('Enter your vigener cipher text:').lower()
input=list(input)
buffer2_input=input

    
num = dict(zip(xrange(0,26),string.ascii_lowercase))
letter_frequency = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.0236,0.0015,0.01974,0.00074]

while displacement_range <=30:
    buffer2_input = np.roll(buffer2_input,1)
    for i,j in zip(input,buffer2_input):
        if i==j:
            coincidence+=1
   
    table_of_keys.add_row([displacement_range ,coincidence])           
  
    buffer_coincidences.append(coincidence)
    displacement_range +=1
    coincidence=0

print(table_of_keys)
total_length=max(buffer_coincidences)
table_of_coincidences.add_row(["MAX. number of coincidence" ,total_length])  
  


total_length=buffer_coincidences.index(total_length)
total_length+=1
length_1=sorted(set(buffer_coincidences))[-2]
table_of_coincidences.add_row(["2nd highest coincidence" ,length_1]) 


length_1=buffer_coincidences.index(length_1)
length_1+=1
length_2=sorted(set(buffer_coincidences))[-3]
table_of_coincidences.add_row(["3rd Highest coincidence" ,length_2])
 


length_2=buffer_coincidences.index(length_2)
length_2+=1
length_3=sorted(set(buffer_coincidences))[-4]
table_of_coincidences.add_row(["4th Highest coincidence" ,length_3])

length_3=buffer_coincidences.index(length_3)
length_3+=1
length_4=sorted(set(buffer_coincidences))[-5]
table_of_coincidences.add_row(["5th Highest coincidence" ,length_4])


length_4=buffer_coincidences.index(length_4)
length_4+=1
length_5=sorted(set(buffer_coincidences))[-6]
table_of_coincidences.add_row(["6th Highest coincidence" ,length_5])


length_5=buffer_coincidences.index(length_5)
length_5+=1
buffer_length=[total_length,length_1,length_2,length_3,length_4,length_5]
print(table_of_coincidences)

possible_key_length.add_row([total_length])
possible_key_length.add_row([length_1])
possible_key_length.add_row([length_2])
possible_key_length.add_row([length_3])
possible_key_length.add_row([length_4])
possible_key_length.add_row([length_5])
print(possible_key_length)

buffer_total_gcds= gcd(total_length,length_1)
buffer_total_gcds=gcd(buffer_total_gcds,length_2)
buffer_total_gcds=gcd(buffer_total_gcds,length_3)
buffer_total_gcds=gcd(buffer_total_gcds,length_4)
buffer_total_gcds=gcd(buffer_total_gcds,length_5)
print 'all shifts gcf would be:',buffer_total_gcds

buffer_store=0
while buffer_store<=2:
    total_length=buffer_length[buffer_store]
    print '\n'+'Lets consider ',total_length,'as the possible key length'

    z=[[]for x1 in xrange(0,total_length)]
    v1=0
    while v1<total_length:
        for i2 in xrange(v1,len(input),total_length):
           z[v1].append(input[i2])
        v1+=1

    v1=0
    Array=[]
    while v1<total_length:
        W=[]
        for charc in source:
            b1 = z[v1].count(charc)
            b1 = b1/26
            b1 = round(b1,7)
            W.append(b1)
        I =24
        J=[]
        t=0
        while I>=0:
            B= LeftShift(letter_frequency,t)
            K = np.dot(W,B)
            K = round(K,6)
            J.append(K)
            I -= 1
            t+=1
        Max1=max(J)
        F = [D for D, E in enumerate(J) if E==Max1]
        F[0]=((26-F[0])%26)
        key=num[F[0]].upper()
        Array.append(key)
        S1=[]
        for character in z[v1]:
            number = ord(character) - 97
            number = ((number - F[0])%26)
            S1.append(number)
        a2=[]
        for id2 in S1:
            a2.append(num[id2])
        z[v1]=a2
        v1+=1
    print 'The Encryption Key:',''.join(Array)   


    v1=0
    var=0
    D1=[]
    vv=int(len(input)/total_length)
    while var<vv:
        while v1<total_length:
            D1.append(z[v1][var])
            v1+=1
        var+=1
        v1=0
    v1=0
    while v1<(len(input)%total_length):
        D1.append(z[v1][var])
        v1+=1
    print '\n'+'Your plain Text:'
    print ''.join(str(elm) for elm in D1)
    buffer_store+=1
