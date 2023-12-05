# Vamos a preguntar al usuario cuantos segundos
# y vamos a decirle cuantas horas, minutos y segundos son

# Por ejemplo:
# 3601
# 1 horas 0 minutos 1 segundos
# 3662
# 1 horas 1 minutos 2 segundos

cuantos_segundos = int(input("¿Cuántos segundos quieres convertir? --> "))
# cuantos_segundos = 7261

segundos_en_una_hora = 60 * 60 # 60 segundos x 60 minutos
segundos_en_un_minuto = 60 

horas = cuantos_segundos // segundos_en_una_hora
minutos = (cuantos_segundos - (horas * segundos_en_una_hora)) // segundos_en_un_minuto
segundos = cuantos_segundos -(horas * segundos_en_una_hora) - (minutos * segundos_en_un_minuto)

respuesta = f'''
En {cuantos_segundos} segundos hay:
{horas} horas {minutos} minutos {segundos} segundos
'''

print(respuesta)


print (((1 + 2) - 4) * 3 / 9)
