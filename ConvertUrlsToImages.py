import urllib2

with open('chrome___cache.txt') as f:
	content = f.readlines()

j = 0
http = []

for i in range(0, len(content)):
	if 'http' in content[i]:
		http.append(content[i])
		j = j+1

for i in range(0, len(http)):
	try:
		name = 'Pictures/%s.jpg' % i
		image = urllib2.urlopen(http[i])
		output = open(name,'wb')
		output.write(image.read())
		output.close()
	except Exception, e:
		print e