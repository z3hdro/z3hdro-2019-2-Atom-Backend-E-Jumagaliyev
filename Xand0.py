class game:
    def __init__(self):
        self.game_map = [
            '   |   |   ',
            ' 1 | 2 | 3 ',
            '___|___|___',
            '   |   |   ',
            ' 4 | 5 | 6 ',
            '___|___|___',
            '   |   |   ',
            ' 7 | 8 | 9 ',
            '   |   |   '
        ]

        self.position = {
            '1': [1, 1],
            '2': [1, 5],
            '3': [1, 9],
            '4': [4, 1],
            '5': [4, 5],
            '6': [4, 9],
            '7': [7, 1],
            '8': [7, 5],
            '9': [7, 9]
        }
        self.crosses = []
        self.zeroes = []
        self.counter = 0
        self.arr = [i for i in range(1, 10)]

        self.game_win_comb = [
            [1, 2, 3], [4, 5, 6],
            [7, 8, 9], [1, 5, 9],
            [3, 5, 7], [1, 4, 7],
            [2, 5, 8], [3, 6, 9]
            ]

    def start(self):
        print('Welcome', end='\n\n')
        print(self.print_game())
        print('This is the game map')
        print('the number on the gameboard shows the position of your input ')
        print('\n\n')
        print('The 1st player will start with crosses')
        print('The 2nd player will play with zeroes', end='\n\n')
        while not self.victory():
            try:
                pos = int(input('Select a number from 1-9 to put X or 0: '))
                print('\n')
                self.turn(pos)
                if self.draw() is True:
                    break
            except ValueError:
                print('\n')
                print('INPUT a number from 1-9', end='\n\n')
            except Exception:
                print('Choose another cell from remaining', end='\n')
                print('or', end='\n')
                print('INPUT a number from 1-9', end='\n')
                print('\n\n\n')

    def print_game(self):
        for row in self.game_map:
            print(row)
        return ''

    def write_symbol(self, input, turn):
        tmp = self.position.get(str(input))
        i = tmp[0]
        if turn == 'x':
            self.crosses.append(input)
            self.game_map[i] = self.game_map[i].replace(str(input), turn)
            return self.print_game()
        elif turn == '0':
            self.zeroes.append(input)
            self.game_map[i] = self.game_map[i].replace(str(input), turn)
            return self.print_game()

    def draw(self):
        if self.counter == 9 and self.victory() is False:
            print('DRAW')
            return True

    def turn(self, position):
        pos = int(position)
        if pos not in self.arr or pos < 1 or pos > 9:
            raise Exception
        if self.counter % 2 == 0 and pos in self.arr:
            self.arr.remove(pos)
            self.write_symbol(pos, 'x')
            print('Cross was put', end='\n')
        elif self.counter % 2 != 0 and pos in self.arr:
            self.arr.remove(pos)
            self.write_symbol(pos, '0')
            print('Zero was put', end='\n')
        self.counter += 1
        print('_____________________ step {}'.format(self.counter), end='\n\n')

    def victory(self):
        for combo in self.game_win_comb:
            if all(pos in self.crosses for pos in combo):
                print('X won! CONGRATULATIONS!!!!!')
                return True
            if all(pos in self.zeroes for pos in combo):
                print('0 won! CONGRATULATIONS!!!!!')
                return True
        return False
