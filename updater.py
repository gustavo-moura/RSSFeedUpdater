

def update(**kwargs):
	file_read = open("ptdc_feed.xml", "r")
	linhas = file_read.readlines()
	file_read.close()

	linhas_write = []
	novoitem = [
		'<!-- update goes here -->',
		'\n',
		str('<item>\n'),
			str('<title>' + kwargs['title'] + '</title>\n'),
			str('<link>' + kwargs['link'] + '</link>\n'),
			str('<description>' + kwargs['description'] + '</description>\n'),
			str('<pubDate>' + kwargs['pubDate'] + '</pubDate>\n'),
			str('<guid>' + kwargs['guid'] + '</guid>\n'),
		str('</item>'),
		'\n'
	]

	#print(len(linhas))
	#print(linhas[21])

	if "<!-- update goes here -->" in linhas[21]:
		print("dentroooo")
		linhas_write = linhas[0:21] + novoitem + linhas[22:]




		file_write = open("ptdc_feed.xml", "w")
		file_write.writelines(linhas_write)
		file_write.close()



update(
	title='titulo', 
	link='https://', 
	description='description',
	pubDate='pubDate',
	guid='guid'
)


