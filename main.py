# a=int(input('wprowadz xd'))
# b=int(input('wprowadz cos'))
#
#
# wynik=(((a*a)+(a*b)+(b*b)))
# print((a*a)+(a*b)+(b*b))
# zadanie=open('zadanie1.txt','a+')
# zadanie.write(str(wynik))
# x=zadanie.read(23)
# x
# lista=open('lista.txt','r')
# listb=open('listb.txt','r')
# class listy(lista,listb):
#     listc=open('listc','a+')
#     for i in range(1,len(lista)):
#         listc.write(lista[i]+listb[i])
n=int(input())
suma = 0
for i in range(1, n+1):
    suma=suma+i

print(suma)
zrycie=open('likkt','w+')
zrycie.write(4)
x=zrycie.read(1)
y=zrycie.read(1)


