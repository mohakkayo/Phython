##파이썬_1022_순차탐색_김지연


aa=[ ]

for i  in range (1, 11):
    aa.append(i)

print(aa)

while True:
    n=int(input("탐색할 값을 입력하세요: "))

    for i in range(len(aa)):
        if aa[i] == n:
              print("찾는 수는",  i+1 , "번 째에 있습니다.")
              break
    if not n in aa:
        print("찾는  숫자가 리스트에 없습니다.")
