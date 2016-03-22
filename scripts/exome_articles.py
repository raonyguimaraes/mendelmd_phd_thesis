import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


csvfile = csv.reader(open('../data/exome_pubmed_timeline.csv'))
articles = {}
csvfile.next()
csvfile.next()

for line in csvfile:
	articles[int(line[0])] = int(line[1])

print articles 


fig = plt.figure()
x = np.array(articles.keys()[:-1])
y = np.array(articles.values()[:-1])

# yn = y + 0.2*np.random.normal(size=len(x))

print len(x), len(y), x, y

def func(x, a, b, c, d):
    return a*x**3 + b*x**2 +c*x + d

years = np.array(range(1993, 2021))

print years
# die()

popt, pcov = curve_fit(func, x, y)

plt.bar(x,y, align='center')
plt.plot(years,func(years,*popt),marker='o', linestyle='--', label="Fitted curve")
# axes = plt.gca()
# axes.set_xlim([,x[-1]])
# axes.set_ylim([y[0],y[-1]])
plt.xticks(years)#, rotation='vertical'

plt.axis([x[0], 2020, 0, 6000])

# popt, pcov = curve_fit(func, x, y, p0=(40, 0.012, 250), maxfev=20000)
# a, b, c = popt
# print 'a=', a, 'b=', b, 'c=', c
# print 'func=', func(x, a, b, c)

# popt2, pcov2 = curve_fit(func, x, y, p0=None, maxfev=20000)
# a2, b2, c2 = popt2
# print 'a2=', a2, 'b2=', b2, 'c2=', c2
# print 'func=', func(x, a2, b2, c2)

# xf = np.linspace(0, 70, 100)
# yf = a*np.exp(-b*x) + c

# plt.clf()
# plt.plot(x, y, 'r', label="Fitted Curve")
# plt.plot(x, func(x, *popt))
# plt.plot(x, func(x, *popt2), 'b-', label='Fit w/o guess')
plt.subplots_adjust(bottom=0.1)
# plt.plot(x, y, 'go', label='Lacquered')
plt.legend()
plt.ylabel("Number of Articles")
plt.xlabel("Years")
plt.title("Articles published on pubmed \n with the word exome in the abstract")
plt.show()
# plt.savefig("growing_of_exome_terms.png")