from random import randint


class Calculate:
    def __init__(self: object, difficulty_lvl: int, /) -> None:
        self.__difficulty_lvl: int = difficulty_lvl
        self.__value1: int = self._generate_value
        self.__value2: int = self._generate_value
        self.__operation: int = randint(1, 3)
        self._results: int = self._generate_results

    @property
    def difficulty(self: object) -> int:
        return self.__difficulty_lvl

    @property
    def value1(self: object) -> int:
        return self.__value1

    @property
    def value2(self: object) -> int:
        return self.__value2

    @property
    def operation(self: object) -> int:
        return self.__operation

    @property
    def generate_results(self: object) -> int:
        return self._generate_results

    def __str__(self: object) -> str:
        op: str = ''
        if self.operation == 1:
            op = 'Somar'

        elif self.operation == 2:
            op = 'Diminuir'

        elif self.operation == 3:
            op = 'Multiplicar'

        else:
            op = 'Operação inválida'

        return f'Valor 1: {self.value1}\nValor 2: {self.value2}\nDificuldade: {self.difficulty}\nOperação: {op}'

    @property
    def _generate_value(self: object) -> int:

        if self.difficulty == 1:
            return randint(0, 10)
        elif self.difficulty == 2:
            return randint(0, 100)
        elif self.difficulty == 3:
            return randint(0, 1000)
        else:
            return randint(0, 10000)

    @property
    def _generate_results(self: object) -> int:
        if self.operation == 1:
            return self.value1 + self.value2
        elif self.operation == 2:
            return self.value1 - self.value2
        elif self.operation == 3:
            return self.value1 * self.value2

    @property
    def _op_symble(self: object) -> str:   # opcional
        if self.operation == 1:
            return '+'
        elif self.operation == 2:
            return '-'
        else:
            return '*'

    def check_results(self: object, answer: int) -> bool:
        certo: bool = False

        if self._results == answer:
            print('Resposta correta')
            certo = True
        else:
            print('Resposta errada')
        print(
            f'{self.value1} {self._op_symble} {self.value2} = {self._results}'
        )
        return certo

    def show_operation(self: object) -> None:
        print(f'{self.value1} {self._op_symble} {self.value2} = ?')
