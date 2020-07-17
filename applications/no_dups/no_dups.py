def no_dups(s):
    # Your code here
    words = s.strip().split()
    new = ""
    duplicate_dic = {}
    for word in words:
        if word not in duplicate_dic.keys():
            duplicate_dic[word] = 1
            new += word + ' '
    return new.strip()
if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))