# MoneyLion

Web Log Extraction — Coderbyte Challenge
Objective -
The goal of this script is to:

Parse a set of web server logs.

Identify all log lines that contain the phrase coderbyte heroku/router.

Extract the request_id from each matching line.

Print the request_id, and if the fwd field is "MASKED", append [M] to the output.


What this code does - 
Opens the log file extraction for reading.

Loops through each line, checking for the presence of coderbyte heroku/router.

Uses regular expressions to extract:

request_id using the pattern request_id=([\w-]+)

fwd value using fwd="([^"]+)"

Prints the request_id:

If fwd is "MASKED", it adds [M] to the end.


Mistakes & Fixes - 

I wrapped the request in a try/except block because I was trying to initially use the live URL which simulates a real-world scenario more accurately, thinking about the http requests and how they could be unreliable. I was able to fix this by writing a direct function with open while saving the file locally in order to test the accuracy of my code and output.

I intended to write a code that anticipates failure in general and did not focus on the immediate output given the time crunch and criticality. I felt it was not just about solving the code but making sure the system can keep itself steady when things go wrong.