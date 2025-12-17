# Como parte do functional programming, python permite que funções sejam objetos de primeira classe, 
# que significa que elas podem ser passadas como argumentos e retornadas, assim como int, float, str, etc.

# O nome da função sem () é uma referência pra ela. Usando o () é uma chamada dela. 

def meu_decorador(funcao_original):
    def nova_funcao():
        print("Algo antes da função")
        funcao_original()
        print("Algo depois da função")
        
    return nova_funcao

@meu_decorador
def diga_ola():
    print("olá")
    
@meu_decorador
def diga_oi():
    print("oi")
   
# -------------------dá pra fazer assim tbm------------------

# diga_ola_decorada = meu_decorador(diga_ola)
# diga_oi_decorada = meu_decorador(diga_oi)

# -----------------------------------------------------------

diga_ola()
diga_oi()

# Basicamente, posso modificar qualquer função. 
# É bem melhor usar decoradores ao invés de tentar mudar as funções internamente

print("\n")
print("#" * 60)
print("\n")

from functools import wraps

def dobrar_retorno(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado * 2
    
    return wrapper

def log_args(func):
    @wraps(func) # O wraps nos ajuda a manter a identidade da função que estamos aplicando o decorator.
    def wrapper(*args, **kwargs):  # Sem ela, a função que estamos nos referindo é o wrapper
        print(f"Chamando função {func.__name__} com args={args} e kwargs={kwargs}")
        return func(*args, **kwargs)
        
    return wrapper
    
@dobrar_retorno
@log_args
def soma_1(a, b):
    return a+b

@log_args
def soma_2(a, b, c):
    """
    Essa função soma!!!

    Parameters
    ----------
    a : TYPE
        DESCRIPTION.
    b : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return a+b+c

print("Resultado: ", soma_1(42, 666))
print("Resultado: ", soma_2(13, 42, 666))


print(soma_1.__name__)
print(soma_2.__doc__)


print("\n")
print("#" * 60)
print("\n")

import time

def medir_tempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"{func.__name__} executada em {fim - inicio:.4f}")
        return resultado
        
    return wrapper

@medir_tempo
def soma_3(a,b):
    time.sleep(1)
    return a+b

print(soma_3(1, 2))