
from game_data import data
from art import logo
from art import vs
import random


print(logo)

follower_user = 0
follower_compupter = 0
count = 0
game_over = True

while game_over:
    rando = random.randint(0,len(data))
    comp = random.randint(0,len(data))
    guess_a = data[rando]['follower_count']
    guess_b  = data[comp]['follower_count']
    print(f"Compare A: {data[rando]['name']}, a {data[rando]['description']}, from {data[rando]['country']}")
    print(vs)
    print(f"Against B: {data[comp]['name']}, a {data[comp]['description']}, from {data[comp]['country']}")
    guess = input("Who has more followers? Type 'A' or 'B' ")
    if guess == 'A':
        follower_user = guess_a
        follower_compupter = guess_b
    else:
        follower_compupter = guess_a
        follower_user = guess_b
    if follower_user > follower_compupter:
        print("you got it right")
        count +=1
        print(count)
    else:
        print(f"Sorry, that's wrong. Final score: {count}")
        game_over =False

    