# SciexShimadzuPressureTrace
Short script utilizing @frida to log pump pressure from a Shimadzu Nexera X2 LC coupled to a ABSciex 6500 qtrap, running analyst 1.6.2.

This script is provided as-is and you run it at your own risk. I've tested it as much as I am able to test, but I only have one instrument configuartion available to me. Different hardware/software may work differently.

Python 3.6.5 can be installed from: https://www.python.org/
During the python install process I believe there is an option to install pip. If there isn't, or you forget to check it, you can install pip by following directions here: https://pip.pypa.io/en/stable/installing/

Once python and pip are installed, you should just be able to open a command prompt (winkey+r, type 'cmd', hit enter) and type: 
```
pip install frida
```
Hit enter and frida should install. More information is available here: https://www.frida.re/docs/installation/

Once that's done, you'll want to create a new file on your computer and name it 'whateveryouwant.py'. Open the file with your favorite text editor and copy/paste the code from the .py file on this repository to your file, and save. By default, the script will save text files with the pressure entries in the same location as the script. If you want to supply your own path, you can change the ```'filepath = ""'``` line to something like ```'filepath = "D:/Pressure Logs"``` for example.

Make sure analyst.exe is running, make sure there is an active hardware profile, and make sure you aren't acquiring anything important in case something bad happens. 

Run the .py file (you should be able to double click it). If everything works, a command prompt should open with output similar to:
```
viutlu.dll baseAddr: 0x12345678
get status address: 0x23456789
Collecting Pressure data. Press enter to stop.
```

And a .txt file named "Pressure Log yyyymmdd-hhmmss.txt" should be generated. After a few seconds, you should be able to open the text file and see entries similar to:
```
Datetime, Pressure 
2018-06-11 17:47:11,12.94
2018-06-11 17:47:14,16.64
2018-06-11 17:47:17,12.94
2018-06-11 17:47:20,14.79
```

If the script does not work, or produces garbage information, then some custom reversing will likely be required to get the script to work on your particular setup. This might be really straight forward or really complicated, depending on changes in software, etc. 


