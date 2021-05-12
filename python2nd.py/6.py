def chat(name1, name2): #함수명을 chat으로 매개변수를 name1, name2로 선언
    print("%s: 안녕? 너 몇살이니?" %name1) #문자형 "name1 : 안녕? 너 몇살이니?" 출력"
    print("%s: 나? 나는 20살이야!" %name2) #문자형 "name2 : 나? 나는 20살이야!" 출력"
chat("정수", "태희") #name1을 정수, name2를 태희로 선언
chat("은지", "가연") #name1을 정수, name2를 태희로 선언

a = 3 #변수 a (숫자형 3 으로 선언)
b = 2 #변수 b (숫자형 2 으로 선언)
c = 5 #변수 c (숫자형 5 으로 선언)
d = c-a #변수 d (문자형 c를 a 로 뺀 값으로 선언)

print(a + b) #문자형 a와 b를 더한 값 출력
print(a * d) #문자형 a와 d를 곲한 값 출력
print(b % d) #문자형 b와 d를 나눈 후  값 출력

if a > b :
    print("Hello 0_0")
if a > c :
    print("what")
elif a == d :
    print("Bye~!")
else :
    print("Hi")
    
def chat(name1, name2, age):
    print("%s: 안녕? 너 몇살이니?" %name1)
    print("%s: 나? 나는 %d!" % (name2, age) + "살이야!")
chat("정수", "태희", 20)
chat("환준", "세영", 19)
