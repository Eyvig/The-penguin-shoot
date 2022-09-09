class Stats():

    def __init__(self):
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        self.penguins_left = 3
        self.score = 0

