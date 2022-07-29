import requests

toGet = ["percentage", "count", "option-text"]
bracTillVal = [2, 1, 1]
numToGet = 2
vals = []

result = requests.post("https://either.io/").text

for i in range(len(toGet)):
    vals.append([])
    toSlice = 0
    for j in range(numToGet):
        toSlice+=result[toSlice:len(result)].find(f"class=\"{toGet[i]}\"")
        for k in range(bracTillVal[i]):
            while True:
                toSlice+=1
                if result[toSlice] == '>':
                    break
        toSlice+=1
        until = 0
        while True:
            until+=1
            if result[toSlice + until] == '<':
                break
        vals[i].append(result[toSlice:toSlice + until])
input(f"Would you rather\n    {vals[2][0]}\n    or\n    {vals[2][1]}\n? ")
for i in range(numToGet):
    input(f"{vals[0][i]}% of people ({vals[1][i]} people) chose {vals[2][i]}")
