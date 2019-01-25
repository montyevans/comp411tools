# I wrote this line about eight times before I gave up and shoved it into a script.
# 
# TO RUN: "./build.sh" - just like a C executable.
#
# Hope it's handy.
# M

for i in {1..5}; do gcc ex$i.c -o ex$i; done
