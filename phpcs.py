import subprocess
PHPCS_BIN = '/usr/local/bin/phpcs'
PHPCS_STANDARD = 'PSR1,PSR2'
PHPCS_SEVERITY = 6
PHPCS_IGNORE = 

proc = subprocess.Popen(['git', 'diff', '--name-only', '--cached'], stdout=subprocess.PIPE)
staged_files = proc.stdout.readlines()
staged_files = [f.decode('utf-8') for f in staged_files]
staged_files = [f.strip() for f in staged_files]


print(staged_files)

