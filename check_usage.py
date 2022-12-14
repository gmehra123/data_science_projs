import os
def check_reboot:
	"""Returns True if the computer has a pending reboot"""
	return os.path.exist("/run/reboot_required")

def main():
	if check_reboot():
		print("pending reboot.")
		sys.exit(1)

main()