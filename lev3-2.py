'''
11. Make a temperature/measurement converter. Write a script that can convert
Fahrenheit to Celcius and back, or inches to centimeters and back, etc in 3 different
ways
'''
def feh2celc(feh):
    return float(feh)-32 *(5/9)
def celsiusToFahrenheit(Celsius):
    Fahrenheit = (Celsius * 9/5) + 32
    return Fahrenheit
if __name__ == '__main__':

    feh = float(input('inter the tempreture in fahrenhite :'))
    #first using lambda
    cel =lambda feh:float(feh)-32 *(5/9)
    print(f"the tempreture = {cel(feh)}")
    #####second way using function
    x = feh2celc(feh)
    print(x)

    ###third way using only variable
    cel = float(feh)-32*(5/9)
    print(cel)
