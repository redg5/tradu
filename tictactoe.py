#!/usr/bin/env python3
"""Juego de Tic Tac Toe (Tres en raya) en consola para 2 jugadores."""


def imprimir_tablero(tablero: list[str]) -> None:
    """Muestra el tablero con posiciones o fichas."""
    celdas = [tablero[i] if tablero[i] != " " else str(i + 1) for i in range(9)]
    print()
    print(f" {celdas[0]} | {celdas[1]} | {celdas[2]}")
    print("---+---+---")
    print(f" {celdas[3]} | {celdas[4]} | {celdas[5]}")
    print("---+---+---")
    print(f" {celdas[6]} | {celdas[7]} | {celdas[8]}")
    print()


def hay_ganador(tablero: list[str], jugador: str) -> bool:
    """Verifica si el jugador ganó."""
    combinaciones = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    return any(all(tablero[i] == jugador for i in linea) for linea in combinaciones)


def tablero_lleno(tablero: list[str]) -> bool:
    """Devuelve True si ya no hay espacios libres."""
    return all(celda != " " for celda in tablero)


def pedir_movimiento(tablero: list[str], jugador: str) -> int:
    """Solicita un movimiento válido y devuelve el índice de celda."""
    while True:
        entrada = input(f"Turno de {jugador}. Elige una posición (1-9): ").strip()

        if not entrada.isdigit():
            print("Entrada inválida. Escribe un número del 1 al 9.")
            continue

        posicion = int(entrada)
        if posicion < 1 or posicion > 9:
            print("Posición fuera de rango. Debe ser del 1 al 9.")
            continue

        indice = posicion - 1
        if tablero[indice] != " ":
            print("Esa casilla ya está ocupada. Elige otra.")
            continue

        return indice


def jugar() -> None:
    """Bucle principal del juego."""
    print("=== Tic Tac Toe / Tres en raya ===")
    print("Jugadores: X y O")

    while True:
        tablero = [" "] * 9
        jugador_actual = "X"

        while True:
            imprimir_tablero(tablero)
            movimiento = pedir_movimiento(tablero, jugador_actual)
            tablero[movimiento] = jugador_actual

            if hay_ganador(tablero, jugador_actual):
                imprimir_tablero(tablero)
                print(f"¡{jugador_actual} gana! 🎉")
                break

            if tablero_lleno(tablero):
                imprimir_tablero(tablero)
                print("Empate 🤝")
                break

            jugador_actual = "O" if jugador_actual == "X" else "X"

        otra = input("¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if otra not in {"s", "si", "sí", "y", "yes"}:
            print("Gracias por jugar.")
            return


if __name__ == "__main__":
    jugar()
