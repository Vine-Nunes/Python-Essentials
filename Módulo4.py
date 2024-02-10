def num(primo):
    if primo%2 != 0 or primo==2 and primo>1:
           if primo%3 != 0 or primo==3:
              print(True,primo)
           else:
              print(False,primo)
    else:
       print(False)

for i in range(1,20):
    if num(i+1):
        print(i+1)
        
