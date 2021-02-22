# this script is to run on Windows

try:
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog
import os
import subprocess


window2 = tk.Tk()
window2.title("Running FDS and OpenSEES")
window2.geometry("380x300")
# this is a frame for the entries of files and options for the user to chose the devices
frame1 = tk.LabelFrame(window2, text="FDS Inputs", padx=5, pady=5)
frame1.grid(row=0, column=0, sticky="nsew")


def location():  # Directory Location
    get = filedialog.askdirectory()
    os.chdir(get)


tk.Button(frame1, text="Directory", command=location, width=15, height=1).grid(row=0, column=1, padx=10, pady=10)
tk.Label(frame1, width=20, text="Get Working Directory", anchor='e').grid(row=0, column=0, padx=5, pady=5)


FDS_FILE = tk.Entry(frame1, width=20)
FDS_FILE.grid(row=1, column=1)
FDS_FILE.insert(tk.END, "SemiConfined_Case1")
tk.Label(frame1, width=15, text="FDS File Name", anchor='e').grid(row=1, column=0)

MPI = tk.Entry(frame1, width=20)
MPI.grid(row=2, column=1)
MPI.insert(tk.END, "4")
tk.Label(frame1, width=15, text="MPI Processes", anchor='e').grid(row=2, column=0)

CORES = tk.Entry(frame1, width=20)
CORES.grid(row=3, column=1)
CORES.insert(tk.END, "2")
tk.Label(frame1, width=15, text="Assigned Cores", anchor='e').grid(row=3, column=0)


frame2 = tk.LabelFrame(window2, text="OpenSEES Inputs", padx=5, pady=5)
frame2.grid(row=1, column=0, sticky="nsew")

OpenSEES_FILE = tk.Entry(frame2, width=20)
OpenSEES_FILE.grid(row=0, column=1)
OpenSEES_FILE.insert(tk.END, "htibeamast")
tk.Label(frame2, width=20, text="OpenSEES File Name", anchor='e').grid(row=0, column=0)

OpenSEES_Program = tk.Entry(frame2, width=20)
OpenSEES_Program.grid(row=1, column=1)
OpenSEES_Program.insert(tk.END, r"C:\Program Files\OpenSEES")
tk.Label(frame2, width=20, text="OpenSEES Saved Here", anchor='e').grid(row=1, column=0)


def runFDS():
    y = 'cmd /k "fdsinit & fds_local -p {} -o {} {}.fds"'.format(MPI.get(), CORES.get(), FDS_FILE.get())
    os.system(y)


tk.Button(window2, text="Run FDS", command=runFDS, width=15, height=1).grid(row=2, column=0, padx=5, pady=5)


def runOpenSEES():
    process = subprocess.Popen(["{0}\OpenSees.exe".format(OpenSEES_Program.get())], stdin=subprocess.PIPE, text=True)
    process.communicate(os.linesep.join(["source {0}.tcl".format(OpenSEES_FILE.get())]))


tk.Button(window2, text="Run OpenSEES", command=runOpenSEES, width=15, height=1).grid(row=3, column=0, padx=5, pady=5)

window2.mainloop()
