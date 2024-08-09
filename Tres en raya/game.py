from player import HumanPlayer, RandomComputerPlayer
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # Se usará una lista para representar el tablero de 3x3
        self.current_winner = None # Realizar un seguimiento del ganador


    def print_board(self):
        # Esto es para obtener las filas
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        
    @staticmethod

    def print_board_nums():
        # Esto nos dice que numero corresponde a cada caja 
        # 0 | 1 | 2
        number_board = [[str(i) for i in range (j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    # esto nos permirrá visualizar los movimientos dispobibles
    def available_moves(self):
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)

        return moves
    # Nos dice si hay un cuadro vacío o no
    def empty_squares(self):
        return ' ' in self.board
    # Nos devuelve el número de cuadros vacíos
    def num_empty_squares(self):
        return len(self.available_moves())
    
    # Esto nos permite realizar el movimiento

    def make_move(self, square, letter):
        # si el movimiento es valido, se hace el movimiento ( se asigna la letra al cuadro)
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # El ganador es el que hace 3 en raya
        # en las filas
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1)*3]

        if all([spot == letter for spot in row]):
            return True

        # en las columnas
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # en las diagonales

        if square % 2 == 0:
            diagonal_1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal_1]):
                return True
            diagonal_2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal_2]):
                return True

    
def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()

    letter  = 'X' # letra inicial

    # iterar mientras el juego tenga cuadros vacías

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' 7hace un movimiento al cuadro {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' gana!')
                return letter
        
        letter = 'O' if letter == 'X' else 'X'



    if print_game:
        print('Es un empate')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)


