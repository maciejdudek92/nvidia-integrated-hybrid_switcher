import subprocess


def screens():
    command = subprocess.run(
        "hwinfo --monitor | grep -E 'Model:|Serial ID:'",
        shell=True,
        capture_output=True,
        text=True,
    )
    output = [l for l in command.stdout.splitlines()]
    monitors = []

    for i in range(len(output)):
        if not "Model:" in output[i]:
            continue

        model_line = output[i].replace(" ", "").split(":")[1]
        serial_line = output[i + 1].replace(" ", "").split(":")[1]

        monitors.append(
            {
                "Model": model_line,
                "Serial": serial_line,
            }
        )
    return monitors


def get_current_graphic_mode():
    return subprocess.run(
        "supergfxctl -g",
        shell=True,
        capture_output=True,
        text=True,
    ).stdout


def set_graphic_mode(mode: str):
    """Integrated, Hybrid"""
    return subprocess.run(
        f"supergfxctl -m {mode}",
        shell=True,
        capture_output=True,
        text=True,
    ).stdout


current_mode = get_current_graphic_mode()
is_monitor_connected = False
screens = screens()

if len(screens) > 0:
    is_monitor_connected = True
else:
    if screens[0]["Serial"] != "0":
        is_monitor_connected = True

if is_monitor_connected and current_mode == "Integrated":
    set_graphic_mode("Hybrid")
if not is_monitor_connected and current_mode == "Hybrid":
    set_graphic_mode("Integrated")
