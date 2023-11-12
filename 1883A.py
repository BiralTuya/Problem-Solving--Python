def main():
    test = int(input())
    
    for j in range(test):
        result = 0
        codestr = input()
        code = [int(char) for char in codestr]
        l = len(code)
        #print(code)
        for i in range(l):
            if code[i] == 0:
                code[i] = 10

        for i in range(l-1):
            result += abs(code[i]-code[i+1])
        result += 4 + code[0]-1
        print(result)
        # print(l)

if __name__ == '__main__':
    main()