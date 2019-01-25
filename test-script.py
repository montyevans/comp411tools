import os
import subprocess

ioDir = "testIO"

files = os.listdir(os.getcwd() + "/" + ioDir)

infiles = [f for f in files if f.find("in") != -1]
outfiles = [f for f in files if f.find("out") != -1]

for f in infiles:
    executable = f.split("in")[0]

    outfilePath = ioDir + "/" + executable + "out" + f.split("in")[1]

    infile = open(ioDir + "/" + f)

    tmp = open("tmp", "w+")

    subprocess.call(["./" + executable], stdin=infile, stdout=tmp)

    subprocess.call(["diff", "tmp", outfilePath])

    subprocess.call(["rm", "tmp"]) 