import subprocess
process = subprocess.Popen(['bash','do.sh','foo','bar'], shell=True, stdout=subprocess.PIPE)
process.wait()
print(process.returncode)
