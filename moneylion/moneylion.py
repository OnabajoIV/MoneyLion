import re

with open("extraction", "r") as file:
    for line in file:
        if "coderbyte heroku/router" in line:
            request_id_match = re.search(r'request_id=([\w-]+)', line)
            fwd_match = re.search(r'fwd="([^"]+)"', line)

            if request_id_match:
                request_id = request_id_match.group(1)
                is_masked = fwd_match and fwd_match.group(1) == "MASKED"

                if is_masked:
                    print(f"{request_id} [M]")
                else:
                    print(request_id)
