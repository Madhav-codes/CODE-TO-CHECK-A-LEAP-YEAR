# FIND LEAP YEAR

while (True):
    years = int(input ("ENTER THE YEAR\n"))
    if years%4==0:
        print("YES", years ,"IS A LEAP YEAR!!\n")
        continue
    else:
        print("NO" ,years ,"IS NOT A LEAP YEAR\n ")
        continue