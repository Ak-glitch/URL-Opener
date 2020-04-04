import webbrowser
c = webbrowser.get('google-chrome')
file_url= open("/home/ak/Desktop/testing_urls.txt","r")
for k in file_url:
	k=k[:]
	c.open_new_tab(k)

#Created by Ak