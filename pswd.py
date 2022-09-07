import subprocess as sp
res = sp.run("netsh wlan show profiles",capture_output="True",shell="flase")
l1 = str(res).split("\\n")
l1.pop()
l1.pop()
l = l1[9:]
for i in range(len(l)):
    l[i] = l[i][27:len(l[i])-2]

d = {}

for i in l:
    a = str(sp.run(f'netsh wlan show profile {i} key = clear',capture_output="True")).split("\\n")
    for j in a:
        if "Key Content" in j:
            d[i] = j[29:len(j)-2]
            break
    else:
        d[i] = "Not Found"

f = open(r"passwords.txt","w")

for i in range(len(l)):
    f.write(f'{l[i]} : {d[l[i]]}\n')

f.close()
