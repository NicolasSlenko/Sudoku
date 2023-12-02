import pygame, sys, sudoku_generator

import cell
from cell import Cell


def print_board(board,row_length,col_length):
  for row in range(row_length):
    for col in range(row_length):
      print(f"{board[row][col]} ", end="")
    print()
def start_menu(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return 1
                elif medium_rectangle.collidepoint(event.pos):
                    return 2
                elif hard_rectangle.collidepoint(event.pos):
                    return 3


        # Fill the background with white
        screen.fill((255, 255, 255))

        #Creates the fonts for the title and buttons
        title_font = pygame.font.Font(None, 100)
        button_font = pygame.font.Font(None, 50)

        #Renders in the title
        title_surface = title_font.render("Sudoku", 0, [0,0,0])
        title_rectangle = title_surface.get_rect(
            center=(300, 200))
        screen.blit(title_surface, title_rectangle)

        #Creating the buttons by first making the text for them
        easy_text = button_font.render('Easy',0, [255,255,255])
        medium_text = button_font.render('Medium', 0, [255,255,255])
        hard_text = button_font.render('Hard', 0, [255,255,255])

        easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
        easy_surface.fill([0,0,0])
        easy_surface.blit(easy_text, (10,10))

        medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
        medium_surface.fill([0, 0, 0])
        medium_surface.blit(medium_text, (10, 10))

        hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
        hard_surface.fill([0, 0, 0])
        hard_surface.blit(hard_text, (10, 10))

        easy_rectangle = easy_surface.get_rect(center=(150, 325))
        medium_rectangle = medium_surface.get_rect(center=(300, 325))
        hard_rectangle = hard_surface.get_rect(center=(450, 325))

        screen.blit(easy_surface, easy_rectangle)
        screen.blit(medium_surface, medium_rectangle)
        screen.blit(hard_surface, hard_rectangle)



        pygame.display.flip()

def generate_board(screen, user, cell_list):

        print(user)

        #Background color of board
        screen.fill((160,223,231))

        font = pygame.font.Font(None, 40)

        #Creates the border
        pygame.draw.line(screen, (0,0,0), (0,0), (600,0), width=10)
        pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, 600), width=10)
        pygame.draw.line(screen, (0, 0, 0), (0, 600), (600, 600), width=10)
        pygame.draw.line(screen, (0, 0, 0), (600, 0), (600, 600), width=12)

        #Creates horizontal dividers between squares
        pygame.draw.line(screen, (0, 0, 0), (0, 200), (600, 200), width=7)
        pygame.draw.line(screen, (0, 0, 0), (0, 400), (600, 400), width=7)
        pygame.draw.line(screen, (0, 0, 0), (0, 66), (600, 66), width=2)
        pygame.draw.line(screen, (0, 0, 0), (0, 132), (600, 132), width=2)
        pygame.draw.line(screen, (0, 0, 0), (0, 266), (600, 266), width=2)
        pygame.draw.line(screen, (0, 0, 0), (0, 332), (600, 332), width=2)
        pygame.draw.line(screen, (0, 0, 0), (0, 466), (600, 466), width=2)
        pygame.draw.line(screen, (0, 0, 0), (0, 532), (600, 532), width=2)


        #Creates vertical dividers between squares
        pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 600), width=7)
        pygame.draw.line(screen, (0, 0, 0), (400, 0), (400, 600), width=7)
        pygame.draw.line(screen, (0, 0, 0), (0, 400), (600, 400), width=7)
        pygame.draw.line(screen, (0, 0, 0), (66, 0), (66, 600), width=2)
        pygame.draw.line(screen, (0, 0, 0), (132, 0), (132, 600), width=2)
        pygame.draw.line(screen, (0, 0, 0), (266, 0), (266, 600), width=2)
        pygame.draw.line(screen, (0, 0, 0), (332, 0), (332, 600), width=2)
        pygame.draw.line(screen, (0, 0, 0), (466, 0), (466, 600), width=2)
        pygame.draw.line(screen, (0, 0, 0), (532, 0), (532, 600), width=2)

        #Fill the board with numbers depending on difficulty

        board_size = 9
        cell_size = 600 // board_size

        for x in cell_list:
            value = x.get_value()
            row, col = x.get_row(), x.get_col()

            text = font.render(str(value), 0, 'black')
            text_rect = text.get_rect(center=((col + 0.5) * cell_size, (row + 0.5) * cell_size))
            if value != 0:
                screen.blit(text, text_rect)

        return screen

def play_board(screen, cell_list):
    oldx = 0
    oldy = 0
    input_active = False
    input_text = ""
    selected_cell = None  # Variable to store the selected cell

    def check_if_done(cell_list):
        for cell in cell_list:
            if cell.value == 0:
                return False
        return True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0] // 66
                y = pos[1] // 66
                x1 = x
                y1 = y
                cell.unhighlight(screen, oldx, oldy)
                for z in cell_list:
                    if z.get_row() == y and z.get_col() == x:
                        z.highlight()
                        oldx = y
                        oldy = x
                        selected_cell = z  # Store the selected cell
                        input_active = True
                        break
                        # Check if the mouse click is within the exit button's rectangle
                if exit_rectangle.collidepoint(pos):
                    sys.exit()  # Exit the program

                if reset_rectangle.collidepoint(pos):
                    pass


            elif event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        # Handle Enter key to store the inputted number
                        try:
                            userInput = int(input_text)
                            print(userInput)
                            if 1 <= userInput <= 9:  # Check if the input is a valid number
                                if selected_cell.value == 0:
                                    selected_cell.displayfill(screen, button_font, userInput)
                                    if (check_if_done(cell_list)):
                                        # Initialize an empty 9x9 array
                                        final_board = [[0 for _ in range(9)] for _ in range(9)]

                                        # Fill in the final_board using the values from the cell_list
                                        for i in range(9):
                                            for j in range(9):
                                                final_board[i][j] = cell_list[i * 9 + j].value
                                        print_board(final_board,9,9)
                                        print("")
                                        print_board(solved_board,9,9)
                                        if final_board == solved_board:
                                            print("You Win!")
                                        else:
                                            print("You Lose!")
                                else:
                                    print("Cannot fill in already filled cell!")
                            else:
                                print("Invalid input. Please enter a number between 1 and 9.")
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                        input_text = ""  # Reset the input_text after storing the input
                        input_active = False  # Deactivate input mode
                    else:
                        # Handle other key presses to append characters to the input
                        input_text += event.unicode


        # Font for the buttons
        button_font = pygame.font.Font(None, 50)
        #Button creation
        reset_text = button_font.render('Reset', 0, [255, 255, 255])
        restart_text = button_font.render('Restart', 0, [255, 255, 255])
        exit_text = button_font.render('Exit', 0, [255, 255, 255])

        reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
        reset_surface.fill([0, 0, 0])
        reset_surface.blit(reset_text, (10, 10))

        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_surface.fill([0, 0, 0])
        restart_surface.blit(restart_text, (10, 10))

        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surface.fill([0, 0, 0])
        exit_surface.blit(exit_text, (10, 10))

        reset_rectangle = reset_surface.get_rect(center=(150, 650))
        restart_rectangle = restart_surface.get_rect(center=(310, 650))
        exit_rectangle = exit_surface.get_rect(center=(450, 650))

        screen.blit(reset_surface, reset_rectangle)
        screen.blit(restart_surface, restart_rectangle)
        screen.blit(exit_surface, exit_rectangle)

        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    start_screen = pygame.display.set_mode([600, 600])
    pygame.display.set_caption("Sudoku")
    user = start_menu(start_screen)
    cell_list = []

    board_screen = pygame.display.set_mode([600, 700])

    if user == 1: #change after to make removed: 30
        game_board, solved_board = sudoku_generator.generate_sudoku(9, 1)
        print_board(solved_board,9,9)
        for i in range(0,9):
            for j in range(0,9):
                c = Cell(game_board[i][j], i, j, board_screen)
                cell_list.append(c)
    elif user == 2:
        game_board, solved_board  = sudoku_generator.generate_sudoku(9,40)
        for i in range(0,9):
            for j in range(0,9):
                c = Cell(game_board[i][j], i, j, board_screen)
                cell_list.append(c)
    elif user == 3:
        game_board, solved_board = sudoku_generator.generate_sudoku(9, 50)
        for i in range(0,9):
            for j in range(0,9):
                c = Cell(game_board[i][j], i, j, board_screen)
                cell_list.append(c)


    board_screen = generate_board(board_screen, user, cell_list)
    user = play_board(board_screen, cell_list)





    while True:
        if user == 4:
            #Print original board removing user's inputs
            pass
        elif user == 5:
            #Restarts everything
            start_screen = pygame.display.set_mode([600, 600])
            user = start_menu(start_screen)
            board_screen = pygame.display.set_mode([600, 700])
            board_screen = generate_board(board_screen, user)
            user = play_board(board_screen)
        if user == 6:
            sys.exit()



