##순차 탐색 및 리스트를 활용한 특정값 찾기


'''    
n=int(input("탐색할 값을 입력하세요(1-10): ")) #탐색값 입력

aa=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def linearSearch(aa,n):
    for i, num in enumerate(aa):
        if num is n:
            return i
        return 'Not Found'
    

aa=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

idx=linear_search(aa, 10)

print("찾는 수는", result, "번 째에 있습니다.")

'''



aa=[1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
    n=int(input("탐색할 값을 입력하세요: "))

    for i in range(len(aa)):
        if aa[i] == n:
              print("찾는 수는",  i+1 , "번 째에 있습니다.")
              break
    else:
        print("찾는 수가 리스트에 없습니다.")

        

        
          




