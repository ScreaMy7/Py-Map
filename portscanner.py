#/usr/bin/python3
from concurrent.futures import thread
import threading #module for multi-threading
import argparse #module for parsing command line arguments
import socket #module for socket
import queue 
import time
import nmap
import pandas as pd


parser= argparse.ArgumentParser()
start_time= time.time()

parser.add_argument("-host",help="Host to scan",dest="host")
parser.add_argument("-ports", help="list of ports to scan",dest="ports")
parser.add_argument("-nmap" ,help="second number", dest='nmap',nargs='?',const=False)
parser.add_argument("-cli" ,help="nmap cli ", dest='cli',nargs='?',const=False)
#parser.add_argument("-UDP", help="for a udp scan",dest="UDP", nargs='?',default=False)
args = parser.parse_args() #arguments to be parsed

#constants
ports =(args.ports.split("-"))
host=args.host
result=[]
queue= queue.Queue()

#Fancy banner :p
print ('''\033[1;34m______                ___  ___              
| ___ \               |  \/  |              
| |_/ / _   _  ______ | .  . |  __ _  _ __  
|  __/ | | | ||______|| |\/| | / _` || '_ \ 
| |    | |_| |        | |  | || (_| || |_) |
\_|     \__, |        \_|  |_/ \__,_|| .__/ 
         __/ |                       | |    
        |___/                        |_|    
                            -  coded with \033[31m <3\033[00m \033[34m by ScreaMy    \033[1;m''')
print ('\033[1;33m--------------------------------------------------------------------------\033[1;m\n')

try:
        print("\033[96mChecking if hostname resolves....\033[1;m")
        print("\033[92mDone\033[1;m\n")
        hostname= socket.gethostbyname(host)
except socket.gaierror:
        print("\033[31mFailed to resolve to Hostname.")
        exit()

def socket_scan(port):
    try:        
        conn_soc= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        conn_soc.settimeout(0.30)
        soc= conn_soc.connect_ex((hostname,port))
        if (not soc):
            conn_soc.close()  
            return True
        else:
            conn_soc.close()  
            return False    
    except:
        print('Could not connect to host. Try again.') 

def fill_queue(sp,ep):
    for port in range(sp,ep+1):
        queue.put(port)

def worker():
    while not queue.empty():
        port=queue.get()
        if socket_scan(port):
            print(f"Port {port} is open")
            result.append(port)
        queue.task_done()

def nmap_integrate(argument):     
    print("\n\033[96mRunning nmap on:\033[1;m",hostname)
    nm = nmap.PortScanner()
    scan=nm.scan(host,arguments=argument)
    print("\033[92mRunning nmap command $ \033[1;m",scan['nmap']['command_line'])
    ans=pd.DataFrame(scan['scan'][hostname]['tcp']).T.drop(columns=['extrainfo','conf','cpe'],axis=1).reset_index().rename({'index':'Port'},axis=1)
    print(ans)
    end_time= time.time()
    print("Total elapsed time:",(end_time-start_time),"s")
  

def main():
    if(args.host==None or args.ports==None):
        exit()
    print("\033[96mScanning Host:\033[1;m",host)

    start_port= int(ports[0])
    end_port= int(ports[1])
    print(f"\033[96mScanning from: {start_port} to {end_port} \033[1;m")
    fill_queue(start_port,end_port)
    thread_list=[]  #creating new threads
    for t in range(50):
        thread=threading.Thread(target=worker)
        thread_list.append(thread)
    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()
    
    if args.nmap is not None:   # default to run nmap on open ports
        p=','.join([str(x) for x in result])
        argument='-sV -sS -p'+p
        nmap_integrate(argument)
    if args.cli is not None:   # to use nmap from cli
        nmap_integrate(args.cli)
    else:
        exit()
    

    
if __name__ == '__main__':
    main()