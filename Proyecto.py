import pexpect

#Se guardan las etiquetas e ip's de cada router
devices = {'R1': {'prompt': 'R1#', 'ip': '192.168.1.1'},
          	'R2': {'prompt': 'R2#', 'ip': '172.16.1.2'},
          	'R3': {'prompt': 'R3#', 'ip': '172.16.1.6'},
          	'R4': {'prompt': 'R4#', 'ip': '172.16.1.14'},
          	'R5': {'prompt': 'R5#', 'ip': '172.16.1.18'},
          	'R6': {'prompt': 'R6#', 'ip': '172.16.0.2'},}

username = 'cisco' #Usuario
password = 'cisco' #Contrasenia

#Fucion para ejecutar un comando a traves de Telnet
def executeCommand(command): #Recibe el comando (string) como parametro
	text = "" #Variable que contiene la respuesta del comando
	for device in devices.keys(): #Se itera cada router
		device_prompt = devices[device]['prompt'] #Se guarda la etiqueta de cada router
		child = pexpect.spawn('telnet ' + devices[device]['ip']) #Se hace la conexion por Telnet
		child.expect('Username:') #Se espera el usuario
		child.sendline(username) #Se ingresa el usuario
		child.expect('Password:') #Se espera por la contrasenia
		child.sendline(password) #Se ingresa la contrasenia
		child.expect(device_prompt) #Se espera por la etiqueta del router
		text+=device_prompt+"\n" #Se guarda la etiqueta del router en la respuesta
		child.sendline('terminal length 0') #Se elimina la opcion --more-- al ejecutar un comando largo
		child.expect(device_prompt) #Se espera por la etiqueta del router
		child.sendline(command) #Se envia el comando
		child.expect(device_prompt) #Se espera por la etiqueta del router
		text+= str(child.before, "UTF-8")+"\n\n" #Se obtiene la respuesta y se convierte a string
		child.sendline('exit') #Se cierra la sesion de telnet
	return text #Se devuelve toda la respuesta obtenida de todos los routers