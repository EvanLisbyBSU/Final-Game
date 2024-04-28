# Burger Flap! A game made by Evan Lisby for CS 120


import pygame, random, simpleGE


class BurgerLad(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Burger Lad w Spatula.png")
        self.setSize(90, 60)
        self.position = (110, 200)
        self.movespeed = 10
        
    def process(self):
        if self.isKeyPressed(pygame.K_SPACE):
            self.addForce(3, 90)
        self.addForce(1.5, -90)
        self.setBoundAction(self.BOUNCE)
        

class Obstacles(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("gray70", (80, 300))
        self.position = (640, 0)    
        self.dx = -5
        
    def checkBounds(self):
        if self.x < 0:
            self.scene.obstacleReset()
            self.scene.incrementScore()
            
    def process(self):
        if self.collidesWith(self.scene.BurgerLad):
            self.scene.resetScore()
            self.scene.obstacleReset()
            self.scene.resetLad()
            
            
class Scorelbl(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (110, 50)
        
    def updateScore(self, score):
        self.score = score
        self.text = f"Score: {self.score}"
        
        
class highScorelbl(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "High Score: 0"
        self.center = (550, 50)
        
    def updateHighScore(self, highScore):
        self.highScore = highScore
        self.text = f"High Score: {self.highScore}"

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("wood panel background.jpg")
        self.BurgerLad = BurgerLad(self)
        self.Scorelbl = Scorelbl()
        self.highScorelbl = highScorelbl()
        self.topObstacle = Obstacles(self)
        self.bottomObstacle = Obstacles(self)
        self.safeArea = 475
        self.score = 0
        self.highScore = 0
        self.obstacleReset()
        self.sprites = [self.BurgerLad, self.topObstacle, self.bottomObstacle, self.Scorelbl, self.highScorelbl]
        
    def obstacleReset(self):
        self.topObstacleSpawnPlace = random.randint(-150, 150)
        self.bottomObstacleSpawnPlace = self.topObstacleSpawnPlace + self.safeArea
        self.topObstacle.position = (640, self.topObstacleSpawnPlace)
        self.bottomObstacle.position = (640, self.bottomObstacleSpawnPlace)

    def incrementScore(self):
        self.score += 1
        self.Scorelbl.updateScore(self.score)
        if self.score > self.highScore:
            self.highScore = self.score
            self.highScorelbl.updateHighScore(self.highScore)
            
    def resetScore(self):
        self.score = 0
        self.Scorelbl.text = "Score: 0"
        
    def resetLad(self):
        self.BurgerLad.position = (110, 200)
        self.BurgerLad.dy = 0
        
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()