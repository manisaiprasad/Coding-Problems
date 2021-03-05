n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
Ascore = 0
Bscore = 0
if len(arr) == 1:
    print("0")
else:
    while len(arr) >= 2:
        first = arr.pop(0)
        Ascore += first+arr.pop(0)
        if len(arr) >= 2:
            second = arr.pop()
            Bscore += second+arr.pop(0)
        if len(arr) == 1:
            Ascore += arr.pop(0)
    print(Ascore-Bscore)