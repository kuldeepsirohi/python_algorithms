def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    li_limit = int(input())
    li = []

    for i in range(li_limit):
        row = []
        #for j in range(li_limit):
        input_string = input()
        char_list = input_string.split()
        row = list(map(int,char_list))
        li.append(row)

    print(li)
    rows = len(li)
    cols = len(li[0])
    for row in range(rows):
        if row%2 ==0:
            for col in range(cols):
                print(li[col][row],end=" ")
        else:
            for col in range(cols-1,-1,-1):
                print(li[col][row],end=" ")



    return 0

if __name__ == '__main__':
    main()
