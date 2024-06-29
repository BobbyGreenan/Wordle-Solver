yellowsadd = []
possible_letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
yellows = [["" for i in range(5)] for i in range(5)]

wordlist = set()

with open("dictwordle.txt", "r") as file:
    for line in (file):
        word = line.strip()
        wordlist.add(word)


def wordcorrect(inputword):
    return inputword in wordlist



green = ["", "", "", "", ""]
attemmpsinput = int(input("how many attempts have you used? \n"))
for row in range(0, attemmpsinput):
    print("what is your guess",(row+1),"?")
    wordforattempt = input("")
    wordpattern = input("what is your pattern? e.g. ybbgy or bbgyb.  \n")
    for x in range(0, 5):
        if wordpattern[x] == "g":
            green[x] = wordforattempt[x]
    for x in range(0, 5):
        if wordpattern[x] == "b":
            if wordforattempt[x] in possible_letters:
                possible_letters.remove(wordforattempt[x])
    for x in range(0, 5):
        if wordpattern[x] == "y":
            yellowsadd.append(wordforattempt[x])
            yellows[row][x] = wordforattempt[x]
for x in yellowsadd:
    if x not in possible_letters:
        possible_letters.append(x)
possible_letters.sort()
possible_words = []
yellowrow1 = ["", "", "", "", ""]
yellowrow2 = ["", "", "", "", ""]
yellowrow3 = ["", "", "", "", ""]
yellowrow4 = ["", "", "", "", ""]
yellowrow5 = ["", "", "", "", ""]
L1 = green[0]
L2 = green[1]
L3 = green[2]
L4 = green[3]
L5 = green[4]
yellow = [
    yellowrow1[0], yellowrow1[1], yellowrow1[2], yellowrow1[3], yellowrow1[4],
    yellowrow2[0], yellowrow2[1], yellowrow2[2], yellowrow2[3], yellowrow2[4],
    yellowrow3[0], yellowrow3[1], yellowrow3[2], yellowrow3[3], yellowrow3[4],
    yellowrow4[0], yellowrow4[1], yellowrow4[2], yellowrow4[3], yellowrow4[4],
    yellowrow5[0], yellowrow5[1], yellowrow5[2], yellowrow5[3], yellowrow5[4]
]
nL1 = L1
nL2 = L2
nL3 = L3
nL4 = L4
nL5 = L5
words = 0
for i in (possible_letters):
    if L1 == "":
        if i == yellows[0][0] or i == yellows[1][0] or i == yellows[2][
                0] or i == yellows[3][0] or i == yellows[4][0]:
            continue
        else:
            nL1 = i
    for j in (possible_letters):
        if L2 == "":
            if j == yellows[0][1] or j == yellows[1][1] or j == yellows[2][
                    1] or j == yellows[3][1] or j == yellows[4][1]:
                continue
            else:
                nL2 = j
        for q in (possible_letters):
            if L3 == "":
                if q == yellows[0][2] or q == yellows[1][2] or q == yellows[2][
                        2] or q == yellows[3][2] or q == yellows[4][2]:
                    continue
                else:
                    nL3 = q
            for t in (possible_letters):
                if L4 == "":
                    if t == yellows[0][3] or t == yellows[1][3] or t == yellows[
                            2][3] or t == yellows[3][3] or t == yellows[4][3]:
                        continue
                    else:
                        nL4 = t
                for h in (possible_letters):
                    if L5 == "":
                        if h == yellows[0][4] or h == yellows[1][
                                4] or h == yellows[2][4] or h == yellows[3][
                                    4] or h == yellows[4][4]:
                            continue
                        else:
                            nL5 = h
                    text = (nL1 + nL2 + nL3 + nL4 + nL5)
                    text = str(text)
                    if wordcorrect(text) == 1:
                        valid_word = 1
                        for i in range(0, 5):
                            for n in range(0, 5):
                                if yellows[i][n] != "":
                                    if yellows[i][n] not in text:
                                        valid_word = 0
                                        break
                                else:
                                    continue
                        if valid_word:
                            words += 1
                            print(text)
                    if L5 != "":
                        break
                if L4 != "":
                    break
            if L3 != "":
                break
        if L2 != "":
            break
    if L1 != "":
        break
print("Words:", words)
