import pexpect



devices = {'R1': {'prompt': 'R1#', 'ip': '192.168.1.1'},

          	'R2': {'prompt': 'R2#', 'ip': '172.16.1.2'},

          	'R3': {'prompt': 'R3#', 'ip': '172.16.1.6'},

          	'R4': {'prompt': 'R4#', 'ip': '172.16.1.14'},

          	'R5': {'prompt': 'R5#', 'ip': '172.16.1.18'},

          	'R6': {'prompt': 'R6#', 'ip': '172.16.0.2'},}

username = 'cisco'

password = 'cisco'





def confRouter():

	text = ""

	for device in devices.keys():

		device_prompt = devices[device]['prompt']

		child = pexpect.spawn('telnet ' + devices[device]['ip'])

		child.expect('Username:')

		child.sendline(username)

		child.expect('Password:')

		child.sendline(password)

		child.expect(device_prompt)

		text+=device_prompt+"\n"

		child.sendline('terminal length 0')  

		child.expect(device_prompt) 

		child.sendline('show ip int brief')

		child.expect(device_prompt)

		text+= str(child.before, "UTF-8")+"\n\n"

		child.sendline('exit')

	return text

	

def confACL():

	text = ""

	for device in devices.keys():

		device_prompt = devices[device]['prompt']

		child = pexpect.spawn('telnet ' + devices[device]['ip'])

		child.expect('Username:')

		child.sendline(username)

		child.expect('Password:')

		child.sendline(password)

		child.expect(device_prompt)

		text+=device_prompt+"\n"

		child.sendline('terminal length 0')  

		child.expect(device_prompt) 

		child.sendline('show access-list')

		child.expect(device_prompt)

		text+= str(child.before, "UTF-8")+"\n\n"

		child.sendline('exit')

	return text

	

def confNAT():

	text = ""

	for device in devices.keys():

		device_prompt = devices[device]['prompt']

		child = pexpect.spawn('telnet ' + devices[device]['ip'])

		child.expect('Username:')

		child.sendline(username)

		child.expect('Password:')

		child.sendline(password)

		child.expect(device_prompt)

		text+=device_prompt+"\n"

		child.sendline('terminal length 0')  

		child.expect(device_prompt) 

		child.sendline('show ip nat translation')

		child.expect(device_prompt)

		text+= str(child.before, "UTF-8")+"\n\n"

		child.sendline('exit')

	return text

	

	

def confEnrut():

	text = ""

	for device in devices.keys():

		device_prompt = devices[device]['prompt']

		child = pexpect.spawn('telnet ' + devices[device]['ip'])

		child.expect('Username:')

		child.sendline(username)

		child.expect('Password:')

		child.sendline(password)

		child.expect(device_prompt)

		text+=device_prompt+"\n"

		child.sendline('terminal length 0')  

		child.expect(device_prompt) 

		child.sendline('show ip rou')

		child.expect(device_prompt)

		text+= str(child.before, "UTF-8")+"\n\n"

		child.sendline('exit')

	return text	

	