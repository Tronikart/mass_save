import requests

urls = input('feed a single string of urls separated by a space: ')
urls = urls.split(' ')

total = len(urls)
current = int()
filenames = list()
errors = list()

print(f'getting ready for {total} urls')

for url in urls:
	current += 1

	# This bit is a bit specific but its to catch the filename and remove any parameter that may come afterwards
	filename = url.split('/')[-1].split('?')[0]

	print('-'*70)
	print(f'saving image number {current} so far, {total-current} remaining, \nsaving with {filename} as its filename')
	request = requests.get(url)
	
	if filename in filenames:
		filename = f'{filename.split(".")[0]} {current}.{filename.split(".")[1]}'
	else:
		filenames.append(filename)

	if request.ok:
		with open(filename, 'wb+') as f:
			f.write(request.content)
	else:
		print(f'error requesting url number {current}, error: {request.status_code}\nurl: {url}')
		errors.append(url)

if errors: 
	print('Urls that couldn\'t be saved:')
	for error in errors:
		print(f'\t{error}')



