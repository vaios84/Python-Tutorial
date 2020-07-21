import urllib
url = 'http://export.arxiv.org/api/query?search_query=all:recommender&systems&start=0&max_results=10'
data = urllib.urlopen(url).read()
print(data)

file1 = open("arxiv_data.xml","w") 
file1.writelines(data)

file1.close() 
