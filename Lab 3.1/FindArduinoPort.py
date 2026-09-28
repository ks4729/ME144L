import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port in ports:
    if "Arduino" in port.description:
        print(f"Arduino found on port: {port.device}")