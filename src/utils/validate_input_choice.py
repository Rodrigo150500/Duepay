def validate_input_choice(msg: str) -> int:

    escolha = int(input(msg))

    while escolha <= 0 or escolha >= 4:
        print("\nDigite um valor válido")
        
        escolha = int(input(msg))

    return escolha

