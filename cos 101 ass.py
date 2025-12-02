name = input ("what your name ")
name = input ("what your name ")
print(' hi ' + name )
tab = input(name + ' do you want to write a test yes/no ' )


if tab == "yes":
    print("chose the formular u want to solve")
    print(" choice 1  mass x accelration")
    print(" choice 2  distance/time ")
    print(" choice 3  mass/voluume")
    print("choice 4  work/time")
chooz = input('choose one of the  4 options')


if chooz == "1":
    m = float(input("enter mass "))
    a =float(input("enter acceleration "))
    print(m*a)

if chooz == "2":
        d = float(input("enter distance "))
        t = float(input("enter time"))
        print(d / t)

if chooz == "3":
        M = float(input("enter mass "))
        v = float(input("enter volume "))
        print(M / v)

if chooz == "4":
        w = float(input("enter work done "))
        T = float(input("enter time "))
        print( w*T )

if chooz == "no":
    print("oh ok maybe next time")



