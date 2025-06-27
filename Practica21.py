#Comparaciones de cursos.
#Datos de cursos
curso_max = 7
curso_min = 2.5
curso_pro = 4
curso_dalto = 1.5
curso_dalto_crudo = 3.5
curso_pro_crudo = 5
#Diferencias de porcentajes.
diferencia_curso_min = 100 - curso_dalto/curso_min * 100
print (f"\nla diferencia entre el curso de tiempo minimas y el curso de dalto es = {diferencia_curso_min}%")

diferencia_curso_pro = 100 - curso_dalto/curso_pro * 100
print (f"\nla diferencia entre el curso de tiempo promedio y el curso de dalto es = {diferencia_curso_pro}%")

diferencia_curso_max = 100 - curso_dalto/curso_max * 100
print (f"\nla diferencia entre el curso de tiempo máximo y el curso de dalto es = {diferencia_curso_max:.2f}%")

tiempo_promedio_crudo = (curso_pro_crudo-curso_pro)
porcentaje_tiempo_crudo_promedio = (tiempo_promedio_crudo/curso_pro_crudo)*100  
print (f"\nel porcentaje de tiempo editado/crudo en el curso promedio es = {porcentaje_tiempo_crudo_promedio:.2f}%")

tiempo_dalto_crudo = (curso_dalto_crudo-curso_dalto)
porcentaje_tiempo_crudo_dalto = (tiempo_dalto_crudo/curso_dalto_crudo)*100
print (f"\nel porcentaje de tiempo editado/crudo en el curso de dalto es = {porcentaje_tiempo_crudo_dalto:.2f}%\n")


escala_10horas_dalto = (10/curso_dalto)

curso_pro_equivalente = curso_pro*escala_10horas_dalto
print (f"\nSi vemos 10 horas en el curso de dalto, es equivalente a que en un curso promedio veamos = {curso_pro_equivalente:.2f} horas")

curso_max_equivalente = curso_max*escala_10horas_dalto
print (f"\nSi vemos 10 horas en el curso de dalto, es equivalente a que en un curso de máxima duración veamos = {curso_max_equivalente:.2f} horas")

curso_min_equivalente = curso_min*escala_10horas_dalto
print (f"\nSi vemos 10 horas en el curso de dalto, es equivalente a que en un curso de mínima duración  veamos = {curso_min_equivalente:.2f} horas\n")


escala_10horas_pro = (10/curso_pro)

curso_dalto_equivalente = curso_dalto*escala_10horas_pro
print (f"\nSi vemos 10 horas en el curso promedio, es equivalente a que en un curso de dalto veamos = {curso_dalto_equivalente:.2f} horas")

curso_max_equivalente = curso_max*escala_10horas_pro
print (f"\nSi vemos 10 horas en el curso promedio, es equivalente a que en un curso de máxima duración  veamos = {curso_max_equivalente:.2f} horas")

curso_min_equivalente = curso_min*escala_10horas_pro
print (f"\nSi vemos 10 horas en el curso promedio, es equivalente a que en un curso de mínima duración  veamos = {curso_min_equivalente:.2f} horas\n")


escala_10horas_max = (10/curso_max)

curso_pro_equivalente = curso_pro*escala_10horas_max
print (f"\nSi vemos 10 horas en el curso de máxima duración, es equivalente a que en un curso promedio veamos = {curso_pro_equivalente:.2f} horas")

curso_max_equivalente = curso_dalto*escala_10horas_max
print (f"\nSi vemos 10 horas en el curso de máxima duración, es equivalente a que en un curso de dalto veamos = {curso_max_equivalente:.2f} horas")

curso_min_equivalente = curso_min*escala_10horas_max
print (f"\nSi vemos 10 horas en el curso de máxima duración, es equivalente a que en un curso mínima duración  veamos = {curso_min_equivalente:.2f} horas\n")


escala_10horas_min = (10/curso_min)

curso_pro_equivalente = curso_pro*escala_10horas_min
print (f"\nSi vemos 10 horas en el curso de mínima duración, es equivalente a que en un curso de mínima duración  veamos = {curso_pro_equivalente:.2f} horas")

curso_max_equivalente = curso_max*escala_10horas_min
print (f"\nSi vemos 10 horas en el curso de mínima duración, es equivalente a que en un curso de máxima duración  veamos = {curso_max_equivalente:.2f} horas")

curso_min_equivalente = curso_dalto*escala_10horas_min 
print (f"\nSi vemos 10 horas en el curso de mínima duración, es equivalente a que en un curso de dalto veamos = {curso_min_equivalente:.2f} horas\n")