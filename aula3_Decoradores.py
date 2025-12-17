import inspect
from functools import wraps 
import time
# O wraps faz com que a documentação das funções  seja mantida usando decorador

def enforce_types(func: callable):
    assinatura = inspect.signature(func)
    anotacoes = func.__annotations__    # Pega a documentação da função"
    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = assinatura.bind(*args, **kwargs)
        bound.apply_defaults() # Busca na assinatura se tem algum argumento default que não foi sobrescrito
                               # Tipo: concatena (texto1, texto2 = "oi").    Nesse caso o "oi" não viria
                               
        for nome_param, valor in bound.arguments.items():
            if nome_param in anotacoes:
                tipo_esperado = anotacoes[nome_param]
                if not isinstance(tipo_esperado, type):
                    raise TypeError(
                        f"Anotação para {nome_param} utiliza um tipo não suportado de constructor: {tipo_esperado!r}"
                    )
                    
                if not isinstance(valor, tipo_esperado):
                    raise TypeError(
                        f"Argumento para {nome_param} utiliza um tipo não suportado de constructor: {tipo_esperado!r} mas recebeu {type(valor)!r}"
                    )
            
        resultado = func(*args, **kwargs)
        
        if "return" in anotacoes:
            tipo_retorno = anotacoes["return"]
            
            if not isinstance(tipo_retorno, type):
                raise TypeError(
                    f"Anotação de retorno utiliza um tipo não suportado de constructor: {tipo_esperado!r}"
                )
                
            if not isinstance(resultado, tipo_esperado):
                raise TypeError(
                    f"Retorno espera {tipo_esperado!r} mas recebeu {type(resultado)!r}"
                )
        return resultado
    
    return wrapper

@enforce_types
def concatena(texto_esquerda: str, texto_direita: str) -> str:
    return texto_esquerda + texto_direita

@enforce_types
def area_retangulo(base: float, altura: float) -> float:
    """ Tipos esperados float + float -> float """
    # Sempre usar documentação nessa disciplina
    return base * altura

print(concatena("Eu adoro ", "a EMAp"))
print(area_retangulo(3.0, 4.0))
# print(area_retangulo("3.0", 4.0)) # A ideia do type hint é se defender disso


###############################################################################
print("#" * 60)


def retry(func, retries=3, exceptions=(Exception,), delay=0.0, backoff=1.0):
    if not isinstance(retries, int) or retries < 1:
        raise ValueError("Retries deve ser int >= 1")
    if not isinstance(delay, (int, float)) or delay < 0:
        raise ValueError("Delay deve ser int ou float >= 0")
    if not isinstance(backoff, (int, float)) or backoff < 1:
        raise ValueError("Backoff deve ser int ou float >= 1")
    
    if not isinstance(exceptions, tuple):
        exceptions = (exceptions,)
    for exc in exceptions:
        if not (isinstance(exc, type) and issubclass(exc, BaseException)):
            raise ValueError("Exceção deve ser classe derivada de BaseException")
            
    def decorator(func):
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            tentativa_atual = 1
            atraso_atual = float(delay)
            
            while True:
                try: 
                    return func(*args, **kwargs)
                except exceptions as err:
                    if tentativa_atual >= retries:
                        raise
                    print(f"Aguardando {atraso_atual:.2f}s para a próxima tentativa...")
                    time.sleep(atraso_atual)
                    
                    # Atualiza os contadores para a próxima iteração do loop
                    tentativa_atual += 1
                    atraso_atual *= backoff # Por conta do CLOSURE, a wrapper SEMPRE vai lembrar dos valores dessas variáveis.
    
        return wrapper
    
    return decorator

# Driver Code
contador = {"falhas" : 0}

@retry(retries=3, exceptions=(ValueError,), delay=0.1, backoff=2.0)
def pode_falhar():
    if contador["falhas"] < 2:
        contador["falhas"] += 1
        raise ValueError("Falhou!")
    return "OK"

print(pode_falhar())

def decorador_com_parametro(parametro1, parametro2):
    print("Fazendo algo com parâmetros")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Aqui o decorador de vdd")
        return wrapper
    return decorator

@decorador_com_parametro(parametro1 = 1, parametro2 = 2)
def funcao():
    pass