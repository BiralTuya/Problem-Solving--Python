def main():
    test = int(input())
    for i in range(test):
        n = int(input())
        for i in range(10, n + 9):
            print(i, end = ' ')
        print(n + 9)
if __name__ == '__main__':
    main()