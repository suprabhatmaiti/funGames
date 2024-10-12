import tkinter
import pygame

def play_game_over_sound():
    play=pygame.mixer.Sound("resources/gameOver.mp3")
    pygame.mixer.Sound.play(play)

def set_tile(row,column):
    global curr_player
    
    if(game_over):
        return
    
    if board[row][column]["text"] !="":
        return
    board[row][column]["text"]=curr_player
    play=pygame.mixer.Sound("resources/buttonClick.mp3")
    pygame.mixer.Sound.play(play)
    if curr_player==playerO:
        curr_player=playerX
    else:
        curr_player=playerO
        
    label["text"]=curr_player+"'s turn"
    check_winner()
    
def check_winner():
    global turns
    global game_over
    turns=turns+1
    
    for row in range(3):
        if(board[row][0]["text"]==board[row][1]["text"]==board[row][2]["text"] and board[row][0]["text"]!=""):
            label.config(text=board[row][0]["text"]+" wins",foreground="yellow")
            for column in range(3):
                board[row][column].config(foreground="yellow")
            game_over=True
            play_game_over_sound()
            return
    
    
    for col in range(3):
        if(board[0][col]["text"]==board[1][col]["text"]==board[2][col]["text"] and board[0][col]["text"]!=""):
            label.config(text=board[0][col]["text"]+" wins",foreground="yellow")
            for row in range(3):
                board[row][col].config(foreground="yellow")
            game_over=True
            play_game_over_sound()
            return
    
    if(board[0][0]["text"]==board[1][1]["text"]==board[2][2]["text"] and board[0][0]["text"]!=""):
            label.config(text=board[0][0]["text"]+" wins",foreground="yellow")
            
            for i in range(3):
                board[i][i].config(foreground="yellow")
            game_over=True
            play_game_over_sound()
            return  
        
    if(board[0][2]["text"]==board[1][1]["text"]==board[2][0]["text"] and board[1][1]["text"]!=""):
            label.config(text=board[0][2]["text"]+" wins",foreground="yellow")
            
            for i in range(3):
                board[i][2-i].config(foreground="yellow")
            
            game_over=True
            play_game_over_sound()
            return  

    if(turns==9):
        game_over=True
        label.config(text="Its a Tie",foreground="yellow")
    
def new_game():
    global turns,game_over
    
    turns=0
    game_over=False
    label["text"]=curr_player+"'s turn"
    label.config(foreground="white")
    for row in range(3):
        for col in range(3):
            board[row][col].config(text="",background="gray",foreground="blue")
            
    
pygame.mixer.init()
playerX='X'
playerO='O'
curr_player=playerX
board =[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

turns=0
game_over=False

window=tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False,False)

frame=tkinter.Frame(window)
label=tkinter.Label(frame,text=curr_player+"'s turn",font=("Consolas",20),background="gray",
                    foreground="white")

label.grid(row=0,column=0,columnspan=3,sticky="we")

for row in range(3):
    for col in range(3):
        board[row][col]=tkinter.Button(frame,text="",background="gray",font=("Consolas",50,"bold"),
                                       foreground="blue",width="4",height=1
                                       ,command=lambda row=row,column=col:set_tile(row,column) )
        board[row][col].grid(row=row+1,column=col)

button=tkinter.Button(frame,text="restart",font=("Consolas",20),background="gray",foreground="white",
                      command=new_game)

button.grid(row=4,column=0,columnspan=3,sticky="we")

frame.pack()
window.mainloop()