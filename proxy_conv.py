import re
#import tkinter as tk
#from tkinter import filedialog
#root = tk.Tk()
#root.withdraw()
#file = filedialog.askopenfilenames()[0]
file="scan.txt"
t = open(file).readlines()
#rf=open("scan.txt",'r')
wf=open("ss.txt",'w')
#t=rf.readlines()
ip_patt="([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})?"
def ip_re(s):
    if len(re.findall(ip_patt+'\s[0-9]{1,5}(\s|,)',s))>0:
        return re.findall(ip_patt,s)[0]
    else:
        return None
def enter(st):
    st=st.replace("\r","")
    st=st.replace("\n","")
    if "," in st:
        if len(re.findall(ip_patt+'\s[0-9]{1,5},',st))>0 and len(re.findall(",",st))>0:
            ip=ip_re(st)
            port1=re.findall("([0-9]{1,5}),",st)[0]
            #print(str(ip)+":"+str(port1))
            wf.write((str(ip)+":"+str(port1))+"\n")
            for port in re.findall(",([0-9]{1,5})",st):
                #print (str(ip)+":"+str(port))
                wf.write((str(ip)+":"+str(port))+"\n")
    else:
        if len(re.findall(ip_patt+'\s[0-9]{1,5}\s',st))>0:
            ip=ip_re(st)
            port1=re.findall(" ([0-9]{1,5})",st)[0]
            #print(str(ip)+":"+str(port1))
            wf.write((str(ip)+":"+str(port1))+"\n")
for string in t:
    enter(string)
wf.close()
