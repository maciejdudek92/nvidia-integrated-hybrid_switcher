import subprocess

def screens():
    command = subprocess.run(
        "hwinfo --monitor | grep -E 'Model:'",
        shell=True,
        capture_output=True,
        text=True,
    )
    output = [l for l in command.stdout.splitlines()]
    monitors = []

    for i in range(len(output)):
        model_line = output[i].replace(" ", "").split(":")[1]

        monitors.append(model_line)
    return monitors

def set_graphic_mode(mode: str):
    """Integrated, Hybrid"""
    return subprocess.run(
        f"supergfxctl -m {mode}",
        shell=True,
        capture_output=True,
        text=True,
    ).stdout
    
def stop_supergfxd():
    """Integrated, Hybrid"""
    return subprocess.run(
        "systemctl stop supergfxd.service",
        shell=True,
        capture_output=True,
        text=True,
    )  
  
def get_vga_controllers():
    command = subprocess.run(
    "lspci | grep VGA",
    shell=True,
    capture_output=True,
    text=True,
)
    vga_controllers = [l for l in command.stdout.splitlines()]
    print(vga_controllers)
    return len(vga_controllers)

if get_vga_controllers() > 1:
    set_graphic_mode("Hybrid")

    is_monitor_connected = False
    screens = screens()
    screens_count = len(screens)

    if screens_count > 1:
        is_monitor_connected = True
        
    if not is_monitor_connected:
        set_graphic_mode("Integrated")
else:
    stop_supergfxd()
