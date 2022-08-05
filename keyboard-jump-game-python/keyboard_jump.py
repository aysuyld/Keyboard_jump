import pygame
import time
import random

pygame.init()#kütüphaneyi başlattık ve fonksiyonların çalışmasını sağladık.
#ekran boyutlarını ayarlama
WIDTH = 800
HEIGHT = 600
black = (0, 0, 0)

pygame.display.set_caption("Klavye Atlama")
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))#girmiş olduğumuz ekran değerlerini çalıştırdık. Aynı şeyi set_mode() ile de yapabilirdik.
background = pygame.image.load("keyback.jpg") 
background = pygame.transform.scale(background, (WIDTH,HEIGHT))
font = pygame.font.Font("comic.ttf", 40)

word_speed = 0.5
score = 0

def new_word():#word.txt den sözcükleri rastgele alır ve x, y konumlarını belirler
    global displayword, yourword, x_cor, y_cor, text, word_speed 
    x_cor = random.randint(300, 700)
    y_cor = 200
    word_speed += 0.10
    yourword = ""
    words = open("words.txt").read().split(", ")
    displayword = random.choice(words)
    
new_word()

font_name = pygame.font.match_font("comic.ttf")

def draw_text(display, text, size, x, y):#belirli bir yazı tipi ve boyutta metin çizmeye yardımcı olur
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)#belirtilen konumda görüntü çizmek veya metin yazmak için kullanılır
    
def game_front_screen():#ön oyun ekranını ve oyun ekran üzerinde görüntüler
    gameDisplay.blit(background, (0, 0))
    if not game_over:
        draw_text(gameDisplay, "Game Over", 90, WIDTH/2, HEIGHT/4)
        draw_text(gameDisplay, "Score: "+str(score), 70, WIDTH/2, HEIGHT/2)
    else:
        draw_text(gameDisplay, "Press any key to begin!", 54, WIDTH/2, 500)
    pygame.display.flip()#ekranın yalnızca bir bölümünü günceller, ancak hiçbir argüman girilmezse tüm ekranı günceller.
    waiting = True
    while waiting:
        for event in pygame.event.get():#olay kuyruğunda depolanan tüm olayları döndürür
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:#olayı klavyede bir tuşa basıldığında veya bırakıldığında meydana gelir.
                waiting = False
                
                
#main_loop

game_over = True
game_start = True
while True:
    if game_over:
        if game_start:
            game_front_screen()
        game_start = False
    game_over = False
        
    background = pygame.image.load('teacher-background.jpg')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    character = pygame.image.load('char.jpg')
    character = pygame.transform.scale(character, (50,50))
    wood = pygame.image.load('wood-.png')
    wood = pygame.transform.scale(wood, (90,50))
    gameDisplay.blit(background, (0,0))
    gameDisplay.blit(wood,(x_cor-50,y_cor+15))
    gameDisplay.blit(character,(x_cor-100, y_cor))
    draw_text(gameDisplay, str(displayword), 40, x_cor, y_cor)
    draw_text(gameDisplay, "Score: "+str(score), 40, WIDTH/2, 5)
        
    y_cor += word_speed
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            yourword += pygame.key.name(event.key)
                
            if displayword.startswith(yourword):
                if displayword == yourword:
                    score += len(displayword)
                    new_word()
                
            else:
                game_front_screen()
                time.sleep(3)
                pygame.quit()
            
    if y_cor < HEIGHT-5:
        pygame.display.update()
    else:
        game_front_screen()


























        
    