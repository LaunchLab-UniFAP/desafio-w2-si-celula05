"""Testes das regras de governanca da coleta."""

import math
import unittest

from src.governanca_si import (
    ALERTA_OCIOSIDADE,
    EFICIENCIA_ACEITAVEL,
    METADADOS_COMPLIANCE,
    calcular_eficiencia_financeira,
)


class CalcularEficienciaFinanceiraTest(unittest.TestCase):
    def test_alerta_abaixo_de_trinta_por_cento_da_capacidade(self) -> None:
        self.assertEqual(calcular_eficiencia_financeira(10), ALERTA_OCIOSIDADE)
        self.assertEqual(calcular_eficiencia_financeira(14.99), ALERTA_OCIOSIDADE)

    def test_aceita_o_limite_e_volumes_superiores(self) -> None:
        self.assertEqual(calcular_eficiencia_financeira(15), EFICIENCIA_ACEITAVEL)
        self.assertEqual(calcular_eficiencia_financeira(50), EFICIENCIA_ACEITAVEL)
        self.assertEqual(calcular_eficiencia_financeira(55), EFICIENCIA_ACEITAVEL)

    def test_limite_deriva_dos_metadados(self) -> None:
        limite = (
            METADADOS_COMPLIANCE["limite_frota_m3"]
            * METADADOS_COMPLIANCE["percentual_minimo_ocupacao"]
        )
        self.assertEqual(limite, 15.0)

    def test_rejeita_valores_negativos_nao_finitos_e_booleanos(self) -> None:
        for volume in (-1, math.inf, -math.inf, math.nan):
            with self.subTest(volume=volume):
                with self.assertRaises(ValueError):
                    calcular_eficiencia_financeira(volume)

        with self.assertRaises(TypeError):
            calcular_eficiencia_financeira(True)
        with self.assertRaises(TypeError):
            calcular_eficiencia_financeira("10")  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
