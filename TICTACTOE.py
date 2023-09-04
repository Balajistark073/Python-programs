import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Tic-Tac-Toe")

# Define fonts
font = pygame.font.Font(None, 48)
menu_font = pygame.font.Font(None, 36)

# Define the board as a 3x3 array
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

# Define the players as X and O
players = ['X', 'O']
# ...

# Calculate the center of the Pygame window
window_center_x = screen.get_width() // 2
window_center_y = screen.get_height() // 2

# Define the size of the grid cells
cell_size = 100




# Choose the first player randomly
current_player = random.choice(players)

# Function to check for a winner
def check_winner(player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Display introduction and menu
def show_menu():
    intro_text = ["Welcome to Tic-Tac-Toe!", "",
                  "Press ENTER to start a new game.", "Press ESC to quit."]
    
    menu_surface = pygame.Surface((500, 500))
    menu_surface.fill(BLACK)
    
    for i, line in enumerate(intro_text):
        text = menu_font.render(line, True, WHITE)
        text_rect = text.get_rect(center=(250, 150 + i * 50))
        menu_surface.blit(text, text_rect)
    
    screen.blit(menu_surface, (0, 0))
    pygame.display.flip()
    
    waiting_for_start = True
    while waiting_for_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting_for_start = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

# Animation function when a player wins
def show_winner_animation(player):
    animation_speed = 10
    win_animation = pygame.Surface((500, 500))
    win_animation.set_alpha(0)
    
    for alpha in range(0, 255, animation_speed):
        win_animation.fill(BLACK)
        win_text = font.render(f"Player {player} wins!", True, WHITE)
        text_rect = win_text.get_rect(center=(250, 250))
        win_animation.blit(win_text, text_rect)
        win_animation.set_alpha(alpha)
        
        screen.blit(win_animation, (0, 0))
        pygame.display.flip()
        pygame.time.delay(50)
    
    pygame.time.delay(1000)

# Main game loop
show_menu()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = y // 100
            col = x // 100
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '-':
                board[row][col] = current_player
                if check_winner(current_player):
                    show_winner_animation(current_player)
                    # Reset the board
                    board = [['-', '-', '-'],
                             ['-', '-', '-'],
                             ['-', '-', '-']]
                else:
                    current_player = 'O' if current_player == 'X' else 'X'
    
    # Draw the board
    screen.fill(BLACK)
    board_top_left_x = window_center_x - (cell_size * 1.5)
    board_top_left_y = window_center_y - (cell_size * 1.5)
    for row in range(3):
        for col in range(3):
            pygame.draw.rect(screen, WHITE, (col * 100, row * 100, 100, 100), 2)
            text = font.render(board[row][col], True, WHITE)
            screen.blit(text, (col * 100 + 40, row * 100 + 40))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
