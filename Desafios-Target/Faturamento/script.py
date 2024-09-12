import json
import datetime

def calcular_faturamento(dados):
    """Calcula o menor valor, maior valor, dias acima da média e retorna também o faturamento diário com o dia da semana."""
    
    for dia in dados['faturamento_diario']:
        data = datetime.datetime.strptime(dia['dia'], "%Y-%m-%d")
        dia['dia_semana'] = data.strftime('%A')

    faturamento_completo = [dia['valor'] for dia in dados['faturamento_diario'] if dia['valor'] > 0]

    if not faturamento_completo:
        return {
            "menor_valor": None,
            "maior_valor": None,
            "dias_acima_media": 0,
            "faturamento_diario": dados['faturamento_diario']
        }
    
    menor_valor = min(faturamento_completo)
    maior_valor = max(faturamento_completo)
    media_faturamento = sum(faturamento_completo) / len(faturamento_completo)
    
    dias_acima_media = sum(1 for valor in faturamento_completo if valor > media_faturamento)
    
    return {
        "menor_valor": menor_valor,
        "maior_valor": maior_valor,
        "dias_acima_media": dias_acima_media,
        "faturamento_diario": dados['faturamento_diario']
    }

def formatar_saida(resultado):
    """Formata e exibe os resultados do cálculo e o faturamento diário com o dia da semana."""
    print(f"Menor valor de faturamento: R${resultado['menor_valor']:.2f}")
    print(f"Maior valor de faturamento: R${resultado['maior_valor']:.2f}")
    print(f"Número de dias com faturamento acima da média: {resultado['dias_acima_media']}")
    
    print("\nRelatorio faturamento Diário:")
    for dia in resultado['faturamento_diario']:
        print(f"{dia['dia']} ({dia['dia_semana']}): R${dia['valor']:.2f}")

def main():
    try:
        with open('faturamento.json', 'r') as file:
            dados = json.load(file)
        
        resultado = calcular_faturamento(dados)
        
        formatar_saida(resultado)
    
    except FileNotFoundError:
        print("Erro: O arquivo 'faturamento.json' não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro: O arquivo 'faturamento.json' não está no formato JSON correto.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()

