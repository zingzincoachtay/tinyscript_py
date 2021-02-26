#!/usr/bin/apython

import re
import sys
import json

run_opt = sys.argv

T = [0,0]
P  = [60,60,24,7,4,12,10,100]
Pw = ['s','m','h','d','w','m','y','D','C']
E = []

def pat(m,sl):
    p = re.compile(m)
    return p.search(sl)
def rem(N,D):
    t1 = N % D
    t2 = (N-t1) / D
    return [t1,t2]
def beau(Tf):
    k = 0
    ul = len(Tf)
    while k<ul:
      beau0 = rem(Tf[k],P[k])
      Tf[k] = beau0[0]
      k+=1
      if beau0[1]>0 and k==ul:
        Tf.append(beau0[1])
      elif beau0[1]>0 and k<ul:
        Tf[k] += beau0[1]
    return Tf

def mmss(t0,Tf):
    t = int(t0)
    mmss0 = rem(t,100)
    Tf[0] += mmss0[0]
    Tf[1] += mmss0[1]
    return Tf

def ssss(t0,Tf):
    t = int(t0)
    ssss0 = rem(t,60)
    Tf[0] += ssss0[0]
    Tf[1] += ssss0[1]
    return Tf

while True:
  t = raw_input('duration: ')
  if t == '' or int(t) == 0:
    break
  E.append(t)
  if pat(',',t) or pat(':',t):
    T = t_std(t,T)
  elif pat('\'',t) or pat('"',t):
    T = t_sh(t,T)
  elif '-s' in run_opt:
    T = ssss(t,T)
  else:
    T = mmss(t,T)
  T = beau(T)

improper = []
upper = min( len(T),len(Pw) )
for k in range(upper):
  improper.append( str(T[k])+Pw[k] )
print( improper[::-1] )

f = open('b.out','w')
json.dump(E,f)
#json.dump(E[:-1],f)
f.close()

def t_sh(t0):
    t = split('\'',t)
def t_std(t0):
    t = split(':',t)

