from capture_devices import devices

def listDevices(type):
    devices_ = devices.run_with_param(device_type=type, result_=True )
    devices_list = [device.replace('DEVICE NAME : ', '') for device in devices_]
    devices_.clear()  # Limpa a lista de dispositivos
    return devices_list