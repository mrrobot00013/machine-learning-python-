dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
x =  dict(dic3.items() | dic2.items() | dic1.items())
print(sorted(x.items()))