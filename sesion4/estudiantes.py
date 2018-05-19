# funciones utiles

# recibir datos de estudiantes
columnas = ["nombre", "apellido", "CI", "edad", "estatura", "notas"]
col_notas = ["mate", "lite", "sociales"]

estudiantes = []

for i in range(5):
    print(i)
    valor = 0
    dic = {}
    for col in columnas:
        if col == "notas":
            print("ingrese las notas:")
            notas_dic = {}
            for materia in col_notas:
                valor1 = raw_input(materia + ": ")
                notas_dic[materia] = valor1
            valor = notas_dic
        else:
            valor = raw_input("ingrese " + col + ": ")
            
        dic[col] = valor
        
    estudiantes.append(dic)
print(estudiantes)
# definir si estan aprobados

# imprimir estadisticas
