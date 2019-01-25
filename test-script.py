'''
A script to automate the somewhat tedious process of running the assignment executables
against all the test input files and diffing against the expected output files.

It needs to be run from the directory containing both the executables and the testIO directory,
or it will collapse and fail miserably.

The script will show all the output diffs. If all is well, it will produce exactly nothing.
Otherwise, you'll see the line-by-line differences for your fixing pleasure, as usual.

 
TO RUN: "python test-script.py", then cross your fingers.


Hope it's handy.
M
'''

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

    # I couldn't figure out piping with the subprocess module, so the script stores the output in a temporary file,
    # uses a second subprocess to diff that with the expected-output file, and then removes the temp file.
    tmp = open("tmp", "w+")

    subprocess.call(["./" + executable], stdin=infile, stdout=tmp)

    subprocess.call(["diff", "tmp", outfilePath])

    subprocess.call(["rm", "tmp"]) 