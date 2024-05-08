from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Juda baland son.")
        return turns - 1
    elif guess < answer:
        print("Juda kichik son.")
        return turns - 1
    else:
        print(f"Siz yutdingiz! Togri raqam {answer}.")                    

def set_difficulty():
    global turns  
    level = input("O'yin qiyinlik darajisini tanglang: (easy yoki hard) ")
    if level == 'easy':
        return EASY_LEVEL_TURNS 
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Raqam Tahmin qilish oyiniga hush kelibsiz!")
    print("1 dan 100 gacha raqamni oyladim.")

    answer = randint(1, 100)
    
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"Raqamni tahmin qilishingiz uchun sizda {turns} ta urushnish bor.")
        guess = int(input("Raqamni tahmin qiling: "))
        turns = check_answer(guess, answer, turns) 

        if turns == 0:
            print("Sizning tahmin qilish imkoniyatingiz tugadi. Siz yutqazdingiz.")
            return 
        elif guess != answer:
            print("Yana tahmin qiling.")

game()
