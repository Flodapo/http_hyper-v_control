This Project is kind of 2 Parts. 

  1. The Hyper-V Host
  2. The "Clients" that call the HTTP Requests

I use it for Home Assistant but it works via HTTP GET so you can use it in many diffrent ways.
It supports 
  - Stoping a VM
  - Starting a VM
  - Checking the Status of a VM

The action and the Name of the VM are configured from the 2. Part (The "Client")
like this:        Start a VM: http://<server-ip>:8080?action=start&vm=YourVMName
                  Stop a VM: http://<server-ip>:8080?action=stop&vm=YourVMName
                  Check status: http://<server-ip>:8080?action=status&vm=YourVMName


For Home Assistant put this in configuration.yaml:
Start / Stop:
rest_command:
  start_vm:
    url: "http://<IP OF HYPER-V HOST>:8080?action=start&vm={{ vm_name }}"
  stop_vm:
    url: "http://<IP OF HYPER-V HOST>:8080?action=stop&vm={{ vm_name }}"
  check_vm_status:
    url: "http://<IP OF HYPER-V HOST>:8080?action=status&vm={{ vm_name }}"




Status:

  sensor:
    - platform: rest
      name: HyperV VM Status
      resource: "http://<server-ip>:8080?action=status&vm=YourVMName"
      value_template: "{{ value_json.status }}"
      scan_interval: 30
