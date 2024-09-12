import math

def is_fibonacci(n):
    if n < 0:
        return False
    
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x

    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

def main():
    while True:
        try:
            num = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")
            continue

        if is_fibonacci(num):
            print(f"O número {num} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {num} não pertence à sequência de Fibonacci.")
        
        continuar = input("Deseja verificar outro número? (sim/não): ").strip().lower()
        if continuar not in ['sim', 's']:
            break

    print("Programa encerrado.")

if __name__ == "__main__":
    main()
