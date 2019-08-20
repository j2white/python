import sys, os

for item, value in sorted(os.environ.items()):
  x = ('{}: {}'.format(item, value))
  print(x)

print('-'*50)

x =  sorted(os.environ.items())
for i in x:
	print(i)


print('-'*50)

f = os.path.basename(sys.argv[0])
a = os.environ['PYTHONPATH']
b = os.environ['USERNAME']
c = os.environ['COMPUTERNAME']

print(f,a,b,c)