def calcular_percentual_representacao(faturamento):
    total_faturamento = sum(faturamento.values())
    percentual_representacao = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento.items()}
    return percentual_representacao, total_faturamento

def formatar_saida(faturamento, percentuais, total_faturamento):
    print("="*60)
    print(f"{'Estado':<15} {'Faturamento (R$)':<20} {'Percentual (%)':<20}")
    print("="*60)
    for estado, valor in faturamento.items():
        percentual = percentuais[estado]
        print(f"{estado:<15} R${valor:>14,.2f} {percentual:>18.2f}%")
    print("="*60)
    print(f"Total de faturamento: R${total_faturamento:,.2f}")
    print("="*60)

def main():
    faturamento = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    percentuais, total_faturamento = calcular_percentual_representacao(faturamento)
    formatar_saida(faturamento, percentuais, total_faturamento)

if __name__ == "__main__":
    main()
