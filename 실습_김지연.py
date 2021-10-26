##파이썬_1022
'''
myList=[30, 10, 20]
print("현재 리스트: %s" %myList)

myList.append(40)
print("append(40)후의 리스트: %s" %myList)

print("pop() 으로 추출한 값 : %s" %myList.pop())
print("pop() 후의 리스트: %s" %myList)

myList.sort()
print("sort() 후의 리스트: %s" %myList)

myList.reverse()
print("reverse() 후의 리스트 : %s" %myList)

print("20값의 위치: %d" %myList.index(20))

myList.insert(2,222)
print("insert(2,222) 후의 리스트: %s" %myList)
 
myList.remove(222)
print("remove(222) 후의 리스트 : %s" %myList)

myList.extend( [77, 88, 77] )
print("extend([77, 88, 77]) 후의 리스트 : %s" %myList)

print("77값의 개수: %d" %myList.count(77))
'''
'''
aa=[ ]
bb=[ ]
value=0

for i in range(0, 100) :
    aa.append(value)
    value+=2

for i in range(0, 100):
    bb.append(aa[99-i])

print(" bb[0]은 %d, bb[99]는 %d 입력됨" %(bb[0], bb[99]))
'''
'''
list1= [ ] #내부배열
list2= [ ] #외부배열
value=1 #배열의 값을 위한 변수, 초기화되지 않고 증가하는 변수

#빈 리스트에 값 추가하기
for i in range(0,3):  #외부배열을 위한 반복문, 3번 반복
    for k in range(0,4): #내부배열을 위한 반복문, 4번 반복
        list1.append(value) #빈 리스트에 value값 추가
        value +=1 #value 1씩 증가
    list2.append(list1)
    list1= [ ] #내부 배열 비우기

#2차원 리스트의 값을 출력
for i in range(0,3):
    for k in range(0, 4):
        print("%3d" %list2[i][k], end=" ") #(3d는 세칸) 세칸으로 출력하고 한 칸 띄우기
    print(" ") #줄바꿈
'''
'''
list1= [ ]
value=0
for i in range(0,10):
    list1.append(i)
    print(list1)
'''

##튜플: 한 번 만들고 나면 변경할 수 없는 집합
##리스트는 대괄호[], 튜플은 소괄호(), 딕셔너리는 중괄호 {}
##소괄호 없어도 되긴 된다
##튜플은 수정불가, 읽기전용

'''
mytuple=1,2,3
print(mytuple)

'''

##딕셔너리: 키로 값을 지정해야 한다.(구성: 키, 값)
##리스트의 인덱스 대신 키 사용, 딕셔너리는 키를 이용하여 값을 찾아낼 때 편리
##딕셔너리는 리스트와 달리 값의 순서를 지켜주지 않음.
##딕셔너리는 수정 가능함
'''
student1={'학번': 20, '이름': '홍길동', '전공': '빅데이터'}
print(student1['학번'])
student1['연락처']= '010-1234-5678'
print(student1)
student1.pop('전공')
print(student1)

student1.clear()
print(student1)

'''


'''
n=int(input("탐색할 값을 입력하세요: "))
def linearSearch(list,n):
    for i in range(len(list)):
        if n==list[i]:
            return i
        return -1

x=[1, 2, 3, 4, 5, 6, 7, 8, 9]

result=linearSearch(x, n)

if result != -1:
    print("찾는 수는", result, "번 째에 있습니다.")

else:
    print("탐색에 실패했습니다.")


'''
'''
    list_num=len(list)

    for x in range(0, list_num):
        if a ==list[x]:
            print(
                
list= [ ]
value=0
for i in range(0,10):
    list.append(value)
    value+=1

'''
























