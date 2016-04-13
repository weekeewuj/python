A = ['Hello','Location',12,'Bash']
l = []
for s in A:
    if isinstance(s,str):
        s = s.lower()
    l.append(s)
print l
