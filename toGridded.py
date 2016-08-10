
#!/usr/bin/python

import sys, getopt
from PIL import Image, ImageDraw

def main(argv):
	inputFile = ''
	outputFile = ''
	#r = -1
	#g = -1
	#b = -1
	
	v = 10

	tMargin = bMargin = lMargin = rMargin = 0

	# Parsing the arguments passed on the command line:
	try:
		opts, args = getopt.getopt(argv, "hi:o:v:t:b:l:r:")
	except getopt.GetoptError:
		print 'usage: toGridded.py - i <inputfile> -o <outputfile> -v <nVerticalSteps> -t <topMargin> -b <bottomMargin> -l <leftMargin> -r <rightMargin>'
		sys.exit (2)
	for opt, arg in opts:
		if opt == '-h':
			print 'usage: toGridded.py - i <inputfile> -o <outputfile> -v <nVerticalSteps> -t <topMargin> -b <bottomMargin> -l <leftMargin> -r <rightMargin>'
			sys.exit ()
		elif opt == '-i':
			inputFile = arg
		elif opt == '-o':
			outputFile = arg
		elif opt == '-v':
			v = int (arg)
		elif opt == '-t':
			tMargin = int (arg)
		elif opt == '-b':
			bMargin = int (arg)
		elif opt == '-l':
			lMargin = int (arg)
		elif opt == '-r':
			rMargin = int (arg)

	if not inputFile:
		print 'The argument: <inputfile> is required.'
		sys.exit ()
	im = Image.open (inputFile)
	
	draw = ImageDraw.Draw (im)

	# Choosing a color:
	#if r != -1 and g != -1 and b != -1:
	#	rgb = True
	#else:
	#	rgb = False

	# Drawing margins
	if lMargin > 0:
		draw.line((lMargin, tMargin, lMargin, im.size[1] - bMargin), fill=0)
	if rMargin > 0:
		draw.line((im.size[0] - rMargin, tMargin, im.size[0] - rMargin, im.size[1] - bMargin), fill=0)
	if tMargin > 0:
		draw.line((lMargin, tMargin, im.size[0] - rMargin, tMargin), fill=0)
	if bMargin > 0:
		draw.line((lMargin, im.size[1] - bMargin, im.size[0] - rMargin, im.size[1] - bMargin), fill=0)

	width = im.size[0] - lMargin - rMargin
	height = im.size[1] - tMargin - bMargin

	step = width / v

	print 'step = ', step
	print 'last horizontal step: ', (width - (v*step)), '(', ((width - (v*step))*100/step), '%)'
	print 'last vertical step: ', (height % step), '(', ((height%step)*100/step), '%)'
	
	# Drawing vertical lines:
	for i in range(1, v):
		draw.line((lMargin + step*i, tMargin, lMargin + step*i, tMargin + height), fill=0)
	draw.line((lMargin + step*v, 0, lMargin + step*v, im.size[1]), fill=0)

	# Drawing horizontal lines:
	for i in range (1, height/step + 1):
		draw.line((lMargin, tMargin + step*i, lMargin+width, tMargin + step*i), fill=0)
	#draw.line((0, tMargin + step*(height/step), im.size[0], tMargin + step*(height/step)), fill=0)
	
	im.show ()


	# Saving the result:
	if not outputFile:
		im.save('gridded_' + inputFile, 'JPEG')
		sys.exit ()
	im.save (outputFile, 'JPEG')

if __name__ == "__main__":
	main (sys.argv[1:])


