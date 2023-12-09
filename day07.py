import time
import numpy as np
import functools
import math
import copy

NUMBER_OF_CALLS = 0
LOG_FILE = open('logfile.txt', 'w')
DATA_CACHE = dict()
USED = []


REL_STRENGTH = {'2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 'T' : 10, 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}

class Hand:
    def __init__(self, cards : list, bid : int):
        self.bid = int(bid)
        self.cards = cards
        self.pval = 1
        cardset = set(cards)
        if len(cardset) == 1: # 'five of a kind'
            self.pval = 7
        elif len(cardset) == 2: # 'four of a kind' or 'full house'
            e = cardset.pop()
            if cards.count(e) == 4 or cards.count(e) == 1:
                self.pval = 6 # 'four of a kind'
            else:
                self.pval = 5 # 'full house'
        elif len(cardset) == 3: # 'three of a kind' or 'two pair'
            if cards.count(cards[0]) == 3 or cards.count(cards[1]) == 3 or cards.count(cards[2]) == 3:
                self.pval = 4 # 'three of a kind'
            else:
                self.pval = 3  # 'two pair'
        elif len(cardset) == 4: # ''pair'
            self.pval = 2
        else:
            pass


def compare_hands(h1, h2):
    if h1.pval > h2.pval:
        return 1
    if h2.pval > h1.pval:
        return -1
    for i in range(5):
        if REL_STRENGTH[h1.cards[i]] > REL_STRENGTH[h2.cards[i]]:
            return 1
        elif REL_STRENGTH[h2.cards[i]] > REL_STRENGTH[h1.cards[i]]:
            return -1
    return 0


def advent7_1():
    file = open('input07_example.txt')
    #file = open('input07.txt')

    hands = list()
    for line in file:
        row = line.strip('\n')
        hand, bid = row.split()
        hands.append(Hand(hand, bid))

    sorted_hands = sorted(hands, key = functools.cmp_to_key(compare_hands))
    sum = 0
    for h in range(len(sorted_hands)):
        #print(sorted_hands[h].cards, sorted_hands[h].pval)
        sum += (h + 1)*sorted_hands[h].bid

    print('Sum:', sum)


def apply_J(hand : Hand):
    if hand.pval == 7: # '5 of k'
        return
    nof_J = hand.cards.count('J')
    if nof_J == 0:
        return
    if hand.pval == 6: # '4 of k'
        hand.pval = 7
        return
    if hand.pval == 5: # 'full house'
        hand.pval = 7
        return
    if hand.pval == 4: # '3 of k'
        hand.pval = 6
        return
    if hand.pval == 3: # '2 pair'
        if nof_J == 2:
            hand.pval = 6
            return
        else:
            hand.pval = 5
            return
    if hand.pval == 2:
        hand.pval = 4
        return
    if hand.pval == 1:
        hand.pval = 2
        return

    
def advent7_2():
    REL_STRENGTH['J'] = 1
    #print(REL_STRENGTH)
    #file = open('input07_example.txt')
    file = open('input07.txt')

    hands = list()
    for line in file:
        row = line.strip('\n')
        hand, bid = row.split()
        hands.append(Hand(hand, bid))
        #print(hands[-1].pval)
        apply_J(hands[-1])

    sorted_hands = sorted(hands, key = functools.cmp_to_key(compare_hands))
    sum = 0
    for h in range(len(sorted_hands)):
        print(sorted_hands[h].cards, sorted_hands[h].pval)
        sum += (h + 1)*sorted_hands[h].bid

    print('Sum:', sum)

    
if __name__ == '__main__':

    start_time = time.time()
    print('Advent 7')
    advent7_1()
    advent7_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
