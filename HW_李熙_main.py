#李熙堃 Joshua Lee
def apart(sentence,dict):
    x = len(sentence)
    while x>0:
        if sentence.isascii() and sentence.isalnum():#判斷是否為一整串的英文字或是數字
            return sentence
        elif x == 1:  # 如果一個字判斷不出來 還是要回傳
            return sentence
        elif sentence in dict:#在字典中
            return sentence
        else:#迴圈從最後一個字開始去除，找到了由上方回傳
            x -= 1
            sentence = sentence[0:x]

def main():
    dict_S = dict()
    result = list()
    with open('dict_no_space.txt','r',encoding = 'utf-8') as dictionary:
        for data in dictionary:
            dict_S[data.strip()] = True
            
    sentence = input()

    start = 0
    while start < len(sentence):
        temp = apart(sentence[start:],dict_S)#找出對應的字元 放入temp
        result.append(temp)#加入LIST中
        start += len(temp) #找到了一個字元，理當要往前進
    print(result)
#這個做法從後面跟前面都可以，但兩種方法會導致不一樣的結果
if __name__ == '__main__':
    main()
