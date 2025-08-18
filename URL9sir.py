#bsmlh
try:
    from urllib.parse import urlparse
    import pyshorteners
except ModuleNotFoundError:
    print("""
You need to install the modules listed in the 'requirements.txt' file in order to be able to run the script. 
Use the following command:          
pip install -r requirements.txt
          """)
    exit()
import argparse
import socket
import sys 



# The help menu
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="A URL shortener"
    )
    parser.add_argument('URL', type=str, nargs='*')
    parser.add_argument('-f', '--force', action='store_true', help='Get the shortener link even if the website is down (or the tool failed to check if its availability)')

    args = parser.parse_args()
# Usage: python3 URL9sir.py [options] <example1.com> <example2.com> <exampleN.com>


# If no aditional arguments are given show the help menu and exit
if len(sys.argv) == 1: 
    parser.print_help()
    exit()


# The script Banner
print("""
██╗   ██╗██████╗ ██╗     █████╗ ███████╗██╗██████╗    ██████╗ ██╗   ██╗
██║   ██║██╔══██╗██║    ██╔══██╗██╔════╝██║██╔══██╗   ██╔══██╗╚██╗ ██╔╝
██║   ██║██████╔╝██║    ╚██████║███████╗██║██████╔╝   ██████╔╝ ╚████╔╝ 
██║   ██║██╔══██╗██║     ╚═══██║╚════██║██║██╔══██╗   ██╔═══╝   ╚██╔╝  
╚██████╔╝██║  ██║███████╗█████╔╝███████║██║██║  ██║██╗██║        ██║   
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚════╝ ╚══════╝╚═╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   """)


# Display an input to choose which URL shortener service to use, or use all of them
Service = input("Pick a service :> clckru[1] isgd[2] dagd[3] ALL[0]: ")

# Display an input to choose if the output should be saved in a file or not
IsSaveOutput = input("Do you want to save the output [Y/n]? (press ENTER to skip) ")


def URL_shorteners(URL):
    # Shorten the shortener function in S variable
    S = pyshorteners.Shortener()

    # Handle the INPUT
    if Service == "1":
        # Use tinyurl
        print(f"{URL} => {S.clckru.short(URL)}")
    elif Service == "2":
        # Use isgd
        print(f"{URL} => {S.isgd.short(URL)}")

    elif Service == "3":
        # Use dagd
        print(f"{URL} => {S.dagd.short(URL)}")

    else:
        # If the INPUT is something ELSE, use all of the URL shortener services
        print(f"{URL} => {S.clckru.short(URL)}")
        print(f"{URL} => {S.isgd.short(URL)}")
        print(f"{URL} => {S.dagd.short(URL)}")


def socket_connect_client(URL):
    # Create socket object 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set a timeout 
    client.settimeout(5) 

    # Connect to the client
    client.connect((URL, 80))

    # Send some data
    client.send(f"GET / HTTP/1.1\r\nHost: {URL}\r\n\r\n".encode("utf-8"))

    print(f"{URL} is up!")


def parse_URL(URL):
    # Parse the URL(because the shortener function doesn't accept "http" method)
    Host = urlparse(URL).netloc
    if Host == "":
        Host = urlparse(URL).path
    else:
        Host


def main():
    # To pass more than one URL at once
    for LINK in args.URL:
        def pass_parse_check_exe():
            # Get input (the website link) from STDIN and pass it as an argument to the function
                        
                parse_URL(LINK)

                try:
                    socket_connect_client(LINK)
                except socket.gaierror:
                    print(f"{LINK} is down :c")
                    print("Try --force to get the link")        
                    return
                URL_shorteners(LINK)
        if args.force == False:
            pass_parse_check_exe()



        else:
            parse_URL(LINK)
            try:
                socket_connect_client(LINK)
                URL_shorteners(LINK)
        
            except socket.gaierror:
                print(f"{LINK} is down :c") 
                URL_shorteners(LINK)

# Save the output in a txt file
if IsSaveOutput.lower() in ["no", "n", ""]:   
    main()

elif IsSaveOutput.lower() in ["yes", "ye", "y"]:
    FileName = input("File name: ")
    print("Wait..")
    
    with open(FileName+".txt" or "URL9sir.txt", 'a') as FILE:
        sys.stdout = FILE
        main()

