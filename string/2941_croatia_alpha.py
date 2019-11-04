txt = input()
cro_alpha = ['dz=','c=', 'c-' ,'d-','lj','nj','s=', 'z=']

for alpha in cro_alpha:
    txt = txt.replace(alpha,'1')

print(len(txt))