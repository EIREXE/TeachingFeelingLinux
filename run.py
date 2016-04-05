#FUCK OFF LINUX
import os
import subprocess

running_dir = os.path.dirname(os.path.realpath(__file__))

if(os.path.isfile("data/scenario/opening.ks")):
    os.rename("data/scenario/opening.ks", "data/scenario/Opening.ks")
args = ("linux/bin/nw", running_dir)
popen = subprocess.Popen(args, stdout=subprocess.PIPE)
popen.wait()
output = popen.stdout.read()
print(output)
