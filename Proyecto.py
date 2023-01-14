import pexpect

devices = {'iosv-1': {'prompt': 'iosv-1#', 'ip': '172.16.1.20'},
            'iosv-2': {'prompt': 'iosv-2#', 'ip': '172.16.1.21'}}
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
	    #print(child.before)
	    text+= str(child.before, "UTF-8")+"\n\n"
	    child.sendline('exit')
	return text