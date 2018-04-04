import subprocess, os
PHPCS_BIN = '/usr/local/bin/phpcs'
PHPCS_STANDARD = 'PSR1,PSR2'
PHPCS_SEVERITY = 6
PHPCS_IGNORE = ''

def runProcess(exe):    
    p = subprocess.Popen(exe, stdout=subprocess.PIPE)
    while(True):
      retcode = p.poll() #returns None while subprocess is running
      line = p.stdout.readline()
      yield line
      if(retcode is not None):
        break

proc = subprocess.Popen(['git', 'diff', '--name-only', '--cached',
    '--diff-filter=ACMR'], stdout=subprocess.PIPE)
staged_files = proc.stdout.readlines()
staged_files = [f.decode('utf-8') for f in staged_files]
staged_files = [f.strip() for f in staged_files]

if(len(staged_files) == 0):
   print('none') 

print 'started'
for line in runProcess([PHPCS_BIN,
    '--standard='+PHPCS_STANDARD, os.getcwd()]):
    print line,
