
#!/usr/bin/python

import sys, getopt
from PIL import Image, ImageDraw

def main(argv):
	inputFile = ''
	outputFile = ''
	r = -1
	g = -1
	b = -1
	h = 0;
	v = 0;
	
	# Parsing the arguments passed on the command line:
	try:
		opts, args = getopt.getopt(argv, "ni:o:r:g:b:h:v:")
	except getopt.GetoptError:
		print 'usage: toGridded.py - i <inputfile> -o <outputfile>'
		sys.exit (2)
	for opt, arg in opts:
		if opt == '-n':
			print 'usage: toGridded.py - i <inputfile> -o <outputfile>'
			sys.exit ()
		elif opt == '-i':
			inputFile = arg
		elif opt == '-o':
			outputFile = arg
		elif opt == '-r':
			r = arg
		elif opt == '-g':
			g = arg
		elif opt == '-b':
			b = arg
		elif opt == '-h':
			h = int (arg)
		elif opt == '-v':
			v = int (arg)

	if h == 0 or v == 0:
		print '-h and -v must be specified'
		sys.exit ()

	# Openning the input file:
	if not inputFile:
		print 'The argument: <inputfile> is required.'
		sys.exit ()
	im = Image.open (inputFile)
	
	size = im.size
	draw = ImageDraw.Draw (im)

	# Choosing a color:
	if r != -1 and g != -1 and b != -1:
		rgb = True
	else:
		rgb = False

	for y in range (1,h):
		#if rgb:
			draw.line((0, im.size[1]/h*y, im.size[0], im.size[1]/h*y), fill=0)
		#else:
		#	draw.line ((0 , 0) + size, fill=128)
	
	for x in range(1,v):
		draw.line((im.size[0]/v*x, 0, im.size[0]/v*x, im.size[1]), fill=0)

	im.show ()


	# Saving the result:
	if not outputFile:
		im.save('gridded_' + inputFile, 'JPEG')
		sys.exit ()
	im.save (outputFile, 'JPEG')

if __name__ == "__main__":
	main (sys.argv[1:])

#

