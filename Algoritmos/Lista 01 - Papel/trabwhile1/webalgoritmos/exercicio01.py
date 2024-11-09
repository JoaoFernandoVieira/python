listaA = [10,15,13,60,80,10]
listaB = [10,10,10,20,20,20]

print(listaA)
print(len(listaB))

print('1----------')
i = 0
while i < len(listaA):
    print(listaA[i])
    i = i + 2
    
print('2----------')
i = 3
while i >=0:
    print(listaA[i])
    i = i - 1
print('3----------')
i=0
while i<3:
    print(listaA[i]+listaB[i])
    i = i + 1

print('4----------')
if listaA[2]>listaB[2]:
    print('Maior:',listaA[2])
else:
    if listaA[2]>listaB[2]:
        print('Maior:',  listaB[2])

print('5----------')
i=1
while i<6:
    listaB[i] = 50
    i = i + 2
print(listaB)

print('6----------')
i = 3
while i < 6:
    print(listaA[i])
    i = i + 1