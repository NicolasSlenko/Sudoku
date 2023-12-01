import pygame, sys
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

def generate_board(screen, user):

        print(user)

        #Background color of board
        screen.fill((160,223,231))



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

        if user == 1:
            #Generate easy board
            pass
        elif user == 2:
            #Generate medium board
            pass
        elif user == 3:
            #Generate hard board
            pass






        return screen

def play_board(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_rectangle.collidepoint(event.pos):
                    return 4
                elif restart_rectangle.collidepoint(event.pos):
                    return 5
                elif exit_rectangle.collidepoint(event.pos):
                    sys.exit()

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
    board_screen = pygame.display.set_mode([600, 700])
    board_screen = generate_board(board_screen, user)
    user = play_board(board_screen)


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




