import pygame as py
import math
import threading
import random as rd

py.init()

# Set up the display
screen_width, screen_height = 1000, 1000
screen = py.display.set_mode((screen_width, screen_height), )
py.display.set_caption("Falling Sand")

class cell():
    def __init__(self, coords, state=False):
        self.coords = coords
        self.size = 10
        self.state = state
        self.rect = py.Rect(coords[0], coords[1], self.size, self.size)
        self.rand_r = rd.randint(120, 255)
        self.rand_g = rd.randint(120, 255)
        self.rand_b = rd.randint(120, 255)
    
    def __str__(self):
        return str(self.rect)
    
    def get_state(self):
        return self.state
    
    def draw(self):
        if self.state:
            py.draw.rect(screen, (self.rand_r, self.rand_g, self.rand_b), self.rect)
        else:
            py.draw.rect(screen, (20, 20, 20), self.rect, width=1)
    
    def get_coords(self):
        return self.coords
    
    def toggle(self):
        self.state = not self.state
    
    def on(self):
        self.state = True
    def off(self):
        self.state = False

    

class display():
    def __init__(self):
        self.size = screen_width // 10
        self.board = [[cell((x*10, y*10)) for y in range(self.size)] for x in range(self.size)]
        self.lock = threading.Lock()
        self.running = True
        self.fall_thread = threading.Thread(target=self.fall_sand)
        self.fall_thread.start()

    def draw(self):
        for x in range(self.size):
            for y in range(self.size):
                c = self.board[x][y]
                c.draw()

    def board_toggle(self, mouse_pos):
        pos = math.floor(mouse_pos[0] / 10), math.floor(mouse_pos[1] / 10)
        if 0 < pos[0] < self.size-1 and 0 < pos[1] < self.size-1:
            with self.lock:
                # Brush
                for i in range(-1, 2, 1):
                    self.board[pos[0]][pos[1]+i].on()
                    self.board[pos[0]+i][pos[1]].on()

    def fall_sand(self):
        while self.running:
            with self.lock:
                for x in range(self.size):
                    for y in range(self.size - 1, -1, -1):
                        c = self.board[x][y]
                        self.update(c, (x, y))
            py.time.delay(5) 
    
    def update(self, c, pos):
        if pos[1] + 1 < self.size:
            below_c = self.board[pos[0]][pos[1] + 1]
            if c.get_state() and not below_c.get_state():
                c.toggle()
                self.board[pos[0]][pos[1] + 1].on()
            elif c.get_state() and below_c.get_state():
                if pos[1] < self.size-2 and 0< pos[0] < self.size - 1:
                    below_left = self.board[pos[0] -1][pos[1] + 2]
                    below_right = self.board[pos[0] +1][pos[1] + 2]
                    left = self.board[pos[0] -1][pos[1]]
                    right = self.board[pos[0] +1][pos[1]]
                    if not below_left.get_state():
                        c.off()
                        left.on()
                    if not below_right.get_state():
                        c.off()
                        right.on()

    def stop(self):
        self.running = False
        self.fall_thread.join()

def main():
    clock = py.time.Clock()

    board = display()

    mouse_down = False
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            elif event.type == py.MOUSEBUTTONDOWN:
                mouse_down = True
            elif event.type == py.MOUSEBUTTONUP:
                mouse_down = False
        if mouse_down:
            mouse_pos = py.mouse.get_pos()
            board.board_toggle(mouse_pos)

        board.draw()

        py.display.flip()
        clock.tick(120)

    board.stop()  # Stop the falling sand thread
    py.quit()



if __name__ == "__main__":
    main()


