#!/usr/bin/python3

#System Health
import os
from system_health import *

def main_menu():
	print("Enter 1 for Display available RAM")
	print("Enter 2 for Display Load avearge")
	print("Enter 3 for Display Hostname details")
	print("Enter 4 for Display All process count")
	print("Enter 5 for Display uptime")
	print("Enter 6 for Exit")
	
while True:
	main_menu()
	ch=int(input("Enter your choice : "))
	if ch == 1:
		display_available_ram()
	elif ch == 2:
		display_load_avg()
	elif ch == 3:
		display_host_details()
	elif ch == 4:
		display_all_process_c()
	elif ch == 5:
		display_uptime()
	elif ch == 6:
		break
	else:
		print("Invalid choice")

