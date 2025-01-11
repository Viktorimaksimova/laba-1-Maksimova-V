import doctest


class Chair:
    def __init__(self, height_chair: float, color_chair: str):
        """
        Создание и подготовка к работе объекта "Стул"

        :param height_chair: Высота стула в миллиметрах
        :param color_chair: Цвет стула

        Примеры:
        >>> black_chair = Chair(880,"black")  # инициализация экземпляра класса
        """
        if not isinstance(height_chair, (int, float)):
            raise TypeError("Высота стула должна быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Высота стула должна быть положительным числом")
        self.height_chair = height_chair

        if not isinstance(color_chair, (str)):
            raise TypeError("Цвет стула должен быть str")
        self.color_chair = color_chair

    def chair_exists(self) -> bool:
        """
        Функция которая проверяет существует ли стул

        :return: Существует ли стул

        Примеры:
        >>> black_chair = Chair(880,"black")
        >>> black_chair.chair_exists()
        """
        ...

    def lifting_the_chearseat(self, height: float) -> None:
        """
        Поднятие сидушки стула.
        :param height: Добавленная высота


        Примеры:
        >>> black_chair = Chair(880,"black")
        >>> black_chair.lifting_the_chearseat(200)
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Добавляемая высота должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая высота должна быть положительным числом")
        ...

    def changing_the_chair_deviation(self, degrees: float) -> None:
        """
        Изменение отклонения стула.

        :param degrees: Градус отклоненя спинки
        :raise ValueError: Если градус отклонения превышает 360,
        то возвращается ошибка.


        Примеры:
        >>> black_chair = Chair(880,"black")
        >>> black_chair.changing_the_chair_deviation(110)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


