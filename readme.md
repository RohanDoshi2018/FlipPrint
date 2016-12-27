Written By: Rohan Doshi

FlipPrint
Double-sided printing with a single-sided printer.

Printing long documents with double-sided printing prevents paper waste. However, printing double-sided documents with a single-sided printer is often confusing - nobody wants to read confusing, wordy descriptions, anually seperate and reverse pages, or run the risk of inserting pages into the printer incorrectly. This app is meant to simplify this process by providing a simple visual guide that automatically splits and rearranges documents into two halves. We take the thinking out of printing.


Web-app flow:
First, the user selects his type of printer (to enable us to customize the instructions) and uploads a file to the server. The server then splits this file into two new PDF files. The client then follows instructions and clicks on links to print these two server-side files (by loading PDF files into invisible iframes).

Design Decision 1: Flask-framework Backend
1) Ease of setting up server-side endpoints for file uploads
1) Ease of connecting to Python libraries for PDF manipulation (e.g. pdfrw)

Design Decision 2: No JavaScript Front-end Framework
1) Adds unecessary complexity to a web-app with only three pages
2) jQuery is sufficient for handling HTTP POST/GET request to Flask Backend

Other Development Considerations
1) Security - Need to prevent unauthorized access of static documents via Flask server endpoints


