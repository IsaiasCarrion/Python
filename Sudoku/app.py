from http.client import OK

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]


class ValidateSudoku:
    def __init__(self, tablero) -> None:
        self.tablero = tablero
        self.lista_invertida = list()

    def chequeo_general(self):
        assert len(self.tablero) == 9, "El Tablero ingresado no respeta 9 x 9 "
        for fila in self.tablero:
            assert len(fila) == 9

    def chequeo_filas(self, lista_a_checkear='tablero_general'):
        if lista_a_checkear == 'tablero_general':
            lista_a_checkear = self.tablero
        for fila in lista_a_checkear:
            for elemento in fila:
                if elemento != '.':
                    assert fila.count(elemento) == 1

    def chequeo_columnas(self):
        for column_index in range(0, 9):
            for row_index in range(0, 9):
                self.lista_invertida.append(
                    self.tablero[row_index][column_index])
                self.chequeo_filas([self.lista_invertida])
                self.lista_invertida.clear()

    def chequeo_subcuadros(self):
        self.chequeo_3_subcuadros(0, 3)
        self.chequeo_3_subcuadros(3, 6)
        self.chequeo_3_subcuadros(6, 9)

    def chequeo_3_subcuadros(self, rango1, rango2):
        self.lista_invertida.clear()
        for column_index in range(0, 9):
            if column_index == 3 or column_index == 6:
                self.lista_invertida.clear()
            for row_index in range(rango1, rango2):
                self.lista_invertida.append(
                    self.tablero[row_index][column_index])
                if len(self.lista_invertida) == 9:
                    self.chequeo_filas([self.lista_invertida])


sudoku = ValidateSudoku(board)
sudoku.chequeo_general()
sudoku.chequeo_filas()
sudoku.chequeo_columnas()
sudoku.chequeo_subcuadros()
