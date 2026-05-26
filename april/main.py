# 18.05.2026: DON'T GET THE TASK, thought you are allowed to use only numbers from this iteration ; - ;
import array
from os import remove
from tabnanny import check


def max_sum(n):
    if (n == 0) or (n == 1): return n
    result = max_sum(n // 2) + max_sum(n // 3) + max_sum(n // 4)
    return n if n > result else result


# 17.05.2026 - done 18.05 (Make the array beautiful)
def make_beautiful(arr: list[int]) -> list[int]:
    def compare(n1, n2):
        if (n1 == 0 and n2 < 0) or (n2 == 0 and n1 < 0): return False
        return n1 * n2 > 0

    i = 0
    while i + 1 < len(arr):
        if len(arr) < 2:
            return arr
        elif not compare(arr[i], arr[i + 1]):
            del arr[i]
            del arr[i]
            if i > 0: i = i - 1
        else:
            i = i + 1
    return arr


# 25.05
def ranged_arr(start, end, arr):
    for n in range(start, end + 1):
        if n not in arr: return False
    return True


"""
    [25.05.2026] - Last Coin in a Game of Alternates 
https://www.geeksforgeeks.org/problems/last-coin-in-a-game-of-alternates

Players take turns removing the coins at the ends of the stack. Each player takes the coin with the highest value.

Personal note: simpler methods to solve exist, but then it fails time limit ; - ;
"""


def coin(arr):
    length = len(arr)
    if length < 2: return arr[0]

    start = arr[0]
    end = arr[-1]

    while length != 1:
        if start > end:
            arr.pop(0)
            start = arr[0]
        else:
            arr.pop(-1)
            end = arr[-1]
        length = length - 1
    return arr[0]

"""
    [26.05.2026] - Minimum Toggle to Partition
Personal note: suffered so much with this one.

"""
def minToggle(arr):
    one = 0
    toggle = 0
    for n in arr:
        one += n
        toggle = min(toggle - n + 1, one)
    return toggle


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # ranged_arr(2, 5, [1, 4, 5, 2, 7, 8, 3])
    # max_sum(1200)
    # print("Result: ", makeBeautiful([-1, 32]))
    # coin([1, 4, 5, 4, 2, 7, 8, 3])
    print("Result: ", minToggle([1, 0, 0, 0, 0, 1, 1, 1, 1]))
