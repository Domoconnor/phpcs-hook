import subprocess, os, sys

PHPCS_BIN = '/usr/local/bin/phpcs'
PHPCS_STANDARD = 'PSR1,PSR2'
PHPCS_SEVERITY = '6'
PHPCS_IGNORE = '/app/Services/FinancialCalculationService.php'
TMP = '.tmp_hooks'

def runProcess(exe):    
    p = subprocess.Popen(exe, stdout=subprocess.PIPE)
    while(True):
      retcode = p.poll() #returns None while subprocess is running
      line = p.stdout.readline()
      yield line
      if(retcode is not None):
        break

p = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'], stdout=subprocess.PIPE)
gitDir = p.communicate()[0].rstrip()


proc = subprocess.Popen(['git', 'diff', '--name-only', '--cached',
    '--diff-filter=ACMR'], stdout=subprocess.PIPE)
staged_files = proc.stdout.readlines()
staged_files = [f.decode('utf-8') for f in staged_files]
staged_files = [f.strip() for f in staged_files]
staged_files = [gitDir+'/'+"".join(f) for f in staged_files]

if(len(staged_files) == 0):
   print('none')
   sys.exit()


print 'started'
for line in runProcess([
    PHPCS_BIN,
    '-q',
    '--standard='+PHPCS_STANDARD,
    '--warning-severity='+PHPCS_SEVERITY,
    '--ignore='+PHPCS_IGNORE] + staged_files):
    print line,
