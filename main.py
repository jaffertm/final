datos = {}

nota1 = int(input("Ingrese la primera nota del curso: "))
nota2 = int(input("Ingrese la segunda nota del curso: "))
nota3 = int(input("Ingrese la tercera nota del curso: "))
nota4 = int(input("Ingrese la cuarta nota del curso: "))
total = nota1 + nota2 + nota3 + nota4
promedio = total / 4
print("El promedio es: ", promedio)
tupla = [str(nota1), " ", str(nota2), " ", str(nota3), " ", str(nota4)]
cadena = "".join(tupla)
codigo = input("Ingrese el codigo del alumno: ")
nombre = input("Ingrese el nombre del alumno: ")
curso = input("Ingrese el nombre del curso: ")

f = open("demofile.txt", "w")
f.write("\n" + cadena)
f.close()
f = open("demofile.txt")
print(f.read())
f.close()