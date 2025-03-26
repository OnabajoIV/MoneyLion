import re

with open("extraction.txt", "r") as file:
    for line in file:
        if "coderbyte heroku/router" in line: # Check if the line contains the heroku router log
            request_id_match = re.search(r'request_id=([\w-]+)', line) #  Extracting the request_id using regex
            fwd_match = re.search(r'fwd="([^"]+)"', line) # Extract the fwd field using regex (value inside quotes)


            if request_id_match: #  this should continue only if request_id is found
                request_id = request_id_match.group(1) # Get the request_id string from the match
                is_masked = fwd_match and fwd_match.group(1) == "MASKED" # This should check if fwd exists and is equal to "MASKED"

                if is_masked:
                    print(f"{request_id} [M]") # if masked, will print request id with [M]
                else:
                    print(request_id) #if not masked, will print just request id