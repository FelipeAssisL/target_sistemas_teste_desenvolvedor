import json

def analisar_faturamento(json_data:json) -> float:
    with open(json_data, 'r') as file:
        dados_faturamento = json.load(file)
    
    faturamentos = [dia["valor"] for dia in dados_faturamento if dia["valor"] > 0]
    
    if not faturamentos:
        print("Não há faturamento registrado.")
        return
    
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_mensal = sum(faturamentos) / len(faturamentos)
    
    dias_acima_da_media = sum(1 for dia in faturamentos if dia > media_mensal)
    
    print(f"Menor faturamento do mês: R$ {menor_faturamento:.2f}")
    print(f"Maior faturamento do mês: R$ {maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

analisar_faturamento("dados.json")


