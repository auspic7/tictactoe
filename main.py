import curses


class Game:
    def __init__(self):
        self.board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turn = 0

    def who_win(self):
        # horizontal win check func
        def row_check(board):
            for row in board:
                if row[0] == row[1] == row[2]:
                    return row[0]
            return 0

        # horizontal win
        win = row_check(self.board)
        if win != 0:
            return win

        # vertical win
        transposed = list(map(list, zip(*self.board)))
        win = row_check(transposed)
        return win

    def place(self, i, j, player):
        if not player == 1 or player == 2:
            return False
        if self.board[i][j] != 0:
            return False
        else:
            self.board = player
            return player

    def print(self):
        for row in self.board:
            pass
            # print


if __name__ == "__main__":
    game = Game()
    game.board = [[1, 0, 0], [1, 0, 0], [0, 0, 0]]

    print(game.who_win())
    print(game.print())