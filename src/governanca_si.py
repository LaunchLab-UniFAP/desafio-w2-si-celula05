"""Regras de governanca economica e ambiental da operacao de coleta."""

from __future__ import annotations

import math
from numbers import Real


METADADOS_COMPLIANCE = {
    "limite_frota_m3": 50.0,
    "percentual_minimo_ocupacao": 0.30,
    "indicadores_ambientais": ["Reducao CO2", "Economia Combustivel"],
}


ALERTA_OCIOSIDADE = "Alerta: Alto Custo de Ociosidade Detectado"
EFICIENCIA_ACEITAVEL = "Eficiencia Economica Aceitavel"


def calcular_eficiencia_financeira(volume_final: Real) -> str:
    """Classifica a viagem pela ocupacao minima definida no manifesto."""

    if isinstance(volume_final, bool) or not isinstance(volume_final, Real):
        raise TypeError("volume_final deve ser um numero real.")

    volume = float(volume_final)
    if not math.isfinite(volume):
        raise ValueError("volume_final deve ser finito.")
    if volume < 0:
        raise ValueError("volume_final nao pode ser negativo.")

    limite_viabilidade = (
        METADADOS_COMPLIANCE["limite_frota_m3"]
        * METADADOS_COMPLIANCE["percentual_minimo_ocupacao"]
    )

    if volume < limite_viabilidade:
        return ALERTA_OCIOSIDADE
    return EFICIENCIA_ACEITAVEL


if __name__ == "__main__":
    print(calcular_eficiencia_financeira(12.5))
