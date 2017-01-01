# FlipPrint
### Double-sided printing with a single-sided printer.
Created By: Rohan Doshi

Demo: http://flipprint.pythonanywhere.com

Double-sided printing of long PDF documents prevents paper waste. However, printing double-sided documents with a single-sided printer is often confusing. Nobody wants to:

1. Read confusing, wordy instructions
2. Manually separate even and odd pages 
3. Figure out whether to reverse the ordering of the even or odd pages
4. Accidentally insert pages into the printer in the wrong orientation
This app is meant to simplify this process by providing a simple visual guide that automatically splits and rearranges documents into two halves. This app take the thinking out of printing.

#### Web-app flow:
First, the user selects his type of printer (to enable the app to customize the instructions to either inkjet or laser printer designs). Then, the user uploads a PDF file to the server. The server then splits this file into two new, temporary PDF files. The user then follows instructions and clicks on links to directly print these two server-side files (by loading PDF files into invisible iframes via the print.js library).

#### How to Run
1. Change your directory to the folder holding server.py. 
2. Launch the flask server using the bash command: python server.py
3. Open the app by navigating to http://127.0.0.1:5000/ on a web-browser (e.g. Google Chrome)

#### Design Decision 1: Flask-framework Backend
1. Simplicity of setting up server-side endpoints for file uploads
2. Python libraries were better than JavaScript libraries for PDF manipulation (we ended up using the pdfrw library)

#### Design Decision 2: No JavaScript Front-end Framework
1. A full-on JavaScript framework (e.g. Angular.js) was unnecessary complex for a web-app with only three views
2. jQuery is sufficient for handling HTTP POST/GET request to the Flask backend

#### Other  Considerations:
1. Memory - Given limited server-side memory (~4 GB), my server-side code automatically deletes the two temporary server-side PDF files for each upload upon the closing of the client (through a call to the /delete endpoint). This is enabled by generating a 32-bit unique ID that maps each client browser instance to the two corresponding server-side PDF files.
2. Security - I need to prevent unauthorized access of static documents via Flask server endpoints. Thus, any PDF documents to my server must remain confidential and not publically accessible.

#### Credit
1. print.js (http://printjs.crabbly.com/): A tiny JavaScript library to help printing from the web
2. pdfrw (https://github.com/pmaupin/pdfrw): pdfrw is a pure Python library that reads and writes PDFs