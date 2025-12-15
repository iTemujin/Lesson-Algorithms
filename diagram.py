from threading import Thread
import pygame

class Dia(Thread):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((2500, 1000))
        self.clock = pygame.time.Clock()
        self.running = True

        self.array = []
        
        self.h_screen = self.screen.get_height()
        self.w_screen = self.screen.get_width()



    def run(self, EZ):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running =  False
            
            self.screen.fill((255,255,255))

            try:
                mami = EZ.getThat()
                for index, value in enumerate(mami):
                    pygame.draw.rect(self.screen, (0,255,0), ((t)*index, 0, t+1, value*self.h_screen/len(self.array)))
            except:
                None


            self.array = EZ.get()
            t = self.w_screen/(len(self.array))
            self.atlag = len(self.array)//self.w_screen

            value = 0
            mozog = 0
            for index in range(len(self.array)):
                value += self.array[index]
                if index% self.atlag == 0:
                    mozog += 1
                    pygame.draw.rect(self.screen, (0,0,0), (mozog+t, 0, t+1, value*self.h_screen/len(self.array)/(len(self.array)/self.h_screen)))
                    value = 0


            pygame.display.flip()

            self.clock.tick(1)

        pygame.quit()

