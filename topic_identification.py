from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import csv
import matplotlib.pyplot as plt 


with open('sentimentglassdoor.csv') as csvFile:
	csvReader = csv.reader(csvFile, delimiter=',')
	document = []
	for row in csvReader:
		document.append((f'{row[5]},{row[6]}'))
	vectorizer = TfidfVectorizer(stop_words='english')
	X = vectorizer.fit_transform(document)
	true_k = 3
	model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
	model.fit(X)

	order_centroids = model.cluster_centers_.argsort()[:, ::-1]
	terms = vectorizer.get_feature_names()
	a = []
	for i in range(true_k):
		for ind in order_centroids[i, :2]:
			a.append(' %s' % terms[ind])
	
def showPlot(category):	
	with open('sentimentglassdoor.csv') as csvFile:	
		csvReader = csv.reader(csvFile, delimiter=',')
		cluster = [0]*true_k
		for row in csvReader:
			Y = vectorizer.transform([row[category]])
			prediction = model.predict(Y)
			cluster[int(prediction)] += 1
		x = cluster
		y = range(0 , 300 , 100)
		if(category == 6):
			plt.title('Topics with max true complaints')
			plt.xlabel('Topics')
			plt.ylabel('No of Cons') 
		if(category == 5):
			plt.title('Top reasons for positivity')
			plt.xlabel('Topics')
			plt.ylabel('No of Pros') 
		
		tick_label = [a[0]+a[1],a[2]+a[3],a[4]+a[5]] 
		plt.bar(y, x, tick_label = tick_label, width = 0.8, color = ['blue']) 
		plt.show() 
#Top reasons for positivity
showPlot(5)
#Top reasons for negativity
showPlot(6)
