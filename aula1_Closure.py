# Closure -> Função definida e retornada dentro de outra função
# Toda Closure é uma inner function, mas nem toda inner function é um closure. A função deve ser retornada!

def aplicar(objeto, nome, *args, **kwargs):
    if not hasattr(objeto, nome):
        raise AttributeError(f"{type(objeto).__name__} não tem \"{nome}\"")
    atributo = getattr(objeto, nome)
    
    if callable(atributo):
        return atributo(*args, **kwargs)
        
    return atributo

texto = "   Buss    "

fruta = "    Banana "

print(aplicar(texto, "strip"))
print(aplicar(fruta, "replace", "a", "@"))


print("#"*60)

def registrar_evento(mensagem):
    print("Evento:", mensagem)

registrar_evento.contador = 0
registrar_evento.log = []

print(registrar_evento.__dict__)

def armazenar_evento(mensagem):
    registrar_evento.contador += 1
    registrar_evento.log.append(mensagem)
    registrar_evento(mensagem)
    print(f"Chamadas: {registrar_evento.contador}")
    print(f"HIstórico: {registrar_evento.log}")
    
armazenar_evento("Sistema Iniciado")
armazenar_evento("Usuário Autenticado")


print("#"*60)

def saudador(pessoa):
    saudacao = "Bem-vindo"
    
    def mensagem():
        return f"{saudacao}, {pessoa}"
    
    # return mensagem()
    return mensagem

# print(saudador("Joao"))
print(hasattr(saudador.__code__.co_consts, "__iter__"))
print(hasattr(saudador.__code__.co_consts, "__next__"))

for cada_constante in saudador.__code__.co_consts:
    if isinstance(cada_constante, type(saudador.__code__)):
        print(f"Função interna detectada: {cada_constante.co_name}")
        
        
msg_joao = saudador("João")
msg_claudio = saudador("Cláudio")
print(msg_joao())
print(msg_claudio())

print(msg_joao.__closure__)

print("#"*60)

# Exemplo de closure com lambda
def greetings():
    nome = "Bunda"
    return lambda: print(f"Oi, {nome}!")

greeter = greetings()
greeter()

def make_counter():
    count = 0
    def counter():
        nonlocal count # Como int não é imutável, eu tenho que falar pro python que count +=1 não cria uma nova, mas sim usa a velha
        # Mutáveis: dict, lista e set
        count += 1
        print(count)
        return count
    
    return counter

counter = make_counter()
counter()
counter()
counter()

print("#"*60)

# Situação em que Closure vale mais a pena

class ValidadorDeIntervalo:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val   
    # O método __call__ torna a instância da classe "chamável" como uma função.
    def __call__(self, valor):
        return self.min_val <= valor <= self.max_val
    
# Esta é uma função fábrica. Ela cria e retorna outras funções.
def cria_validador(min_val, max_val):
    def validador(valor):
        return min_val <= valor <= max_val
    return validador

# Usar closure é menos verboso e mais prático

# CRIANDO CACHE

def memoize(function):
     cache = {}
     def closure(number):
         if number not in cache:
             cache[number] = function(number)
         return cache[number]
     return closure