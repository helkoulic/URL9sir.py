#bsmlh

try:
    from urllib.parse import urlparse
    import pyshorteners
except ModuleNotFoundError:
    print("""
You need to install the modules listed in the 'requirements.txt' file to run the script. 
Use the following command:          
pip install -r requirements.txt
          """)
    exit()
import socket
import sys


#------------The help menu-------------------------------------------------------
# If the script name is the only given input
def Help(): 
    print("""
This is the help menu of URL9sir.py
                  
Usage: python3 URL9sir.py [options] <example1.com> <example2.com> <exampleN.com>
        
Options:
        -help / -h      Display this help menu
        -force / -f     Get the shortener link if the website is down (or the tool failed to check if its up)
                  
""")


# If no aditional arguments are given
if len(sys.argv) == 1: 
    Help()
    exit()

# If a help argument is given
elif sys.argv[1].lower() in ["-help", "--help", "help", "-h", "h" ]:
    Help()
    exit()

#-----------------------------------------------------------------------------------




#--------------The script Banner----------------------------------------------------
print("""
██╗   ██╗██████╗ ██╗     █████╗ ███████╗██╗██████╗    ██████╗ ██╗   ██╗
██║   ██║██╔══██╗██║    ██╔══██╗██╔════╝██║██╔══██╗   ██╔══██╗╚██╗ ██╔╝
██║   ██║██████╔╝██║    ╚██████║███████╗██║██████╔╝   ██████╔╝ ╚████╔╝ 
██║   ██║██╔══██╗██║     ╚═══██║╚════██║██║██╔══██╗   ██╔═══╝   ╚██╔╝  
╚██████╔╝██║  ██║███████╗█████╔╝███████║██║██║  ██║██╗██║        ██║   
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚════╝ ╚══════╝╚═╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   """)
#------------------------------------------------------------------------------------


# Display an input to choose which URL shortener service to use, or use all of them
Service = input("Pick a service :> clckru[1] isgd[2] dagd[3] ALL[0]: ")

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

        #Pass more than one URL at once
        def pass_parse_check_exe(A):
            
            # Get input (the website link) from STDIN and pass it as an argument to the function
            URL = sys.argv[A]
            

            parse_URL(URL)

            try:
                socket_connect_client(URL)
            except socket.gaierror:
                print(f"{URL} is down :c")        
                return
            URL_shorteners(URL)
            
        
        # Force output the link even if the host is down
        for ARG in range(1,1000):
            try:
                    if sys.argv[ARG].lower() in ["--force", "-force", "-f"]:
                                    
                        # Get input(the URL link) from STDIN and pass it as an argument to the function
                        for ARG in range(2,1000):       
                                URL = sys.argv[ARG]
                                
                                parse_URL(URL)

                                try:
                                    socket_connect_client(URL)
                                    URL_shorteners(URL)
        
                                except socket.gaierror:
                                    print(f"{URL} is down :c") 
                                    URL_shorteners(URL)
                                                          
                    else:
                        pass_parse_check_exe(ARG)                       
                        print(".... ... .. .")
                    
            except:
                break



# SAVE INPUT
# NO no N n 
if IsSaveOutput.lower() in ["no", "n", ""]:   
    main()

# yes y Y ye YA YES YS MHM
elif IsSaveOutput.lower() in ["yes", "ye", "y"]:
    FileName = input("File name: ")
    
    print("Wait..")
    # Save the output in a file
    with open(FileName+".txt" or "URL9sir.txt", 'a') as FILE:
        sys.stdout = FILE
        main()



