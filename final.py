
from game_data import data
from art import logo, vs
import random
# Format the account data
def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = data[account]['name']
    account_descr = data[account]['description']
    account_country = data[account]['country']
    return f"{account_name}, a {account_descr}, from {account_country }"

def chec_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess =='a'
    else:
        return guess == 'b'

score =0
game_should_continue = True
account_b = random.randint(0,len(data))


# Make the game repeatable
while game_should_continue:
    # Generate a random account from the game data
    # Making account at position B become the next account at position A
    account_a = account_b
    account_b = random.randint(0,len(data))
    while account_a == account_b:
        account_b = random.randint(0,len(data))
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # ask a user for a guess
    guess = input("Who has more followers? Type 'A' or 'B' ").lower()
    # check if user is correct
    # Get follower count of each account
    a_follower_count = data[account_a]['follower_count']
    b_follower_count = data[account_b]['follower_count']

    is_correct = chec_answer(guess, a_follower_count, b_follower_count)

    # clear the screen

    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        score +=1
        print(f"you are right {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that was the wrong asnwer and your final score: {score}")

