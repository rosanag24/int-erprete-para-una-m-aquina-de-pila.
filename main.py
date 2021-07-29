from Interprete import Interprete
from os import path
import re
#### VALIDACION DE ARCHIVO DE ENTRADA #####
def checkFileExistance(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False
##### PROGRAMA PRINCIPAL QUE LLAMA AL INTERPRETE #####    
def main():
    print("INTERPRETE PARA MAQUINA DE PILAS:\n")
    stack = Interprete()
    filename = input(">> Ingrese Nombre del Archivo:")
    if(checkFileExistance(filename)):
        archivo = open(filename)
        linea=archivo.readline()
        while (linea !=''):
            Interprete.stack_op.append(linea)
            linea=archivo.readline()

##### VERIFICAR EL ORDEN DENTRO DE LA PILA ####
#    for item in stack.stack_op:
#        print(item)
#    print(stack.stack_op.pop())        
###############################################
if __name__ == "__main__":
    main()

