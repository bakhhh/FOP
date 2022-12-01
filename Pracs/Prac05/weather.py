# 
# weather.py: Print min and max temps from a file 
#              (source: http://www.bom.gov.au/climate/) 


import matplotlib.pyplot as plt 

fileobj = open('Marchweather.csv', 'r') 

# add reading code here

minline = fileobj.readline()
maxline = fileobj.readline()

fileobj.close()

minsplitline = minline.strip().split(',')
maxsplitline = maxline.strip().split(',')
print(minsplitline)
mins = [float(m) for m in minsplitline]
maxs = [float(m) for m in maxsplitline]

dates = [d for d in range(1,32)]

print(dates)

plt.plot(dates, mins, dates, maxs) 
plt.title("March Weather")
#plt.plot(dates, mins)

plt.show()
