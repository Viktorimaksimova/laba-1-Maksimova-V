import doctest


class Soap:
    def __init__(self, weight_soap: float, form_soap: str):
        """
        Создание и подготовка к работе объекта "Мыло"

        :param weight_soap: Масса мыла в граммах
        :param form_soap: Форма мыла

        Примеры:
        >>> soap = Soap(85,"Прямоугольная")  # инициализация экземпляра класса
        """
        if not isinstance(weight_soap, (int, float)):
            raise TypeError("Масса мыла должна быть типа int или float")
        if weight_soap <= 0:
            raise ValueError("Масса мыла должна быть положительным числом")
        self.weight_soap = weight_soap

        if not isinstance(form_soap, (str)):
            raise TypeError("Форма мыла должна быть str")
        self.form_soap = form_soap

    def soap_exists(self) -> bool:
        """
        Функция которая проверяет существует ли мыло

        :return: Существует ли мыло

        Примеры:
        >>> soap = Soap(85,"Прямоугольная")
        >>> soap.soap_exists()
        """
        ...

    def soap_foaming(self, foam: float) -> None:
        """
        Вспенивание мыла.
        :param foam: Объем добавляемой жидкости

        :raise ValueError: Если количество вспениного мыла превышает массу мыла, то вызываем ошибку

        Примеры:
        >>> soap = Soap(85,"Прямоугольная")
        >>> soap.soap_foaming(2)
        """
        if not isinstance(foam, (int, float)):
            raise TypeError("Вспененное мыло должно быть типа int или float")
        if water < 0:
            raise ValueError("Вспененное мыло должно быть положительным числом")
        ...

    def melting_and_adding_extra_soap(self, extra_soap: float) -> None:
        """
        Расплавка и прибавление дополнительного мыла

        :param extra_soap: Масса добавленного мыла
        Примеры:
        >>> soap = Soap(85,"Прямоугольная")
        >>> soap.melting_and_adding_extra_soap(200)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации