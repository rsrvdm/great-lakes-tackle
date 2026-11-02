# Run from the repo root: python3 src/build.py
import base64,re
def uri(f,m): return f'data:{m};base64,'+base64.b64encode(open('assets/'+f,'rb').read()).decode()
s=open('src/src.html').read()
M={'LOGO':('glt-logo-original.jpg','image/jpeg'),'HERO':('hero.webp','image/webp'),'AERIAL':('aerial.webp','image/webp'),'P1':('p1.webp','image/webp'),'P3':('p3.webp','image/webp')}
for i in range(1,7):
    M[f'T{i}']=(f't{i}.webp','image/webp');M[f'R{i}']=(f'r{i}.webp','image/webp')
for k,(f,m) in M.items(): s=s.replace('{{'+k+'}}',uri(f,m))
open('index.html','w').write(s);print(len(s)//1024,'KB',re.findall(r'\{\{\w+\}\}',s))
