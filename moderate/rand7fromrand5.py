import random
def rand5():
    return random.randint(0,4)

def rand7Fromrand5():
    """
    Generate a random number between 0 and 6 (inclusive)
    :return:
    """
    while True :
        num = 5*rand5()+rand5()
        if num < 21 :
            return num%7

if __name__ == "__main__":
    for _ in range(10):
        print(rand7Fromrand5())

