import math
import random
class Player:
    def __init__(self, letter):
        # letter es X o O
        self.letter = letter

    def get_move(self, game):
        pass





class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        # Da un lugar random valido para el siguiente movimiento
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input('turno de' + self.letter + 'Movimiento de entrada (0-8): ')



            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True

            except ValueError:
                print('Cuadro inválido, intenta de nuevo :)')
        return val   