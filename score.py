from turtle import Turtle, Screen


ALIGNMENT = "left"
FONT = ("Courier", 18, "normal")
screen = Screen()


with open("highscore.txt", "w+") as highscore_file:
    HIGHSCORE = highscore_file.read()
    print(HIGHSCORE)
    if HIGHSCORE == "":
        HIGHSCORE = "0"
    else:
        HIGHSCORE = HIGHSCORE


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore = HIGHSCORE
        self.clear()
        self.hideturtle()
        self.score = 0
        self.goto(-60, 270)
        self.color('white')
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.penup()

    def high_score_update(self):
        with open("highscore.txt", "w+") as highscore_file:
            highscore_file.write(self.highscore)

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
            self.clear()
            screen.clear()
            screen.bgcolor('black')
            self.goto(-70, 0)
            self.write(f"Game Over!", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = str(self.score)
            print(self.highscore)
        self.score = 0
        self.score_update()
        self.high_score_update()
