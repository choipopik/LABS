def to_nums(str):
    result = []
    eds = {1:'один',2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять',0:''}
    s_tens = {10:'десять',11:'одиннадцать',12:'двенадцать',13:"тринадцать", 14:"четырнадцать", 15:"пятнадцать", 16:"шестнадцать", 17:"семнадцать", 18:"восемнадцать", 19:"девятнадцать"}
    tens = {2:'двадцать', 3:'тридцать',4:'сорок',5:'пятьдесят',6:'шестьдесят',7:'семьдесят',8:'восеьмедят',9:'девяносто',0:''}
    hunds = {1:'сто',2:'двести',3:'триста',4:'четыреста',5:'пятьсот',6:'шестьсот',7:'семьсот',8:'восемьсот',9:'девятьсот',0:''}


    if int(str) == 1000:
        result.append( 'тысяча' )
    elif len(str)==1:
        result.append(eds[int(str)])
    elif len(str)==2 and str[0]=="1":
        result.append(s_tens[int(str)])
    elif len(str)==2 and str[0]!="1":
        result.append(tens[int(str[0])])
        result.append(eds[int(str[1])])
    elif len(str) == 3:
        result.append(hunds[int(str[0])])
        result.append(to_nums(str[1:])[0])
        result.append(to_nums(str[1:])[1])

    return result



a = input()
print(*to_nums(a))

