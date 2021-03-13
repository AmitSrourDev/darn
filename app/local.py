import subprocess
def run(cmd):
    subprocess.run(cmd.split(' '))

def ls():
    subprocess.call(["ls", "-l"])