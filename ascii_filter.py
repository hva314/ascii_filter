#!/usr/bin/python3

import os 
import sys
import click

lst = sys.argv
print(lst)
for i in range(1,len(lst)):

    file_name = str(lst[i])
    print()
    print(str(i)+". Collecting data from "+lst[i]+"...")

    f = os.popen("sed -n '$=' "+file_name)
    num_line = int(f.read())

    print("Done!")
    print("Line numbers:", num_line)
    count = 1
    with open(file_name, encoding="ISO-8859-1") as r, open("new_"+file_name, "w") as w:
        for line in r:
            
            print("\rRunning: "+str(count)+"/"+str(num_line)+" => %"+str(round(count/num_line*100,2)), end="")
            count += 1

            if (all(ord(char) < 128 for char in line)):
                w.writelines(line)

