import time
import numpy as np
import math
import copy

NUMBER_OF_CALLS = 0
LOG_FILE = open('logfile.txt', 'w')
DATA_CACHE = dict()
USED = []


def advent4_1():
    #file = open('input04_examp.txt')
    file = open('input04.txt')
    sum = 0
    for line in file:
        row = line.strip('\n')
        numbers = row.split(': ')[1]
        winning = numbers.split(' | ')[0].split()
        my_nums = numbers.split(' | ')[1].split()
        #print('wins / my: ', winning, my_nums)
        card_sum = 0
        for num in my_nums:
            if num in winning:
                if card_sum == 0:
                    card_sum = 1
                else:
                    card_sum *= 2
        sum += card_sum

    print('Sum: ', sum)
        

class Card:
    """"""
    def __init__(self, number : int, winning : list, my_nums : list):
        self.number = number
        self.winning = winning
        self.my_nums = my_nums
        
    
def advent4_2():
    #file = open('input04_example.txt')
    file = open('input04.txt')
    sum = 0
    number = 0
    cards = list()
    for line in file:
        row = line.strip('\n')
        numbers = row.split(': ')[1]
        winning = numbers.split(' | ')[0].split()
        my_nums = numbers.split(' | ')[1].split()
        #print('wins / my: ', winning, my_nums)
        cards.append(Card(number, winning, my_nums))
        number += 1
    #print(cards)

    sum += len(cards)

    new_cards = list()
    for number in range(len(cards)):
        new_cards.append([])
        card_sum = 0
        for num in cards[number].my_nums:
            if num in cards[number].winning:
                card_sum += 1
        for i in range(number + 1, min(number + 1 + card_sum, len(cards))):
            #print('new card: ', i)
            new_cards[number].append(cards[i])
            sum += 1
        for card in new_cards[number]:
            card_sum = 0
            for num in card.my_nums:
                if num in card.winning:
                    card_sum += 1
            for i in range(card.number + 1, min(card.number + 1 + card_sum, len(cards))):
                new_cards[number].append(cards[i])
                #print('new card: ', i)
                sum += 1
            
    print('Sum :', sum)


    
if __name__ == '__main__':

    start_time = time.time()
    print('Advent 4')
    advent4_1()
    advent4_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
