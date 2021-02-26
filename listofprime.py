
import json
#$N = 1024*1024*1024*1024*1024*1024*16
N = 1024
p=[2]
for n in range(3,N,2) : 
  if all((n%i)!=0 for i in (h for h in p if h*h<=n)) : p.append(n)
#print ' '.join(str(x) for x in p)
print( json.dumps(p) )

