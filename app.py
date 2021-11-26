
import os
import json
import sys

from swecodxf import create_mur

#path = sys.argv[1]

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

my_file_handle=open(file_path, "r")
data = my_file_handle.read()

pyObj = json.loads(data)

btmLeft = []
btmRight = []
topRight = []
topLeft = []

pfData = pyObj["profileData"]

faces = []
def putFaces(tuples1, tuples2):
    for i in range(len(tuples1)-1):
        faces.append([tuples1[i], tuples1[i+1], tuples2[i+1], tuples2[i]])

for pfKey in pfData.keys():
    pts3d = pfData[pfKey]["points3d"]
    btmLeft.append((pts3d["btmLeft"]["x"], pts3d["btmLeft"]["y"], pts3d["btmLeft"]["z"]))
    btmRight.append((pts3d["btmRight"]["x"], pts3d["btmRight"]["y"], pts3d["btmRight"]["z"]))
    topLeft.append((pts3d["topLeft"]["x"], pts3d["topLeft"]["y"], pts3d["topLeft"]["z"]))
    topRight.append((pts3d["topRight"]["x"], pts3d["topRight"]["y"], pts3d["topRight"]["z"]))

putFaces(btmLeft, btmRight)
putFaces(btmRight, topRight)
putFaces(topRight,topLeft)
putFaces(topLeft, btmLeft)

create_mur(faces, btmLeft, btmRight, topRight, topLeft)