
```markdown
# Hyper-V VM Control via HTTP

This project allows you to control Hyper-V VMs via HTTP requests. It has two main parts:

1. **The Hyper-V Host:** Runs the Python script and acts as the server.
2. **The Clients:** Send HTTP requests to control or query the status of VMs.

## Features

The system supports the following actions:
- **Start a VM**
- **Stop a VM**
- **Check the status of a VM**

The requests are made using HTTP GET, allowing integration with a wide range of systems, including Home Assistant.

## Setup

### Requirements

- Python must be installed on the Hyper-V host.

### HTTP Endpoints

You can perform actions on a VM by sending HTTP GET requests to the server:

- **Start a VM:**  
  `http://<server-ip>:8080?action=start&vm=YourVMName`

- **Stop a VM:**  
  `http://<server-ip>:8080?action=stop&vm=YourVMName`

- **Check status:**  
  `http://<server-ip>:8080?action=status&vm=YourVMName`

Replace `<server-ip>` with the IP address of your Hyper-V host.

---

## Home Assistant Integration

You can use this project with Home Assistant. Add the following configurations to your `configuration.yaml`:

### Start/Stop Commands

```yaml
rest_command:
  start_vm:
    url: "http://<server-ip>:8080?action=start&vm={{ vm_name }}"
  stop_vm:
    url: "http://<server-ip>:8080?action=stop&vm={{ vm_name }}"
  check_vm_status:
    url: "http://<server-ip>:8080?action=status&vm={{ vm_name }}"
```

### Status Sensor

```yaml
sensor:
  - platform: rest
    name: HyperV VM Status
    resource: "http://<server-ip>:8080?action=status&vm=YourVMName"
    value_template: "{{ value_json.status }}"
    scan_interval: 30
```

> **Note:** Replace `<server-ip>` with the IP address of your Hyper-V host and `YourVMName` with the name of your VM.

---

### Example Automations for Home Assistant

Use the following examples to call the `start_vm` and `stop_vm` services:

#### Start a VM

```yaml
action:
  - service: rest_command.start_vm
    data:
      vm_name: YourVMName
```

#### Stop a VM

```yaml
action:
  - service: rest_command.stop_vm
    data:
      vm_name: YourVMName
```

> **Note:** Replace `YourVMName` with the actual name of your VM in both the automations and the status sensor configuration.

---

## Running the HTTP Server

A batch file is included in the `Hyper-V Host` folder to start the HTTP server. Follow these steps:

1. Run the batch file as an administrator to start the server.
2. To start the server automatically at boot, use the Windows Task Scheduler.

---

## Contributing

Feel free to submit issues or feature requests via the [GitHub repository](https://github.com/your-repo-link). Contributions are welcome!

---



---

Happy automating!
```
