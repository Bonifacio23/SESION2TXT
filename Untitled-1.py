def calcular_ren():
    print("="*50)
    print("\tSISTEMA DE BOLETIN DE CALIFICACIONES")
    print("="*50)
    resumen_notas = ""
    suma_notas = 0
    nota_max = -1
    nota_min = 21
    curso_mayor = ""
    curso_menor = ""
    cantidad_cursos = 0
    continuar = "s"
    while continuar.lower() == "s":
        print("cursos Nro", (cantidad_cursos+1))
        curso = input("Ingrese el nombre del curso: ")
        if curso == "":
            print("Tienes que registrar por lo menos un curso")
            continue
        while True:
            try:
                notas = float(input("Ingrese la nota del curso[0-20]: "))
                if notas<0 or notas>20 :
                    print("Ingrese una nota entre 0-20")
                    continue
                break
            except ValueError:
                print("Ingrese un valor numerico valido")
        suma_notas += notas
        cantidad_cursos += 1
        resumen_notas += f"-{curso}: {notas:.2f}\n"
        #nota maxima
        if notas>nota_max:
            nota_max = notas
            curso_mayor = curso
        #nota minima
        if notas<nota_min:
            nota_min = notas
            curso_menor = curso
            
        print("Registro exitoso")
        
        continuar = input("Desea continuar(s/n):")
    promedio = suma_notas/cantidad_cursos
    print("="*50)
    print("\tRESUMEN DE NOTAS")
    print("="*50)
    if promedio>=13.0:
        condicion = "Aprobado"
    elif promedio>=10.5:
        condicion = "Recuperacion"
    else: 
        condicion = "Desaprobado"
    print("Cursos:\n", resumen_notas)
    print("Cursos Evaluados: ", cantidad_cursos)
    print(f"promedio: {promedio:.2f}")
    print(f"la nota maxima es: {curso_mayor} - {nota_max:.2f}")
    print(f"la nota minima es: {curso_menor} - {nota_min:.2f}")
    print(f"Condición academica: {condicion}")

if __name__ == "__main__":
    calcular_ren()
