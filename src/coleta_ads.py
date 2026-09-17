"""Motor interativo de coleta de volumes para a frota."""

from __future__ import annotations

import math
from collections.abc import Callable


LIMITE_MAXIMO_M3 = 50.0
SENTINELA_ENCERRAMENTO = -1.0
STATUS_CAPACIDADE = "Status: Capacidade Maxima Atingida"
MENSAGEM_ERRO = "Erro: Entrada Invalida"


def converter_volume(entrada: str) -> float:
    """Converte uma entrada em volume finito e permitido pelo motor."""

    try:
        volume = float(entrada)
    except (TypeError, ValueError) as erro:
        raise ValueError(MENSAGEM_ERRO) from erro

    if not math.isfinite(volume):
        raise ValueError(MENSAGEM_ERRO)
    if volume < 0 and volume != SENTINELA_ENCERRAMENTO:
        raise ValueError(MENSAGEM_ERRO)
    return volume


def processar_motor_coleta(
    limite_maximo: float = LIMITE_MAXIMO_M3,
    leitor: Callable[[str], str] = input,
    escritor: Callable[[str], None] = print,
) -> float:
    """Acumula volumes ate a sentinela ou o limite operacional.

    Entradas invalidas sao informadas e descartadas. O volume que alcanca ou
    ultrapassa o limite permanece no total para preservar o registro real da
    ultima cacamba recebida.
    """

    if not math.isfinite(limite_maximo) or limite_maximo <= 0:
        raise ValueError("O limite maximo deve ser um numero positivo e finito.")

    volume_acumulado = 0.0
    escritor("--- MOTOR OPERACIONAL DE COLETA (ADS) ---")

    while True:
        try:
            entrada = leitor("Digite o volume da cacamba (m³) ou -1 para encerrar: ")
        except EOFError:
            break

        try:
            volume = converter_volume(entrada)
        except ValueError:
            escritor(MENSAGEM_ERRO)
            continue

        if volume == SENTINELA_ENCERRAMENTO:
            break

        volume_acumulado += volume
        if volume_acumulado >= limite_maximo:
            escritor(STATUS_CAPACIDADE)
            break

    escritor(f"Volume Total: {volume_acumulado:g} m³")
    return volume_acumulado


if __name__ == "__main__":
    processar_motor_coleta()
