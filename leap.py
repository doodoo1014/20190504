def leapCommon(y):
    if (y%4==0 and y%100!=0) or (y%400==0):
        print("윤년(Leap Year) 입니다.")
    else:
        print("평년(Common Year) 입니다.")

year=int(input("연도 입력 : "))
leapCommon(year)
