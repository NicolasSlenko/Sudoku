import pygame
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.highlighted = False


    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def draw(self):
        pass

    def draw_input(self, value):
        pass

    def highlight(self):
        pygame.draw.line(self.screen, (255, 0, 0), (self.col * 66, self.row * 66), ((self.col + 1) * 66, self.row * 66), width=2)
        pygame.draw.line(self.screen, (255, 0, 0), (self.col * 66, self.row * 66), (self.col * 66, ((self.row + 1) * 66)), width=2)
        pygame.draw.line(self.screen, (255, 0, 0), (self.col * 66, ((self.row + 1) * 66)), ((self.col + 1) * 66, ((self.row + 1) * 66)), width=2)
        pygame.draw.line(self.screen, (255, 0, 0), ((self.col + 1) * 66, self.row * 66), ((self.col + 1) * 66, ((self.row + 1) * 66)), width=2)
        self.highlighted = True

    def displayfill(self, screen, font, number):
        if self.highlight and self.value == 0:
            self.value = number
            self.render(screen, font)
    def render(self, screen, font):
        if self.value != 0:
            text = font.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect(center=((self.col + 0.5) * 66, (self.row + 0.5) * 66))
            screen.blit(text, text_rect)

    def get_value(self):
        return self.value

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

def unhighlight(screen, row, col):
    pygame.draw.line(screen, (0,0,0), (col * 66, row * 66), ((col + 1) * 66, row * 66),
                         width=2)
    pygame.draw.line(screen, (0, 0, 0), (col * 66, row * 66),
                         (col * 66, ((row + 1) * 66)), width=2)
    pygame.draw.line(screen, (0, 0, 0), (col * 66, ((row + 1) * 66)),
                         ((col + 1) * 66, ((row + 1) * 66)), width=2)
    pygame.draw.line(screen, (0, 0, 0), ((col + 1) * 66, row * 66),
                         ((col + 1) * 66, ((row + 1) * 66)), width=2)


def get_cell(row, col, cell_list):
    for cell in cell_list:
        if cell.row == row and cell.col == col:
            return cell

