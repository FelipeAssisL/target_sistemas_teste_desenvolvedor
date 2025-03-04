def fibonacci(n:int) -> int:
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")