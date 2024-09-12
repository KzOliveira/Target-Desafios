def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

def formatar_saida(original, invertida):
    largura = max(len(original), len(invertida))
    print("="*largura)
    print(f"{original:<{largura}}")
    print(f"{invertida:<{largura}}")
    print("="*largura)

def main():
    string = "Me chamo, Kevin Oliveira :)!"
    
    string_invertida = inverter_string(string)
    formatar_saida(string, string_invertida)

if __name__ == "__main__":
    main()
