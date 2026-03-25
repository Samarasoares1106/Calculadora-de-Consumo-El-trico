# ⚡ Calculadora de Consumo Elétrico
# Desenvolvido por: Samara Soares

def calcular_consumo():
    print("="*30)
    print("🔌 Calculadora de Consumo Elétrico")
    print("="*30 + "\n")
    
    # Entrada de dados
    aparelho = input("Nome do aparelho: ")
    potencia = float(input("Potência do aparelho em watts (W): "))
    horas_dia = float(input("Horas de uso por dia: "))
    
    # Cálculo do consumo mensal (kWh)
    # Fórmula: (Potência * Horas * Dias) / 1000
    consumo_mensal = (potencia * horas_dia * 30) / 1000
    
    # Cálculo do custo estimado (Baseado em R$ 0,75 por kWh)
    custo_kwh = 0.75  
    custo_estimado = consumo_mensal * custo_kwh
    
    # Exibição dos resultados formatados
    print("\n" + "-"*30)
    print("📊 RESULTADO DO CÁLCULO")
    print("-"*30)
    print(f"🔹 Aparelho: {aparelho}")
    print(f"🔹 Consumo mensal: {consumo_mensal:.2f} kWh")
    print(f"🔹 Custo mensal estimado: R$ {custo_estimado:.2f}")
    print("-"*30)

if __name__ == "__main__":
    calcular_consumo()
