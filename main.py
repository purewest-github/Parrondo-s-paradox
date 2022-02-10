import random
import time

# ゲームの回数
counter = 0
# 所持金
pay = 100

# -------------------------------------------------
# ゲームAの設定
def game_a():
    challenge = random.randint(1, 100)
    global pay
    if challenge <= 48:
        pay += 1
    else:
        pay -= 1

# ゲームBの設定
def game_b():
    challenge = random.randint(1, 100)
    global pay
    if (pay % 3 ==0 and challenge == 100) or (pay % 3 !=0 and challenge <= 85):
        pay += 1           
    else:
        pay -= 1
    
# ゲームCの設定
def game_c():
    challenge = random.randint(1, 100)
    if challenge <= 50:
        game_a()
    else:
        game_b()
    
    
# -------------------------------------------------
# ゲームの実行
def play():
    print("回数", "    ", "所持金")
    while True:
        if pay <= 0 or pay >= 200:
            break
        else:
            global counter
            game_a()
            # game_b()
            # game_c()
            print("\r{0}       {1}".format(counter, pay), end="")
            time.sleep(0.001)
            counter += 1
        
play()
        