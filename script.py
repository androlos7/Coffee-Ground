from colorama import Fore, Style #For color

logo = """
                                                                                                                                                                                 
                                             .                                            
                                            =.                                            
                                            +=                                            
                                             **.                                          
                                        .     -#=                                         
                                       *       .**                                        
                                       =*        *+                                       
                                        -#-      .%                                       
                                         .#*      %                                       
                                           #=    -:                                       
                                           -+                                             
                                           =.                                             
                                ::::::::::::::::::::::::::.                               
                               =%------------------------%+                               
                          -----*%========================%*-----                          
                          #+::::::::::::::::::::::::::::::::::+%                          
                          #=                                  =%                          
                          *##********************************###                          
                           :%:                              .%:                           
                            %=                              -%                            
                            *#                              **                            
                            -%.                             %=                            
                            .%#*****************************%.                            
                             #*                            +#                             
                             =%    .- =             + =.   #+                             
                             :%:   *+ #+     :     +# *#  .%-                             
                              %=   %+ ##  .*#.:=   ## *%  =%                              
                              +#   *+ #+ :%* =%:   =# **  **                              
                              -%.   : -  *- *#:     : :   %=                              
                               %-          =-            :%.                              
                               #*                        +#                               
                               =%************************%+                               
                               .%:                      .%:                               
                                %+                      =%                                
                                +#                      **                                
                                -%.                     %=                                
                                 #**********************#.                                
                                                                                
"""

print(logo)

print(f"{Fore.GREEN}Welcome to Coffee Ground. Grab your coffee and check your IP and other stuff with just one click.{Style.RESET_ALL}")

#OS and Device Info

import locale
import os

language = locale.getdefaultlocale()[0]
os_name = os.name

print(f"Language OS System: {language}")
print(f"Name of the OS System: {os_name}")


import platform

system_info = platform.system()
node_name = platform.node()

print(f"OS System: {system_info}")
print(f"Device Name: {node_name}")

#CPU Information

import platform

processor_info = platform.processor()
print(f"CPU: {processor_info}")

#local Network Info

import socket
import uuid

def get_mac_address():
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(2, 7)][::-1])
    return mac

def get_ip_address():
    ip = socket.gethostbyname(socket.gethostname())
    return ip

print(f"MAC-Address: {get_mac_address()}")
print(f"IP-Address: {get_ip_address()}")

#Public IP Adress Info

import requests

def get_public_ip():
    response = requests.get("https://api.ipify.org?format=json")
    public_ip = response.json()["ip"]
    return public_ip

print(f"Public IP Address: {get_public_ip()}")
