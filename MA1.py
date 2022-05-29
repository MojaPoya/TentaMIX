"""
Solutions to module 1
Student: Winston Olsson
Mail: winston.lidingo@hotmail.com
Reviewed by: Johan Andersson Östling
Reviewed date: 31/03
"""
#Jsg blev tillsagd att ta bort så mycket kommentarer som möjligt ifall det verkar sträft.
import random
import time

from numpy import empty


def power(x, n):         # Optional
    if n==0:
        return 1
    elif n<0:
        return(power(x,n+1)/x) #Går även att köra en if sats på denna där man kör bara en else och delar 1 med svaret svaret för power.
    else:
        return(x*power(x,n-1))


def multiply(m, n):      # Compulsory
    #För att optimera koden kan igenom att sänka antalet anrop kan vi undersöka vilken av m eller m som är störst och välja den som retunerare
    if n==1:
        return m
    elif n==0 or m==0:
        return 0
    else:
        return (m+(multiply(m,n-1)))



def divide(t, n):
    if n>t:
        return 0
    else:
        return 1+divide(t-n,n)

def harmonic(n):         # Compulsory
    if n==1: #Uppgiften ger positivt heltal så vi antar att allt annat ej går.
        return 1
    else:
        return 1/n + harmonic(n-1) 


def digit_sum(x):        # Optional
    if len(str(x))==1:
        return x
    else:
        return int(str(x)[len(str(x))-1])+digit_sum(int(str(x)[0:len(str(x))-1]))
    


def get_binary(x):       # Optional
    pass

def reverse(s):          # Optional
    if len(s) <= 1:
        return s
    else:
        mid = len(s)// 2
        return reverse(s[mid:]) + reverse(s[:mid])






def largest(a):
    if len(a)==1:
        return a[0]
    if len(a)==2:
        if a[0]>=a[1]:
            return a[0]
        else: 
            return a[1]        



        
        
    else:
        if a[0]>=a[-1]:
            return largest(a[:-1])
        else: 
            return largest(a[1:])




    

def count(x, s):         # Compulsory Modifierad version
    if s==[]:
        return 0  
    if type(s[0])==list:
        if x==s[0]:
            return 1+count(x,s[1:])
        else:
            return count(x,s[0])+count(x,s[1:])       
    elif x==s[0]:
        return 1+count(x,s[1:])
    else:
        return 0+count(x,s[1:])
    

def zippa(l1, l2):       # Compulsory
    if l1==[]:
        return l2
    elif l2==[]:
        return l1
    else:
        
        return [l1[0],l2[0]]+(zippa(l1[1:],l2[1:]))


def bricklek(f, t, h, n): # Compulsory Jag använder mig av att alltid utnyttja 
    if n==1:
        return [f'{f}->{t}'] 
    else:
        return bricklek(f,h,t,n-1)+[f'{f}->{t}'] + bricklek(h,t,f,n-1)


def main():
    """ Demonstates my implementations """
    # Write your demonstration code here
    print('Bye!')
    

if __name__ == "__main__":
    main()
    
####################################################    
# tstart = time.perf_counter ()

# def fib(n):

#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(40))
# tstop = time.perf_counter ()
# print(f"Measured time: {tstop -tstart} seconds")
#Används för att undersöka FIB


    
"""
  Answers to the none-coding tasks
  ================================
  15:
  Bästa fall 1 opperation, då vi kan fortfarande alltid råka gissar rätt.
  Sämsta fall är O(n/2) dvs om vi alltid skulle gissa på talet näst lägnst åt ett hål så bara 1 tal hamnar på ena sida och resterande på andra
  %Detta medför att två tal kan försvinna i en sökning
  
  Exercise 16: Time for bricklek with 50 bricks:
  
  1 sek = 1 förflyttning.
  tn=(2^n)-1 som är 2^50-1= CA 36 miljoner år
  
  
  
  
  Exercise 17: Time for Fibonacci:
  55
Measured time: MT=0.00001269999993382953 seconds, n=10 , 1.618^10 = MT*10^7 , k=10^7

6765
Measured time: 0.0018200000013166573 seconds, n=20 ungefär 1.618^20 =   MT*k
  
832040
Measured time: 0.19872639999994135 seconds,  n=30 ==  MT*k= 1.618^30

102334155
Measured time: 23.75371979999909 seconds, n= 40 ==  MT*k= 1.618^40
#########################################################################################
Notera mätt tid.
MT för n=20; 1.618^20 = MT(n=10)*1.618^10=0.0015616686 vilket sec stämmer ungefär överäns med uppmätt tid
MT för n=30; 1.618^20 = MT(n=10)*1.618^20=0.19203 vilket sec stämmer ungefär överäns med uppmätt tid
MT för n=40; 1.618^20 = MT(n=10)*1.618^30=23.6 vilket sec stämmer ungefär överäns med uppmätt tid




b)

Se uppgift ovan: Detta ger

MT för n=50 = MT(n=10)*1.618^40= 2903.65 sec som är ungefär 48 min
MT för n=50 = MT(n=10)*1.618^90= 8.16^13 sec som är ungefär 2588592 år

  
Exercise 20: Comparison sorting methods:

  T(n^2)= Insersion method
  T(n*log(n))= Merged method.

  T(1000) ger 1 sekund tid.

  
 n=10^6: T_megred(1 000 000)/T_merged(1000)=log(1 000 000)* 1 000 000
  / log(1000) *1000= 2000 gånger längre, 2000 sekunder

n=10^9: T_merged(1 000 000 000)/T_merged(1000)= 9*10^9/(3*10^3)=3*10^6, Tre miljoner sekunder





  b)
   n=10^6: T_insersion(1 000 000)/T_insersion(1000)= 1 000 000^2 / 1 000^2= 10^6 längre tid. En miljon sekunder. Typ 11,5 dagar.
   n=10^9: T_insersion(10^9)/T_insersion(1000)=10^12 sekunder.

  
  
  
Exercise 21: Comparison Theta(n) and Theta(n log n)
  
t(b)=c*t(a)*log(n)

c=1/t(a)=1/10

t(a)<1/10*t(a)*log(n)
10<log(n)

n>10^10





"""