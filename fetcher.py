import urllib.request
from fetcher_core import *
fcb()
def get_url():
    fcc()
    UNAME = input("ENTER UNAME: ")
    PASS = input("ENTER PASS: ")

    VALID_UNAME = "vinay"
    VALID_PASS = "vinayj@123"

    # Check username first
    if UNAME != VALID_UNAME:
        print("INVALID UNAME!, PROGRAM IS TERMINATED!!")
        exit()

    # Then check password
    elif PASS != VALID_PASS:
        print("INVALID PASS!, PROGRAM IS TERMINATED!!")
        exit()

    else:
        URL = input("Enter Target URL (including http/https): ")
        filename = input("Enter Filename (including file extension): ")
        print("The Target URL is " + URL)
        print("The Filename is " + filename)
        
        try:
            # Construct the full URL
            full_url = URL if URL.endswith('/') else URL + '/'
            full_url += filename
            
            # Retrieve and save the file
            urllib.request.urlretrieve(full_url, filename)
            print(f"File saved as {filename}")

        except Exception as e:
            print(f"An error occurred: {e}")

get_url()
