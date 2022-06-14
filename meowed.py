# Demo Meower client using meower.py
import meower

page = 1
meower.change_page(1)

while(meower.page_len() != page):
	for i in range(0, meower.home_len()):
		print(meower.get_post(meower.post_id(i)))
	page += 1
	meower.change_page(page)