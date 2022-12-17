bud=40
dic=[26,20.5,34,10.5,18]
paper=["TOI","Hindu","ET","BM","HT"]
i=0
b=[]
for i in range(4):
    j=i+1
    while j<5:
        if dic[i]+dic[j]<=bud:
            a=[paper[i],paper[j]]
            b.append(a)
        j+=1
print(b)