def validate_input_choice(msg: str) -> int:
    while True:
        try:
            escolha = int(input(msg))
            
            if 1 <= escolha <= 3:  # Verifica se está no intervalo válido
                return escolha
            else:
                print("\nDigite um valor válido (1, 2 ou 3).")

        except ValueError:  # Captura erro de conversão
            print("\nEntrada inválida! Digite um número válido.")
