# 18.05.2026: DON'T GET THE TASK, thought you are allowed to use only numbers from this iteration ; - ;
def max_sum(n):
    if (n == 0) or (n == 1): return n
    result = max_sum(n // 2) + max_sum(n // 3) + max_sum(n // 4)
    return n if n > result else result


# 17.05.2026 - done 18.05 (Make the array beautiful)
def makeBeautiful(arr: list[int]) -> list[int]:
    def compare(n1, n2):
        if (n1 == 0 and n2 < 0) or (n2 == 0 and n1 < 0): return False
        return n1 * n2 > 0


    i = 0
    while i+1 < len(arr):
        if len(arr) < 2: return arr
        elif compare(arr[i], arr[i+1]) == False:
            del arr[i]
            del arr[i]
            if (i > 0): i = i-1
        else:
            i = i + 1
    return arr


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # max_sum(1200)
    #print("Result: ", makeBeautiful([-1, 32]))