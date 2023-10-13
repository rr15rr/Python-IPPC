#Este proyecto utiliza el modulo de "sockets" para sacar la IP y el nombre del PC del usuario

import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("El nombre de tu PC es: " + hostname)
print("Tu direccion IP es: " + ip)
print("Gracias")