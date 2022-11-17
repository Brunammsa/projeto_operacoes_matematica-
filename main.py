from models.functions import Calculate


def main() -> None:
    points: int = 0
    play(points)


def play(points: int) -> None:
    print('~~~~~~~~~~ Bem vindo ao jogo das operações ~~~~~~~~~~\n\n')
    difficulty: int = int(
        input(
            'Informe o nível de dificuldade desejado. [1 - fácil, 2 - médio, 3 - difícil]: '
        )
    )

    calc: Calculate = Calculate(difficulty)

    print('\nInforme o resultado da operação: ')
    calc.show_operation()

    results: int = int(input())

    if calc.check_results(results):
        points += 1
        print(f'Você tem {points} ponto(s)')

        continue_game: int = int(
            input('Deseja continuar no jogo? [1 - sim, 0 - não]: ')
        )

        if continue_game:
            play(points)

        else:
            print(f'Você finalizou com {points} pontos')
            print('Até a próxima!')
    else:
        print(
            f'Infelizmente você errou e perdeu o jogo, finalizando com {points} pontos'
        )


if __name__ == '__main__':
    main()
