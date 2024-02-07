year = int(input("tell me any year: "))
month = int(input("select a month from 1 to 12: "))
day = int(input("chosse a day: "))
if year > 2024:
    print(None)
    break
elif month > 12:
    print(None) 
    break   
if year%4==0 and month==2:
    
    if day > 29:
        print(None)
    else:
        print(day, month, year)

elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
   
    if day > 31:
        print(None)
    else:
        print(day, month, year)

elif month==2:
    
    if day > 28:
        print(None)
    else:
        print(day, month, year)

elif month==4 or month==6 or month==9 or month==11: 
    
    if day > 30:
        print(None)
    else:
        print(day, month, year)
else:
    None


