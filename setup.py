import os

def setup(name, ver, packages):
	os.mkdir(name)
	os.chdir(name)
	
	with open('packages.weblib', 'w') as f:
		f.write('{')
		f.write('\n')
		f.write('	')
		f.write('project: "' + name + '"')
		f.write('\n')
		f.write('	')
		f.write('version: ' + ver)
		f.write('\n')
		f.write('	')
		f.write('packages: {' + packages + '}')
		f.write('\n')
		f.write('}')
	
	os.mkdir('src')
	os.chdir('src')
	
	with open('main.py', 'w') as e:
		if packages == '':
			pass
		else:
			for i in range(len(packages.split(','))):
				e.write('import ' + packages.split(',')[i] + '\n')
		e.write('print(\'Hello, World!\')')
	

setup('py4web4', '1.0.0', 'requests,py4web3,py4web2,py4web,os,re,time,pyweb.weblib.dev')
