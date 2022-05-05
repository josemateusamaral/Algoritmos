print('\nCelsius\t\tfahrenheit')
temperaturaCelsius = 0
while (temperaturaCelsius != 101):
    if temperaturaCelsius % 10 == 0:
        conversaoFahrenheit = int( (temperaturaCelsius * (9/5)) + 32 )
        print(temperaturaCelsius,'\t\t',conversaoFahrenheit)
    temperaturaCelsius += 1
