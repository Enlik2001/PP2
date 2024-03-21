#ex1
def grams_to_ounces(grams):
    ounces = grams * 0.035274
    return ounces

#ex2
def C(F):
    C = (5/9) * (F - 32)
    return C

#ex3
def solve(numlegs, numheads):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
    return None

#ex4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

#ex5
from itertools import permutations
def string_permutations(input_str):
    return [''.join(p) for p in permutations(input_str)]

#ex6 
def reverse_words(input_str):
    words = input_str.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

#ex7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

#ex8 
def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

#ex9
def sphere_volume(radius):
    volume = (4 / 3) * 3.141592653589793 * (radius**3)
    return volume

#ex10
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

#ex11
def is_palindrome(word):
    return word == word[::-1]

#ex12
def histogram(numbers):
    for num in numbers:
        print('*' * num)

#ex13
import random
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    num = random.randint(1, 20)
    tries = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        tries += 1
        if guess < num:
            print("Your guess is too low.")
        elif guess > num:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {tries} guesses!")
            break

#ex14
from Functions import (
    ounces, 
    c,
    solve,
    is_prime,
    filter_prime,
    string_permutations,
    reverse_words,
    has_33,
    spy_game,
    sphere_volume,
    unique_elements,
    is_palindrome,
    histogram,
    guess_the_number
)