import csv
import re
from textblob import TextBlob as tb
from time import strptime
import string
import nltk
import pandas as pd
import matplotlib.pyplot as plt 
			
data = []
quart = []

def createNewCsv():
	try:
		with open('glassdoortest1.csv') as csvFile:
			csvReader = csv.reader(csvFile, delimiter=',')
			count  = 0
			with open('sentimentglassdoor.csv', mode='w') as glassdoor:
	    			writer = csv.writer(glassdoor, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
	    			for row in csvReader:
	    				if(count == 0):
	    					writer.writerow([f'{row[0]},{row[1]}','quarter','year',f'{row[2]},{row[3]},{row[4]},prospolarity,conspolarity,totalpolarity'])
	    				else:
	    					pros = getSentiment(row[3])
	    					cons = getSentiment(row[4])
	    					row[2] = clean(row[2])
	    					row[3] = clean(row[3])
	    					row[4] = clean(row[4])
	    					quarter = getQuarter(row[1])
	    					year = getYear(row[1])
	    					writer.writerow([f'{row[0]},{row[1]}',quarter,year,f'"{row[2]}","{row[3]}","{row[4]}"',pros,cons,pros+cons])
	    				count = 1
	    			
	except Exception:
		pass
    	
    	
def clean(line):
	line = re.sub('\"', ' ', line)	 
	return line    		
    
def cleanText(text): 
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ", text).split()) 
 	

def getSentiment(text):
	analysis = tb(cleanText(text))
	return(analysis.sentiment.polarity)
	
def getQuarter(date):
	dmonth = str(date[3:6])
	dmonth = strptime(dmonth,'%b').tm_mon
	return (dmonth // 4)+1
	
def getYear(date):
	dyear = date[7:]
	return dyear
	
def plotGraph(index):
	count = 0
	a = {}
	count = 0
	years=['16','17','18']
	quaters=['1','2','3','4']

	try:
		with open('sentimentglassdoor.csv') as glassdoor:
			csvReader = csv.reader(glassdoor, delimiter=',')
			for r in csvReader:
				if(count>0):
					arrlen = len(r)-1
					for y in years:
						if r[3] == y:
							for q in quaters:
								if r[2] == q:
									key = y+ '_' + q
									if (key in a):
										a[key]+=float(r[arrlen-index])
									else:
										a[key]=float(r[arrlen-index])	
				count = 1
			
			x = a.values()
			#print(x)
			tick_label = [*a]
			#print(tick_label)
			if index == 0:
				plt.title('Change in trends of Comments by Quarter')
				y = range(0 , 200 , 20)
			elif index == 1:
				plt.title('Change in trends of Cons by Quarter')
				y = range(0 , -200 , -20)
			else:	
				plt.title('Change in trends of Pros by Quarter')
				y = range(0 , 200 , 20)
			plt.ylabel('Sentiment Score')
			plt.xlabel('Time Line') 
			plt.bar(y, x, tick_label = tick_label, width = 0.8, color = ['blue']) 
			plt.show() 

	except Exception:
		pass
	
createNewCsv()
#Overall sentiment score
plotGraph(0)
#Cons sentiment score
plotGraph(1)
#Pros sentiment score
plotGraph(2)

