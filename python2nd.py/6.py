def chat(name1, name2):
    print("%s: 안녕? 너 몇살이니?" %name1)
    print("%s: 나? 나는 20살이야!" %name2)
chat("정수", "태희")
chat("은지", "가연")

a = 3
b = 2
c = 5
d = c-a

print(a + b)
print(a * d)
print(b % d)

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