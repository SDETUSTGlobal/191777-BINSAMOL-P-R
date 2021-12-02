fh = open('demo.txt','w+')
fh.write('Hello World.\nWelcome to the Earth \n')

for i in range(10):

    fh.write("This is line no %d\n" % (i+1))

fh.write('Stranger in Moscow\n')
fh.close()