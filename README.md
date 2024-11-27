(View the raw README.md to copy code)

This Project is kind of 2 Parts. 

  1. The Hyper-V Host
  2. The "Clients" that call the HTTP Requests

I use it for Home Assistant but it works via HTTP GET so you can use it in many diffrent ways.
It supports 
  - Stoping a VM
  - Starting a VM
  - Checking the Status of a VM

The action and the Name of the VM are configured from the 2. Part (The "Client")
like this:        
                  - Start a VM: http://<server-ip>:8080?action=start&vm=YourVMName
                  - Stop a VM: http://<server-ip>:8080?action=stop&vm=YourVMName
                  - Check status: http://<server-ip>:8080?action=status&vm=YourVMName


For Home Assistant put this in configuration.yaml:
Start / Stop:

rest_command:
  start_vm:
    url: "http://<server-ip>:8080?action=start&vm={{ vm_name }}"
  stop_vm:
    url: "http://<server-ip>:8080?action=stop&vm={{ vm_name }}"
  check_vm_status:
    url: "http://<server-ip>:8080?action=status&vm={{ vm_name }}"

Status:

sensor:
  - platform: rest
    name: HyperV VM Status
    resource: "http://<server-ip>:8080?action=status&vm=YourVMName"
    value_template: "{{ value_json.status }}"
    scan_interval: 30

You need to put your Hyper-V Host IP at <server-ip>



The VM Name can be set from the rest service call like this for Start / Stop:

action: rest_command.start_vm
metadata: {}
data:
  vm_name: YourVMName

action: rest_command.stop_vm
metadata: {}
data:
  vm_name: YourVMName


You have to set YourVMName in the Automations and in the Status in configuration.yaml.




There is a batch file in the Hyper-V Host folder that you can use for starting the HTTP Server at will. You need the file to be run as admin. If you want to start it at boot use the windows Task Planer. (that is i do it but you may know a better way)
