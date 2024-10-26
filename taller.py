from os import system as sys

def es_operador(simbolo):
    return simbolo in {"+", "-", "*", "/", "^"}

def realizar_operacion(op_a, op_b, operador):
    if operador == "+":
        return op_a + op_b
    elif operador == "-":
        return op_a - op_b
    elif operador == "*":
        return op_a * op_b
    elif operador == "/":
        return op_a / op_b
    elif operador == "^":
        return op_a ** op_b
    else:
        raise ValueError(f"Operador no reconocido: {operador}")
    
def evaluar_lista(lista):
    pila = []
    for item in lista:
        if item.isnumeric() or (item.lstrip('-').replace('.', '', 1).isdigit()):
            pila.append(float(item))
        elif es_operador(item):
            if len(pila) < 2:
                print("No hay suficientes datos en la lista")
                return None
            op_b = pila.pop()
            op_a = pila.pop()
            resultado = realizar_operacion(op_a, op_b, item)
            pila.append(resultado)
            print(f"Pila actual: {pila}")
        else:
            print(f"El simbolo ingresado no es permitido: '{item}'")
            
    return pila[0] if pila else "No hay suficientes datos en la lista"

def main():
    sys('cls')
    lista = ['3', '4', '2', '*', '1', '5', '-', '2', '3', '^', '^', '/', '+']
    resultado = evaluar_lista(lista)
    print(f"El resultado final es: {resultado}")

if __name__ == "__main__":
    main()
