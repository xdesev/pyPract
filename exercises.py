from random import randrange
import requests
from bs4 import BeautifulSoup

"""
Solutions for excercies suggested by https://www.practicepython.org/
<Exercise #> - <Exercise name> <difficulty>
Some exercises include extra functonality, for further details visit practicepython.org
"""


def character_input():
    """Exercise 1 - Character Input *
    Create a program that asks the user to enter their name and their age.
    Print out a message addressed to them that tells them the year that they will turn 100 years old
    """
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    
    print("Your name is {name}".format(name=name))
    print("it will take you {age} years until you turn 100 years".format(age=100-age))


def odd_or_even():
    """Exercise 2 - Odd Or Even *
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate message to the user.
    Hint: how does an even / odd number react differently when divided by 2?
    """
    num = int(input("num1: "))

    if num % 4 == 0:
        print("multiple of 4")
    elif num % 2 == 0:
        print("even")
    else:
        print("odd")


def list_lest_than():
    """Exercise 3 - List Less Than Ten **
    Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    and write a program that prints out all the elements of the list that are less than 5.
    """
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    x = int(input("enter num: "))

    for val in a:
        if val < x:
            b.append(val)

    print(b)


def divisors():
    """Exercise 4 - Divisors **
    Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
    (If you dont know what a divisor is, it is a number that divides evenly into another number.
    """
    num = int(input("Enter a number to check: "))
    for x in range(1, int(num/2) + 1):
        if (num % x == 0):
            print(x)

def list_overlap():
    """Exercise 5 - List Overlap **
    Take two lists, and write a program that returns a list that contains only the elements
    that are common between the lists (without duplicates).
    Make sure your program works on two lists of different sizes.
    """
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    common_list = []

    for val in a:
        if val in b and val not in common_list:
            common_list.append(val)
    
    print(common_list)


def string_lists():
    """Exercise 6 - String Lists **
    Ask the user for a string and print out whether this string is a palindrome or not.
    (A palindrome is a string that reads the same forwards and backwards.)
    """
    txt_str = input("Enter a string to check if it is a palindrome: ")
    txt_pal_list = list(txt_str)
    txt_pal_list.reverse()
    txt_pal = "".join(txt_pal_list)
    
    if (txt_str == txt_pal):
        print("string entered is a palindrome!")
    else:
        print("string entered is not a palindrome")


def list_comprehensions():
    """Exercise 7 - List Comprehensions **
    Lets say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
    Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
    """
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [val for val in a if val % 2 == 0]
    print(b)


def rock_paper_scissor():
    """Exercise 8 - Rock Paper Scissors ***
    Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
    compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
    """
    games = int(input("Enter how many games do you want to play: "))
    print("Type s - for scissor, r - for rock, and p - for paper")
    p1_wins = 0
    p2_wins = 0

    for g in range(games):
        print("* * *   Game {game}  * * *".format(game=g + 1))
        
        while True:
            p1 = input("P1 move: ")
            p2 = input("P2 mvoe: ")

            if p1 == "r" or p1 == "p" or p1 == "s" \
                or p2 == "r" or p2 == "p" or p2 == "s":
                raise ValueError("Its required to enter r, p, s for p1 and p2 moves")
            
            if p1 == p2:
                continue

            if p1 == "s":
                if p2 == "r":
                    print("P2 wins!")
                    p2_wins = p2_wins + 1
                else:
                    print("P1 wins!")
                    p1_wins = p1_wins + 1
            elif p1 == "r":
                if p2 == "s":
                    print("P1 wins!")
                    p1_wins = p1_wins + 1
                else:
                    print("P2 wins!")
                    p2_wins = p2_wins + 1
            else:
                if p2 == "s":
                    print("P2 wins!")
                    p2_wins = p2_wins + 1
                else:
                    print("P1 wins!")
                    p1_wins = p1_wins + 1
            break

        games = games - 1
    
    print("Summary\nPlayer 1: {p1} wins\nPlayer 2: {p2} wins".format(p1=p1_wins, p2=p2_wins))


def divisors2(num):
    """Exercise 4 modified
    Returns a list containing all divisors of a number
    """
    return [n for n in range(1, int(num/2) + 1) if num % n == 0]


def check_primality_functions():
    """Exercise 11 - Check Primality Functions ***
    Ask the user for a number and determine whether the number is prime or not.
    (For those who have forgotten, a prime number is a number that has no divisors.).
    You can (and should!) use your answer to Exercise 4 to help you.
    Take this opportunity to practice using functions, described below.
    """
    num = int(input("Enter a number: "))
    divisors = divisors2(num)
    if len(divisors) == 1:
        print("{n} is a prime number".format(n=num))
    else:
        print("{n} is not a prime number".format(n=num))


def list_remove_duplicates():
    """Exercise 14 - List Remove Duplicates **
    Write a program (function!) that takes a list and returns a new list
    that contains all the elements of the first list minus all the duplicates.
    """
    my_list = [1, 2, 3, 4, 1, 2, 5]
    new_list = []

    for val in my_list:
        if val not in new_list:
            new_list.append(val)
    
    print("new_list", new_list)

    new_set = set(my_list)
    print("new_set", new_set)


def reverse_word_order():
    """Exercise 15 - Reverse Word Order ***
    Write a program (using functions!) that asks the user for a long string containing multiple words.
    Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
    My name is Michele
    Then I would see the string:
    Michele is name My
    """
    txt = "My name is Michele"
    txt_list = txt.split(" ")
    txt_list.reverse()

    print(*txt_list)
    
    new_txt = " ".join(txt_list)
    print(new_txt)


def decode_web_page():
    """Exercise 17 - Decode A Web Page ****
    Use the BeautifulSoup and requests Python packages to print out a list
    of all the article titleson the New York Times homepage.
    http://www.nytimes.com/
    """
    url = "http://www.nytimes.com/"
    r = requests.get(url)
    class_is_multi= { '*' : 'class'}
    soup = BeautifulSoup(r.text, "html.parser", multi_valued_attributes=class_is_multi)
    p_list = [p.text for p in soup.find_all('p') if "indicate-hover" in str(p)]
    titles = "\n".join(p_list)
    print(titles)


def cows_and_bulls():
    """Exercise 18 - Cows and Bulls ***
    Create a program that will play the "cows and bulls" game with the user. The game works like this:
    Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
    For every digit that the user guessed correctly in the correct place, they have a "cow".
    For every digit the user guessed correctly in the wrong place is a "bull."
    Every time the user makes a guess, tell them how many "cows" and "bulls" they have.
    Once the user guesses the correct number, the game is over.
    Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
    """
    random_num = randrange(10000)
    random_str = "{:04d}".format(random_num)
    tries_count = 0

    while True:
        guess_num = input("Enter your guess number: ")
        cows_count = 0
        bulls_count = 0
        tries_count += 1
        for n in range(4):
            if guess_num[n] == random_str[n]:
                cows_count += 1
            else:
                bulls_count += 1
        
        print("{cows} cows, {bulls} bulls".format(cows=cows_count, bulls=bulls_count))
        
        if (cows_count == 4):
            break
    
    print("You won in {tries} tries!".format(tries=tries_count))



def decode_web_page_two():
    """Exercise 19 - Decode A Web Page Two ****
    Using the requests and BeautifulSoup Python libraries,
    print to the screen the full text of the article on this website:
    http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
    The article is long, so it is split up between 4 pages.
    Your task is to print out the text to the screen so that you can read
    the full article without having to click any buttons.
    """
    url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    txt_list = [div.text for div in soup.find_all('div') if 'class' in div.attrs and 'article__body' in div['class']]
    file = open("article.txt", mode="w+", encoding="utf-8")
    file.write("\n".join(txt_list))
    file.close()
    print("article.txt was updated")


decode_web_page_two()