def fc(temper,action):
    if(action==0):
        print("C2F :",temper, "=>", temper*1.8+32)
    else:
        print("F2C :",temper, "=>", (temper-32)/1.8)

temper=int(input("온도 : "))
action=int(input("변환(C2F:0 , F2C:1) : "))
fc(temper,action)
