"""Testes do motor operacional de coleta."""

import unittest

from src.coleta_ads import (
    MENSAGEM_ERRO,
    STATUS_CAPACIDADE,
    converter_volume,
    processar_motor_coleta,
)


def criar_leitor(entradas: list[str]):
    valores = iter(entradas)
    return lambda _: next(valores)


class ConverterVolumeTest(unittest.TestCase):
    def test_converte_numero_e_sentinela(self) -> None:
        self.assertEqual(converter_volume("12.5"), 12.5)
        self.assertEqual(converter_volume("-1"), -1.0)

    def test_rejeita_entrada_invalida(self) -> None:
        for entrada in ("texto", "-2", "nan", "inf", "-inf"):
            with self.subTest(entrada=entrada):
                with self.assertRaises(ValueError):
                    converter_volume(entrada)


class ProcessarMotorColetaTest(unittest.TestCase):
    def test_acumula_ate_atingir_capacidade(self) -> None:
        saidas: list[str] = []
        total = processar_motor_coleta(
            leitor=criar_leitor(["20", "35"]), escritor=saidas.append
        )

        self.assertEqual(total, 55.0)
        self.assertIn(STATUS_CAPACIDADE, saidas)
        self.assertIn("Volume Total: 55 m³", saidas)

    def test_sentinela_encerra_antes_do_limite(self) -> None:
        saidas: list[str] = []
        total = processar_motor_coleta(
            leitor=criar_leitor(["10", "-1"]), escritor=saidas.append
        )

        self.assertEqual(total, 10.0)
        self.assertNotIn(STATUS_CAPACIDADE, saidas)

    def test_descarta_entradas_invalidas_e_continua(self) -> None:
        saidas: list[str] = []
        total = processar_motor_coleta(
            leitor=criar_leitor(["texto", "-2", "nan", "10", "-1"]),
            escritor=saidas.append,
        )

        self.assertEqual(total, 10.0)
        self.assertEqual(saidas.count(MENSAGEM_ERRO), 3)

    def test_rejeita_limite_invalido(self) -> None:
        for limite in (0, -1, float("nan"), float("inf")):
            with self.subTest(limite=limite):
                with self.assertRaises(ValueError):
                    processar_motor_coleta(limite_maximo=limite)


if __name__ == "__main__":
    unittest.main()
