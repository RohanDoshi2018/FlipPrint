# FlipPrint
### Double-sided printing with a single-sided printer.
Created By: Rohan Doshi

Double-sided printing of long PDF documents prevents paper waste. However, printing double-sided documents with a single-sided printer is often confusing. Nobody wants to:

1. Read confusing, wordy instructions
2. Manually seperate even and odd pages 
3. Figure out whether to reverse the ordering of the even or odd pages
4. Accidentally insert pages into the printer in the wrong orientation
This app is meant to simplify this process by providing a simple visual guide that automatically splits and rearranges documents into two halves. This app take the thinking out of printing.

#### Web-app flow:
First, the user selects his type of printer (to enable the app to customize the instructions to either inkjet or laser printer designs). Then, the user uploads a PDF file to the server. The server then splits this file into two new, temporary PDF files. The user then follows instructions and clicks on links to directly print these two server-side files (by loading PDF files into invisible iframes via the print.js library).

#### Design Decision 1: Flask-framework Backend
1. Ease of setting up server-side endpoints for file uploads
2. Ease of connecting to Python libraries for PDF manipulation (e.g. pdfrw)

#### Design Decision 2: No JavaScript Front-end Framework
1. Adds unecessary complexity to a web-app with only three pages
2. jQuery is sufficient for handling HTTP POST/GET request to the Flask backend

#### Other  Considerations:
1. Memory - Given limited and temporary server-side memory (~4 GB), my server-side code automatically deletes the two temporary server-side PDf files for each upload upon the closing of the client (through a call to the /delete endpoint). This is enabled by generating a 32-bit unique ID that maps each client browser instance to two server-side temporary files.
2. Security - Need to prevent unauthorized access of static documents via Flask server endpoints.

#### Credit
1. print.js (http://printjs.crabbly.com/): A tiny javascript library to help printing from the web
2. pdfrw (https://github.com/pmaupin/pdfrw): pdfrw is a pure Python library that reads and writes PDFs