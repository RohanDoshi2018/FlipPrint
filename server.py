import os
import json
from flask import Flask, request, render_template, redirect
from werkzeug.utils import secure_filename
from pdfrw import PdfReader, PdfWriter

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/uploads/'

@app.route("/")
def index():
	return app.send_static_file('index.html')

@app.route("/upload", methods=['POST'])
def upload():
	file = request.files['file']
	pages = PdfReader(file).pages
	num_pages = len(pages)

	if request.form['printer_type'] == "inkjet":
		odd_range = list(range(1,num_pages+1,2))
		even_range = list(range(2,num_pages+1,2))

		odddata = PdfWriter()
		for odd in odd_range:
		    odddata.addpage(pages[odd-1])
		odddata.write('static/temp/' + request.form['id'] + '_odd.pdf')

		evendata = PdfWriter()
		if num_pages % 2 == 1:
		    blank_page = PdfReader('static/blank.pdf').pages
		    evendata.addpage(blank_page[0])
		for even in even_range[::-1]:
		    evendata.addpage(pages[even-1])
		evendata.write('static/temp/' + request.form['id']  + '_even.pdf')
	elif request.form['printer_type'] == "laser": # incorrect
		odd_range = list(range(1,num_pages+1,2))
		even_range = list(range(2,num_pages+1,2))

		odddata = PdfWriter()
		for odd in odd_range[::-1]:
		    odddata.addpage(pages[odd-1])
		odddata.write('static/temp/' + request.form['id'] + '_odd.pdf')

		evendata = PdfWriter()
		for even in even_range:
		    evendata.addpage(pages[even-1])
		if num_pages % 2 == 1:
		    blank_page = PdfReader('static/blank.pdf').pages
		    evendata.addpage(blank_page[0])
		evendata.write('static/temp/' + request.form['id']  + '_even.pdf')	

	return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/<path:path>')
def static_proxy(path):
	# send_static_file will guess the correct MIME type
	return app.send_static_file(path)

@app.route("/delete", methods=['POST'])
def delete():
	odd_path = 'static/temp/' + request.json['id'] + '_odd.pdf'
	even_path = 'static/temp/' + request.json['id'] + '_even.pdf'
	try:
		os.remove(odd_path)
		os.remove(even_path)
	except:
		pass
	return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

if __name__ == "__main__":
	app.debug = True
	app.run()
	app.run(debug = True)


