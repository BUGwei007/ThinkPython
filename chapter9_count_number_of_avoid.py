## 9.3对每个字母找到avoids的数量

def avoids(word, letter):
    """ 判断一个单词中是否出现 禁止的单词！"""
    for i in word:
        if i == letter:
            return False
    return True


def main():
    fin = open('avoid.txt')
    print(fin)
    for x in range(ord('a'), ord('e') + 1):
        letter = chr(x)
        count = 0
        print(fin.closed)
        # print(fin.readlines())
        for line in fin:
            word = line.strip()
            print(word, letter)
            if avoids(word, letter):
                count += 1
        print(letter, '的数量为', count)
    print(fin.closed)
    print(fin.readline())

main()