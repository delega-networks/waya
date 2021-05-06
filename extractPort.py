#!/usr/bin/python3
#

import shlex

from subprocess import Popen, PIPE
import xml.etree.ElementTree as ET

def executor(command):
    try:
        args = shlex.split(command)
        p = Popen(args, stdout=PIPE, stderr=PIPE)
        return p
    except Exception as e:
        print(e)

def parseXML(path, name):
    print("[!] Parseando XML")
    tree = ET.parse(path)
    root = tree.getroot()
    for host in root.findall('host'):
      result=""
      ip = host.find('address')
      ports = host.find('ports')
      portList = ports.findall('port')
      for port in portList:
         result += str(port.attrib['portid'])+" "
      return name+";"+str(ip.attrib['addr'])+";"+result+"\n"

# Escaneo, si se quiere hacer mas ruido "--min-rate 3000" 
# Por defecto "-sS" da igual que no se ponga
# Para escanear todos los puertos (elefante en una cacharrería) "-sS -p0-65535" EJ: "nmap -sS -p0-65535 --min-rate 3000 -Pn --open {ip} -oX {path}"
# Para menos ruido "-T3", "-T2", "-T1"
# Las opciones "-T" son incompatibles con "--min-rates"
# Si se satura la maquina bajar --min-rate
# "-Pn" no comprueba si ICMP esta abierto
# "--open" para q saque solo los abiertos
# Ver mas info nmap en https://www.stationx.net/nmap-cheat-sheet/
def findPorts(path, ip):
    print(f"[!] Escaneando puertos ({ip})")
    # Modificar por el escaneo que se quiera utilizar
    command = f"sudo nmap --top-ports 1000 -T5 -Pn --open {ip} -oX {path}"
    result = executor(command)
    result.stdout.read()
    return ""

dataCSV = "NAME;IP;PORTS\n"

# Usa output.txt y lo llama output, lee cada línea y la guarda como data
with open('output.txt', 'r') as output:
    data = output.readlines()
    for line in data:
        if line != "\n":
            name = line.split("'")[1]
            ip = line.split("'")[3]
            path=f"./scans/{ip}.xml"
            findPorts(path, ip)
            dataCSV += parseXML(path, name)

with open('output.csv', 'w') as result:
    result.write(dataCSV)