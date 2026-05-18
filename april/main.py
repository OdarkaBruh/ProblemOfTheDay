#18.05.2026: DON'T GET THE TASK, thought you are allowed to use only numbers from this iteration ; - ;
def max_sum(n):
    if (n == 0) or (n == 1): return n
    result = max_sum(n // 2) + max_sum(n // 3) + max_sum(n // 4)
    return n if n > result else result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    max_sum(1200)