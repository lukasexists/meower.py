# Demo Meower client using meower.py
from meower import meower

for i in range(0, meower.home_len()):
	print(meower.get_post(meower.find_post(i)))
