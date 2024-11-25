import time

class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['.']*3 for _ in range(3)]
        self.player_turn = 'X'
    
    def draw_board(self):
        for row in self.current_state:
            print(" | ".join(row))

    def is_valid(self,px,py):
        return 0 <= px <= 2 and 0 <= py <= 2 and self.current_state[px][py] == '.'

    
    def is_end(self):
        for i in range(3):
            if(self.current_state[0][i]!='.') and (self.current_state[0][i] == self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i] 
            
        for row in self.current_state:
            if row == ['X','X','X'] or row == ['O','O','O']:
                return row[0]
        
        if self.current_state[1][1] != '.':
            if ((self.current_state[0][0] == self.current_state[1][1] == self.current_state[2][2]) or 
                (self.current_state[0][2] == self.current_state[1][1] == self.current_state[2][0])):
                return self.current_state[1][1]
        
        if all([self.current_state[i][j] != '.' for i in range(3) for j in range(3)]):
            return 'patta'
        
        return None
    
    def min(self):
        return self.minimax(is_maximizing=False)
    
    def max(self):
        return self.minimax(is_maximizing=True)

    def minimax(self,alpha=-2,beta=2,is_maximizing=True):
        best_value = -2 if is_maximizing else 2
        px = None
        py = None
        result = self.is_end()  
        
        if(result == 'X'):
            return (1,0,0)
        if(result == 'O'):
            return (-1,0,0)
        if(result == 'patta'):
            return (0,0,0)
        
        for i in range(3):
            for j in range(3):
                if(self.current_state[i][j] == '.'):
                    self.current_state[i][j] = 'X' if is_maximizing else 'O'
                    value,qx,qy = self.minimax(alpha,beta,not(is_maximizing))
                    
                    if (value > best_value and is_maximizing) or (value < best_value and not is_maximizing):
                        px,py = i,j
                        best_value = value
                    self.current_state[i][j] = '.'

                    if (best_value > beta and is_maximizing) or (best_value < alpha and not is_maximizing):
                        return (best_value,px,py)
                    if (best_value > alpha and is_maximizing):
                        alpha = best_value
                    if (best_value < beta and not is_maximizing):
                        beta = best_value
                    
        return (best_value,px,py)       
                    
    def play(self):
        while True:
            self.draw_board()
            print()
            result = self.is_end()
            
            if(result is not None):
                if(result == 'X'):
                    print("Hai vinto")
                if(result == 'O'):
                    print("Hai perso")
                if(result == 'patta'):
                    print("Hai pareggiato!")
                return
                
            if(self.player_turn == 'X'):
    
                start = time.time()
                _,qx,qy = self.max()
                end = time.time()
                print(f"Tempo di Valutazione: {end-start} e Mossa Consigliata:[{qx},{qy}]")
                while True:
                    px = int(input("Inserisci riga:"))
                    py = int(input("Inserisci colonna:"))
                    
                    if(self.is_valid(px,py)):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    
                    print("Riprova")
            else:
                _,qx,qy = self.min()
                self.current_state[qx][qy] = 'O'
                self.player_turn = 'X'
    
gg = Game()
gg.play()            
                       
                  