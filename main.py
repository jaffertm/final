datos = {"codigo": ["001", "002", "003", "004", "005"],
         "nombre": ["Juan", "Jose", "Yesica", "Carlos", "Daniela"],
         "curso": ["Ingles", "Diseño web", "Matematicas", "Desarrollo personal", "Soporte de TI"]}

listadatos = []
promedio = 0
resp = "s"
while resp == "s":
    codigoIn = input("Ingrese el codigo del alumno: ",)
    nombre = input("Ingrese el nombre del alumno: ")
    curso = input("Ingrese el nombre del curso: ")
    nota1 = int(input("Ingrese la primera nota del curso: "))
    nota2 = int(input("Ingrese la segunda nota del curso: "))
    nota3 = int(input("Ingrese la tercera nota del curso: "))
    nota4 = int(input("Ingrese la cuarta nota del curso: "))
    x = 0
    for i in datos["codigo"]:
        if i == codigoIn:
            codigoTemp = i
            nombreTemp = datos["nombre"][x]
            cursoTemp = datos["curso"][x]
            registro = codigoTemp, nombreTemp, cursoTemp
            listadatos.append(registro)
            total = nota1 + nota2 + nota3 + nota4
            promedio = total / 4
            print("El promedio es: ", promedio)
            cadena = ["Codigo:" + str(codigoTemp) + " | " + "Nombre :" + str(nombreTemp) + " | " + "Curso :" + cursoTemp + " | " + "Promedio: " + str(promedio) + " | " +"Nota 1: " + str(nota1) + " | " + "Nota 2: " + str(nota2) + " | " + "Nota 3: " + str(nota3) + " | " + "Nota 4: " + str(nota4)]
            f = open("demofile.txt", "a")
            cadena = "".join(cadena)
            f.write("\n" + cadena)
            f.close()
        x += 1
    resp = input("¿Desea seguir ingresando datos? : s/n ")
f = open("demofile.txt")
print(f.read())
f.close()