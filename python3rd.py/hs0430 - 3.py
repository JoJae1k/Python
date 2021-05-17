pay_rate = int(input("시간 값을 입력: ")) # 변수 pay_rate 를 숫자형 "시간 값을 입력: "으로 선언
hour_worked = int(input("시급 값을 입력: ")) # 변수 hour_worked를 숫자형 "시급 값을 입력: "으로 선언
montly_pay = pay_rate * hour_worked # 변수 montly_pay를 pay_rate 와 hour_worked를 곱한 값으로 선언
print("당신의 급여는?: ", montly_pay) # "당신의 급여는?: ,montly_pay" 를 출력

#결론 : 위와 같이 계산기를 만들 수도 있다. 문자형에 int를 쓰는 이유는 터미널에 입력해야 되는 값이 숫자형이기 때문이다.
