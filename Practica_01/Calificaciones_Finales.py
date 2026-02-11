Cal_alumnos = [8,8,7,5,0,9,9,5,6,10]
Cal_alumnos.sort()
print(Cal_alumnos)

suma_calificaciones = 0
for i in Cal_alumnos:
    suma_calificaciones += i 
print(suma_calificaciones)

promedio_cal = suma_calificaciones / len(Cal_alumnos)
print(promedio_cal)

aprobado = 0
reporobado = 0 

for i in Cal_alumnos:
    if i >= 7:
        aprobado +=1
    else:
        reporobado +=1

aprobados_porcentaje = (aprobado/promedio_cal)*100
reporobado_porcentaje = (reporobado/promedio_cal)*100
print("Aprobados: ",aprobado)
print("Reprobados: ",reporobado)
print("Porcentaje aprovados ",aprobados_porcentaje,"%")
print("Porcentaje de reprobados ",reporobado_porcentaje,"%")