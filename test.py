from utils import Converter


class TestConverter:
    def test_calculation(self):
        sc = Converter("USD", "EUR", 3)
        assert type(sc.calculation()) == float

    def test_calculation_2(self):
        sc = Converter("AAAA", "EUR", 3)
        assert sc.calculation() == "Код валюты не найден"

    def test_calculation_3(self):
        sc = Converter("EUR", "EUR", 1)
        assert sc.calculation() == 1.00
