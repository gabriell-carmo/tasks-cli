def somar(a, b):
    return a + b

resultado = somar(3, 5)
print(resultado)

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

print(somar(10, 5))
print(subtrair(10, 5))
print(multiplicar(10, 7))
print(dividir(40, 2))
print(dividir(10, 0))

def validar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    return len(cpf) == 11 and cpf.isdigit()

print(validar_cpf("123.456.789-10"))
print(validar_cpf("123.456"))