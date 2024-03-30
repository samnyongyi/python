'''a,b,c=2,3,4
print(a+b-c,a+b*c,a*b/c)

s1, s2, s3="100", "100.123", "999999999999"
print(int(s1)+1, float(s2)+1, int(s3)+1)

a=100
b=100.123
##str(a)+'1'
##str(b)+'1'
print(str(a)+'1', str(b)+'1')

a=10
a+=5; print(a)
a-=5; print(a)
a*=5; print(a)
a/=5; print(a)
a//=5; print(a)
a%=5; print(a)
a**=5; print(a)'''

money,c500,c100,c50,c10=0,0,0,0,0

money=int(input("교환할 금액"))

c500=money//500
money%=500
c100=money//100
money%=100
c50=money//50
money%=50
c10=money//10
money%=10

print("\n500원짜리>>%d개" %c500)
print("\n100원짜리>>%d개" %c100)
print("\n50원짜리>>%d개" %c50)
print("\n10원짜리>>%d개" %c10)
print("바꾸지 못한 잔돈>>%d\n" %money)


money,c500,c100,c50,c10=0,0,0,0,0

'''money=int(input("교환할 금액"))

c50000=money//50000
money%=50000
c100=money//10000
money%=10000
c50=money//5000
money%=5000
c10=money//1000
money%=1000

print("\n50000원짜리>>%d개" %c500)
print("\n10000원짜리>>%d개" %c100)
print("\n5000원짜리>>%d개" %c50)
print("\n1000원짜리>>%d개" %c10)
print("바꾸지 못한 잔돈>>%d\n" %money)'''



