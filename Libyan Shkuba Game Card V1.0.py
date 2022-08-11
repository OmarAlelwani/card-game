from random import shuffle, choice
# variables #
p1_hand = []
p1_waklat = []
p1_score = 0
p1_shkubat = []

p2_hand = []
p2_waklat = []
p2_score = 0
p2_shkubat = []

deck = ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10',
        'p1','p2','d3','d4','d5','d6','d7','d8','d9','p10',
        'h1','h2','h3','h4','h5','h6','h7','h8','h9','h10',
        'c1','c2','c3','c4','c5','c6','c7','c8','c9','c10']
floor = []
first_to_play = "P1"
last_eaten_player = None
shoot = 0
turn = 0
last_player_with_higher_score = "none"
# functions #

def shuffle_deck():
     shuffle(deck)

def decide_who_plays_first():
    global shoot
    global first_to_play
    if shoot == 0:
        first_to_play = choice(["P1","P2"])
    elif shoot != 0:
        if p1_score == p2_score:
            if last_player_with_higher_score== "P1":
                first_to_play = "P1"
            else: first_to_play = "P2"
        elif p1_score > p2_score:
            first_to_play = "P1"
        else: irst_to_play = "P2"
    return first_to_play

def print_board():
     print("player 2: ",p2_hand)
     print()
     print("    ",floor)
     print()
     print("player 1: ",p1_hand)

def card_dist_for_first_turn():
    p1_hand.append(deck.pop(0))
    print(p1_hand)

    c = input("do u want to keep it(yes or no): ")
    if c == "yes":
        for i in range(2):
            p1_hand.append(deck.pop(0))
        for i in range(3):
            p2_hand.append(deck.pop(0))
        for i in range(4):
            floor.append(deck.pop(0))
            
    elif c == "no":
        floor.append(p1_hand.pop(0))
        
        for i in range(3):
            floor.append(deck.pop(0))
        for i in range(3):
            p1_hand.append(deck.pop(0))
        for i in range(3):
            p2_hand.append(deck.pop(0))
	
def card_dist_for_normal_turn():
    for i in range(3):
        p1_hand.append(deck.pop(0))
    for i in range(3):
        p2_hand.append(deck.pop(0))


def card_dist():
    if turn == 0: card_dist_for_first_turn()
    else: card_dist_for_normal_turn()
    
def calculate_score():
    global p1_waklat
    global p2_waklat
    global p1_shkubat
    global p2_shkubal
    global p1_score
    global p2_score
    win_condition = 61
    p1_dinari = 0
    p2_dinari = 0
    num_of_7 = 0
    num_of_6 = 0
    while True:
    #----Calculate How Many Dinari's Each Player Has-------#
        for i in p1_waklat:
            if i[0] == "d":
                p1_dinari += 1
        p2_dinari = abs(10 - p1_dinari)
        #-------Dinari Special Cases Calculation------#
        if p1_dinari == 8:
            p1_score += 10
            break
        elif p1_dinari == 9:
            p2_score = 0
            break
        elif p1_dinari == 10:
            p1_score, p2_score = True, False
            break
        elif p2_dinari == 8:
            p2_score += 10
            break
        elif p2_dinari == 9:
            p1_score = 0
            break
        elif p2_dinari == 10:
            p1_score, p2_score = False, True
            break
        #---------Dinar Normal Cases Calculation--------#
        else:
            if p1_dinari > p2_dinari:
                p1_score += 1
            elif p2_dinari > p1_dinari:
                p2_score += 1
        #-------- Shkuba Cases------#
        for i in p1_shkubat:
            if len(i) == 3:
                p1_score += 10
            else:
                p1_score += int(i[1])
                
        for i in p2_shkubat:
            if len(i) == 3:
                p2_score += 10
            else:
                p2_score += int(i[1])
                
        #----------Normal Cases(1)Card Numbers--------#
        if len(p1) > len(p2):
            p1_score += 1
        elif len(p1) < len(p2):
            p2_score += 1
        #---------Normal Cases(2)7 Of Diamond------#
        if "d7" in p1_waklat:
            p1_score += 1
        else: p2_score +=1
        #-------------Normal Cases(3)Number of 7's-----#
        for i in p1_waklat:
            if i[1] == "7":
                num_of_7 += 1
            if i[1] == "6":
                num_of_6 += 1
        if num_of_7 > 2:
            p1_score += 1
        elif num_of_7 < 2:
            p2_score += 1
        else:
            if num_of_6 > 2:
                p1_score += 1
            if num_of_6 < 2:
                p2_score += 1
            else: pass
        break
    #------------Win Condition-------#
    while True:
        if p1_score >= win_condition and p2_score >= win_condition:
            win_condition += 10
        else: break
    if p1_score >= win_condition:
        p1_score, p2_score = True, False
    elif p2_score >= win_condition:
        p1_score, p2_score = False, True
    #------------Return Score---------#
    return p1_score, p2_score


def play_a_turn():
    
    while True:
        played_card = input("player 1 turn ## enter the card you want to play: ")
        if played_card in p1_hand:
            break
        else: print("invalid input")
     
     
    wanted_cards = input("enter the cards you want to eat: ").split()
    print(wanted_cards)
          
    target = 0
    for i in wanted_cards:
        target += int(i[1:])

     
    if int(played_card[1:]) == target:
          if len(wanted_cards) == len(floor):
               p1_score += target
               print("nice shkoba!!")
          

               p1_waklat.append(p1_hand.pop(p1_hand.index(played_card)))
               for i in wanted_cards:
                    p1_waklat.append(floor.pop(floor.index(i)))
      
          else:
               p1_waklat.append(p1_hand.pop(p1_hand.index(played_card)))
               for i in wanted_cards:
                    p1_waklat.append(floor.pop(floor.index(i)))
    else:
          floor.append(p1_hand.pop(p1_hand.index(played_card)))
          

    print_board() 

    while True:
        played_card = input("player 2 turn ## enter the card you want to play: ")
        if played_card in p2_hand:
            break
        else: print("invalid input")
     
     
    wanted_cards = input("enter the cards you want to eat: ").split()
    print(wanted_cards)
          
    target = 0
    for i in wanted_cards:
        target += int(i[1:])

     
    if int(played_card[1:]) == target:
          print("nice")
          if len(wanted_cards) == len(floor):
               p2_score += target
               print("nice shkoba!!")

               p2_waklat.append(p2_hand.pop(p2_hand.index(played_card)))
               for i in wanted_cards:
                    p2_waklat.append(floor.pop(floor.index(i)))
          else:
               p2_waklat.append(p2_hand.pop(p2_hand.index(played_card)))
               for i in wanted_cards:
                    p2_waklat.append(floor.pop(floor.index(i)))

    else:
          floor.append(p2_hand.pop(p2_hand.index(played_card)))

def check_if_there_is_a_winner():
    
    if p1_score == True:
         print("player 1 has won")
         return True
    elif p2_score == True:
        print("player 2 has won")
        return True


def reset_values():
    deck = ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10',
            'p1','p2','d3','d4','d5','d6','d7','d8','d9','p10',
            'h1','h2','h3','h4','h5','h6','h7','h8','h9','h10',
            'c1','c2','c3','c4','c5','c6','c7','c8','c9','c10']
    
    p1_hand = []
    p1_waklat = []
    p1_shkubat = []

    p2_hand = []
    p2_waklat = []
    p2_shkubat = []

    floor = []
    turn = 0

def run_game():
    while check_if_there_is_a_winner() != True:
        global turn
        global shoot
        shuffle_deck()
        for i in range(6): 
             card_dist()
             turn += 1 
             for i in range(3):
                print_board()
                play_a_turn()
        
        calculate_score()
        shoot += 1
        reset_values()

run_game()
