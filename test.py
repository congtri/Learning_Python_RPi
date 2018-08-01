import argparse
import subprocess

def execute(cmd, is_print = 1):
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	output = ''
	for line in iter(proc.stdout.readline,''):
		save_log(line.rstrip(), is_print)
		output += line.rstrip() + "\n"
	proc.communicate()[0]
	proc.wait()
	return output

parser = argparse.ArgumentParser(description='Testing')
parser.add_argument('-t', '--test',
                    help='Setting output status of GPIO\'s pin',
                    choices=['set', 'clear', 'toggle'],
                    action='store',
                    required=False)

parser.add_argument('-test',
                    help='Testing argument',
                    nargs='+',
                    action='store'
                    )

parser.add_argument('-gpio',
                    help='Setting output status of GPIO\'s pins',
                    action='store',
                    nargs='+')

arg = 0
try:
    arg = parser.parse_args()
except:
    print 'Incorrect argument'
    exit(-1)

if arg.test:
    for c in arg.test:
        print c

    print arg.test

    # for i in range(0, arg.test.lengt)
    # print 'arg.test[0]'

if arg.test:
    if arg.test == "set":
        print 'Argument GPIO Set'
    elif arg.test == "clear":
        print 'Argument GPIO Clear'
    else:
        print 'Argument GPIO Toggle'

if __name__ == '__main__':
    print __name__
    list_a = ['1', '2', '3', '456', 7]

    print len(list_a)
    pass

