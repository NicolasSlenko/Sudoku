import pygame
class Cell:
    #cell constructor
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.highlighted = False


    #setter and getter methods
    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    #highlight method
    def highlight(self):
        pygame.draw.line(self.screen, (255, 0, 0), (self.col * 66, self.row * 66), ((self.col + 1) * 66, self.row * 66), width=2)
        pygame.draw.line(self.screen, (255, 0, 0), (self.col * 66, self.row * 66), (self.col * 66, ((self.row + 1) * 66)), width=2)
        pygame.draw.line(self.screen, (255, 0, 0), (self.col * 66, ((self.row + 1) * 66)), ((self.col + 1) * 66, ((self.row + 1) * 66)), width=2)
        pygame.draw.line(self.screen, (255, 0, 0), ((self.col + 1) * 66, self.row * 66), ((self.col + 1) * 66, ((self.row + 1) * 66)), width=2)
        self.highlighted = True

    #display method and fill in board method
    def displayfill(self, screen, font, number):
        if self.highlight and self.value == 0:
            self.value = number
            self.render(screen, font)

    #method that puts input on screen (used to make red output)
    def render(self, screen, font):
        if self.value != 0:
            text = font.render(str(self.value), True, (255, 0, 0))
            text_rect = text.get_rect(center=((self.col + 0.5) * 66, (self.row + 0.5) * 66))
            screen.blit(text, text_rect)

    #method that puts renders and resets board (makes black output)
    def render_reset(self,screen,font):
        if self.value != 0:
            text = font.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect(center=((self.col + 0.5) * 66, (self.row + 0.5) * 66))
            screen.blit(text, text_rect)


#unhighlight method
def unhighlight(screen, row, col):
    pygame.draw.line(screen, (0,0,0), (col * 66, row * 66), ((col + 1) * 66, row * 66),
                         width=2)
    pygame.draw.line(screen, (0, 0, 0), (col * 66, row * 66),
                         (col * 66, ((row + 1) * 66)), width=2)
    pygame.draw.line(screen, (0, 0, 0), (col * 66, ((row + 1) * 66)),
                         ((col + 1) * 66, ((row + 1) * 66)), width=2)
    pygame.draw.line(screen, (0, 0, 0), ((col + 1) * 66, row * 66),
                         ((col + 1) * 66, ((row + 1) * 66)), width=2)


#return cell from cell_list method
def get_cell(row, col, cell_list):
    for cell in cell_list:
        if cell.row == row and cell.col == col:
            return cell

