"""
Created on Tue Feb 12 

@author: Veronica Sakane

Description:
------------
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing num; for example, 134468.
Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.
Find the least number for which the proportion of bouncy numbers is exactly 99%.

https://repl.it/@vsakane/bounce
"""
from time import time

def bouncy(num):
    dec_seq = False
    inc_seq = False
    right_dig = num % 10
    num //= 10

    while num > 0:
        left_dig = num % 10
        if left_dig < right_dig: inc_seq = True
        elif left_dig > right_dig: dec_seq = True
        right_dig = left_dig
        num //= 10
        if inc_seq and dec_seq: return True
    return False


def main():
    start = time()
    count = 0
    num = 99
    while count < 0.99 * num:
        num += 1
        if bouncy(num): count += 1
    end = time()
    
    print(num)
    print(end-start)


if __name__ == "__main__":
    main()
