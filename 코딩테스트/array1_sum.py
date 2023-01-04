

num=int(input("입력할 숫자의 개수: "))
abc=[]

def start():
    a=input("숫자입력 ㄱㄱ")
    for i in range(num):
        abc.append(int(a[i]))

    return print(sum(abc))

if num>100 and num<1:
    print("숫자개수를 잘 입력해주세요")
else:
    start()



