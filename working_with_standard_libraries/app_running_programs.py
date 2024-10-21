import subprocess

# Legacy methods
# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen

subprocess.run(['dir'], shell=True, check=True)
