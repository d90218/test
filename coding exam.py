#First Question

def score(scorelist):
    new_score_list = []
    for i in range(len(scorelist)):
        tmpscore = transferscore(scorelist[i])
        if tmpscore < 40:
            new_score_list.append(scorelist[i])
        else:
            new_score_list.append(tmpscore)
    print(new_score_list)
        

def transferscore(score):
    quotient, remainder = divmod(score, 10)
    if  remainder <= 4 and (5-remainder)<3:
        newscore = (quotient*10 + 5)
        print(quotient, remainder, newscore) 
    elif remainder >= 5 and (10-remainder)<3:
        newscore = ((quotient+1)*10)
        print(quotient, remainder, newscore)
    else:
        print(quotient, remainder, newscore)
        return score
    return newscore


score([33,73,63,39])


#Second Question

def counthigh(n):
    count = 0
    total_high = 100
    sum = 0
    while count != n-1:
        total_high = total_high / 2
        count += 1
        sum = sum + total_high
    print("總共:%f 第十次：%f" %(100+2*sum, total_high/2))

counthigh(10)