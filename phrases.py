from textblob import TextBlob

def analisar_sentimento(frase):
    """Analisa o sentimento da frase usando TextBlob."""
    polaridade = TextBlob(frase).sentiment.polarity
    if polaridade > 0:
        return "Positiva"
    elif polaridade < 0:
        return "Negativa"
    return "Neutra"

def testar_casos_extremos():
    """Executa testes de casos extremos para a função de análise de sentimento."""
    casos = [
        ("", "Neutra"),
        ("!!!???", "Neutra"),
        ("I hate everything about this terrible, horrible, disgusting day!", "Negativa"),
    ]
    print("Testes de casos extremos:")
    for frase, esperado in casos:
        resultado = analisar_sentimento(frase)
        print(f'Frase: "{frase}" | Esperado: {esperado} | Resultado: {resultado}')
    print("-" * 40)

def mostrar_historico(historico):
    """Exibe o histórico de análises realizadas."""
    print("\nHistórico de análises:")
    for frase, resultado in historico:
        print(f'- "{frase}" → {resultado}')

def mostrar_contador(contagem):
    """Exibe o contador de sentimentos detectados."""
    print(f'\nContador: Positiva={contagem["Positiva"]}, Negativa={contagem["Negativa"]}, Neutra={contagem["Neutra"]}\n')

def main():
    testar_casos_extremos()
    historico = []
    contagem = {"Positiva": 0, "Negativa": 0, "Neutra": 0}
    while True:
        frase = input("Digite uma frase para análise de sentimento (ou 'sair' para encerrar): ")
        if frase.lower() == "sair":
            print("Encerrando o aplicativo.")
            break
        resultado = analisar_sentimento(frase)
        historico.append((frase, resultado))
        contagem[resultado] += 1
        print(f"Sentimento detectado: {resultado}")
        mostrar_historico(historico)
        mostrar_contador(contagem)

if __name__ == "__main__":
    main()