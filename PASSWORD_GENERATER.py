import itertools




'''
# gethering the details 
details_str = []
details_int = []
no_of_details_str = int(input("How many string items/details you are having about the target Account(mobile / name / fathername / Mother name / birthdate / any other details) : "))
no_of_details_int = int(input("How many integer items/details you are having to provide (mobile-n0/Fav-No/Birth-date/Birth-year) :"))

# Getinig and storing User details in a list
print("\n\n\n\n\n********************STRING VALUES INSERTION*************************************")
for i in range(no_of_details_str):
    details_ =str(input(f"Enter the details No {i}  :"))
    details_str.append(details_.strip())
    
print("\n\n\n\n\n********************INTEGER VALUES INSERTION*************************************")
for i in range(no_of_details_int):
    details_ = str(input(f"Enter the {i} detail :"))
    details_int.append(details_.strip())
    
    
#Printing the User details on screen 
print("\n\n\n\n\n********************YOU ENTERED **************************************************")
print(f"STRING DETAILS :-->> {details_str}\nINTEGER DETAILS :-->>{details_int}")
print("\n\n\n\n\n\n\n\n\n\n_________________________________________________________________________________________________________________________________________________")
'''
                                                                  ################################
                                                                  #                              #
                                                                  #   PyQt Interface For         #
                                                                  #   PASSWORD_GENERATOR         #
                                                                  ################################



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
        self.setWindowTitle("[Reaction@localhost]$ Password Generator")
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
        
        
        details_label = QLabel(f"____________________________________________________________________________________________________________________________________\n               $ System Scanning....                                 |                $ Tool Info $\n                                                                     |            \n[Reaction@localhost]$ Fetched Data :                                 |\n                                                                     |        -> UserName Password Cracker\n                   >> Devide IP :{host_ip}                       |        -> Password Generator\n                   >> Device Name :{host_name}                            |        -> Process\n_____________________________________________________________________|______________________________________________________________")
        details_label.setFont(QFont("courier",8,QFont.Bold))
        details_label.setStyleSheet("color : white;")
        details_label.setAlignment(Qt.AlignLeft)
        layout.addWidget(details_label)

        # LABEL TO PRINT "FILE OF PASSWORDS SUCCESSFULLY CREATED" :-
        self.sucess_msg_label = QLabel(f"{constant_text} PassWord File created Successfully")
        self.sucess_msg_label.setFont(QFont("italic",10))
        self.sucess_msg_label.setStyleSheet("color : yellow; background-color : black")
        self.sucess_msg_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.sucess_msg_label)
        self.sucess_msg_label.setVisible(False)

        # Target URL label and input
        self.str_no_of_details_label = QLabel(f'''{constant_text} STRING Inputs Inside [] In " " Seperated By Commas (,):\n                                  For Ex: ["reaction","Example"] ''')
        self.str_no_of_details_label.setFont(QFont("Underline", 10))
        self.str_no_of_details_label.setStyleSheet("color: green;")
        self.str_no_of_details_label.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.str_no_of_details_label)
        self.str_no_of_details_label.setVisible(False)

        self.str_no_of_details_input = QLineEdit()
        self.str_no_of_details_input.setFont(QFont("Courier", 10))
        self.str_no_of_details_input.setStyleSheet("color: yellow; background-color: black;")
        layout.addWidget(self.str_no_of_details_input)
        self.str_no_of_details_input.setVisible(False)

        # Target username label and input
        self.int_no_of_details_label = QLabel(f'''{constant_text} INTEGER Inputs Inside [] In " " Seperated By Commas (,):\n                                  For Ex: ["09","28","2007","9974115457"] ''')
        self.int_no_of_details_label.setFont(QFont("Underline", 10))
        self.int_no_of_details_label.setStyleSheet("color: green;")
        self.int_no_of_details_label.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.int_no_of_details_label)
        self.int_no_of_details_label.setVisible(False)

        self.int_no_of_details_input = QLineEdit()
        self.int_no_of_details_input.setFont(QFont("Courier", 10))
        self.int_no_of_details_input.setStyleSheet("color: yellow; background-color: black;")
        layout.addWidget(self.int_no_of_details_input)
        self.int_no_of_details_input.setVisible(False)

        # Submit button to store the inputs
        self.submit_button = QPushButton("ENTER")
        self.submit_button.setFont(QFont("Courier", 10))
        self.submit_button.setStyleSheet("color: white; background-color: red;")
        self.submit_button.clicked.connect(lambda:(self.store_inputs(),self.display_sucess_msg_label(),self.hide_user_input()))
        layout.addWidget(self.submit_button)
        self.submit_button.setVisible(False)
        
        
        
        # LABEL FOR DISPLAYING THE INSTRUCTION TO ENTER THE PASSWORD HINTS / USER INPUTS 
        self.instruction_label = QLabel("",self)
        self.instruction_label.setFont(QFont("Courier",8,QFont.Bold))
        self.instruction_label.setAlignment(Qt.AlignLeft)
        self.instruction_label.setStyleSheet("color : blue; background-color :black")
        layout.addWidget(self.instruction_label)
        self.instruction_label.setVisible(False)
        
        self.read_instruction_button = QPushButton("READ INSTRUCTION")
        self.read_instruction_button.setFont(QFont("Courier",8))
        self.read_instruction_button.setStyleSheet("color : white; background-color : red;")
        self.read_instruction_button.clicked.connect(lambda:(self.instruction_label_Text()))
        layout.addWidget(self.read_instruction_button)
        
        
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
        
        

         
             
        
        self.setLayout(layout)
        
        
    def hide_user_input(self):
        self.str_no_of_details_label.setVisible(False)
        self.str_no_of_details_input.setVisible(False)
        self.int_no_of_details_label.setVisible(False)
        self.int_no_of_details_input.setVisible(False)
        self.submit_button.setVisible(False)
        
    def display_sucess_msg_label(self):
        
        self.sucess_msg_label.setVisible(True)
        
    #function To Give Text to instruction Label
    def instruction_label_Text(self):
        self.instruction_label.setText('''____________________________________________________________________________________________________________________________________________________\n\n                                            ENTER TARGET USERNAME RELATED DATA AS FOLLOWS\n____________________________________________________________________________________________________________________________________________________\n\n>> String Details >> Inside The [] Covered In DoubleInverted-Commas (" ") And Sepereted By Commad (,)\n\n                  For Ex:-  TARGET USERNAME -->> john wick mosco\n                            Details         -->> ["john","wick","mosco"]\n                            (Enter Target's Details like Name , Surname , NickName , FatherName etc....)\n\n>> Integer Details >> Inside The [] And Sepereted By Commas (,)\n\n                   For Ex:-  Birth-Date, Contact-No , Birth-year, Birth-Month, Common Number/Digit used in Every Acc. etc....\n                             Details    -->> [09,9974455621,2005,07,31]\n\n____________________________________________________________________________________________________________________________________________________''')
        self.instruction_label.setVisible(True)
        self.read_instruction_button.setText("START PROCESS")
        self.read_instruction_button.clicked.connect(lambda:(self.display_input_fields()))
        
    def display_input_fields(self):
        self.instruction_label.setVisible(False)
        self.read_instruction_button.setVisible(False)
        
        self.str_no_of_details_input.setVisible(True)
        self.str_no_of_details_label.setVisible(True)
        self.int_no_of_details_input.setVisible(True)
        self.int_no_of_details_label.setVisible(True)
        self.submit_button.setVisible(True)
        
        
        
        
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
                                
    def store_inputs(self):
                         # Get user input from the fields
                        details_str = self.str_no_of_details_input.text() # no of str inputs
                        details_int = self.int_no_of_details_input.text()        # no of int inputs
                        main_details.append(details_str)
                        main_details.append(details_int)
        
                        
        
                        # Print them (or use them in further logic)
                        print(f"STR DETAILS NUMBER : {str_details}")
                        print(f"INT DETAILS NUMBER : {int_details}")





















#_____________________________________________________________GENERATING POSSIBLE PASSWORDS________________________________________________________________________________________________#



#*********************************************************************************************************************************************************************************************************
# 1) RESULTS BY MERGING STRING DETAILS
str_merge = []





for item in details_str:                                # WITHOUT @
            for  j in range(0,len(details_str)):
               str_merge.append(item + details_str[j])
                                           

print("STRING MERGING ==>>",str_merge)
print("\n\n\n\n\n\n\n\n\n\n_________________________________________________________________________________________________________________________________________________")
            
            
            

#*********************************************************************************************************************************************************************************************************
                
# 2) RESULTS BY MULTIPLICATION OF INTEGER AND STRING LISTS

multiplication = []
multiplication_reversed =[]

     
for item in details_str:                    #  STR * INT
    for j in range(0,len(details_int)):
        multiplication.append(item + details_int[j])
    
print("MULTIPLICATION ==>>>>",multiplication)
print("\n\n\n\n\n\n\n\n\n\n_________________________________________________________________________________________________________________________________________________")

for item in details_int:                     # INT *  STR
    for j in range(0,len(details_str)):
        multiplication_reversed.append(item + details_str[j])
        
print("REVERSED MULTIPLICATION ==>>",multiplication_reversed)         
print("\n\n\n\n\n\n\n\n\n\n_________________________________________________________________________________________________________________________________________________")





#*********************************************************************************************************************************************************************************************************
# 3) STR MERGED * INTEGER

str_merge_int = []
str_merge_int_reversed = []




for item in str_merge:                                       # STR_MERGE * INT
    for j in range(0,len(details_int)):
        str_merge_int.append(item + details_int[j])
        
print("merged str * int ----------->>>>",str_merge_int)
print("\n\n\n\n\n\n\n\n\n\n_________________________________________________________________________________________________________________________________________________")


for item in details_int:                                    # INT * STR_MERGE
    for j in range(0,len(str_merge)):
        str_merge_int_reversed.append(item + str_merge[j])
        
        
print("REVERSED STR_MERGE * INT -------------->>>>>>>>>>>>> ",str_merge_int_reversed)
print("\n\n\n\n\n\n\n\n\n\n_________________________________________________________________________________________________________________________________________________")




#*********************************************************************************************************************************************************************************************************
 # 4) @ ,#,$,%,!,@,#
                                                            
                                                            
                                                      
                                                            
                                                             
                                                                                   ########################
                                                                                   #   (i)   WITH @       #
                                                                                   #                      #
                                                                                   ########################
            
str_merge_AT = []




for item in details_str:                                # WITH @
            for  j in range(0,len(details_str)):
               str_merge_AT.append(item + "@" + details_str[j])
                                           

print("STRING MERGING ==>>",str_merge_AT)                                                                          
                                                                                          
                                                                                          

# str_merge  * int with @     ||  int * str_merge with @

str_merge_AT_int_AT =[]
int_AT_str_merge_AT = []


for item in str_merge_AT:
    for j in range(0,len(details_int)):
        str_merge_AT_int_AT.append(item + "@" + details_int[j])
        
print("STR_MERGE + @ + INT--------------->>>>>>>>",str_merge_AT_int_AT)
print("\n\n\n\n\n")

for item in details_int:
    for j in range(0,len(str_merge_AT)):
        int_AT_str_merge_AT.append(item + "@" + str_merge_AT[j])
        
print("INT + @ + STR_MERGED_AT",int_AT_str_merge_AT)



str_merge_AT = []
for item in details_str:
    
    for j in range(0,len(details_str)):              # WITH @
        str_merge_AT.append(item + "@" + details_str[j])
                
print("@----------->>>>",str_merge_AT)            
print("\n\n\n\n\n\n\n\n\n\n_________________________________________________________________________________________________________________________________________________")



# @

str_merge_int_AT = []
str_merge_int_reversed_AT = []


for item in str_merge:                                     # STR_MERGE * INT WITH @
    for j in range(0,len(details_int)):
        str_merge_int_AT.append(item + "@" + details_int[j])
    
print( "STR_MERGED * INT  with @ -->>",str_merge_int_AT)
print("\n\n\n\n\n\n\n\n\n\n_________________________________________________________________________________________________________________________________________________")



for item in details_int:                             # INT * STR_MERGE WITH @
    for j in range(0,len(str_merge)):
        str_merge_int_reversed_AT.append(item + "@" + str_merge[j])
        
        
print("INT * STR_MERGE WITH @ --->>",str_merge_int_reversed_AT)
print("\n\n\n\n\n\n\n\n\n\n_________________________________________________________________________________________________________________________________________________")


# @

multiplication_AT = []
multiplication_reversed_AT=[]

for item in details_str:                        #   STR * INT WITH @
    for j in range(0,len(details_int)):
        multiplication_AT.append(item + "@" +details_int[j])

print(" STR * INT WITH @------->>>",multiplication_AT)

print("\n\n\n\n\n\n\n\n\n\n_________________________________________________________________________________________________________________________________________________")


for item in details_int:                      # INT * STR WITH @
    for j in range(0,len(details_str)):
        multiplication_reversed_AT.append(item + "@" + details_str[j])
        
print("INT * STR WITH @ ------>>>",multiplication_reversed_AT)
print("\n\n\n\n\n\n\n\n\n\n_________________________________________________________________________________________________________________________________________________")





                                                                                   ########################
                                                                                   #   (ii)   WITH #      #
                                                                                   #                      #
                                                                                   ########################




str_merge_HASH = []



for item in details_str:                                
            for  j in range(0,len(details_str)):
               str_merge_HASH.append(item + "#" + details_str[j])
                                           

print("STRING MERGING ==>>",str_merge_HASH)                                                                          
                                                                                          
                                                                                            

# str_merge  * int with #     ||  int * str_merge with #

str_merge_AT_int_HASH =[]
int_HASH_str_merge_AT = []




for item in str_merge_AT:
    for j in range(0,len(details_int)):
        str_merge_AT_int_HASH.append(item + "#" + details_int[j])
        
print("STR_MERGE + # + INT--------------->>>>>>>>",str_merge_AT_int_HASH)
print("\n\n\n\n\n")

for item in details_int:
    for j in range(0,len(str_merge_AT)):
        int_HASH_str_merge_AT.append(item + "#" + str_merge_AT[j])
        
print("INT + # + STR_MERGED_AT",int_HASH_str_merge_AT)


print("\n\n\n\n\n\n\n\n\n\n_________________________________________________________________________________________________________________________________________________")


str_merge_HASH_int_HASH =[]
int_HASH_str_merge_HASH = []



for item in str_merge_HASH:
    for j in range(0,len(details_int)):
        str_merge_HASH_int_HASH.append(item + "#" + details_int[j])
        
print("STR_MERGE + # + INT--------------->>>>>>>>",str_merge_HASH_int_HASH)
print("\n\n\n\n\n")

for item in details_int:
    for j in range(0,len(str_merge_HASH)):
        int_HASH_str_merge_HASH.append(item + "#" + str_merge_HASH[j])
        
print("INT + # + STR_MERGED_AT",int_HASH_str_merge_HASH)
print("\n\n\n\n\n")

str_merge_HASH_int_AT =[]
int_AT_str_merge_HASH = []



for item in str_merge_HASH:
    for j in range(0,len(details_int)):
        str_merge_HASH_int_AT.append(item + "@" + details_int[j])
        
print("STR_MERGE + # + INT--------------->>>>>>>>",str_merge_HASH_int_AT)
print("\n\n\n\n\n")

for item in details_int:
    for j in range(0,len(str_merge_HASH)):
        int_AT_str_merge_HASH.append(item + "@" + str_merge_HASH[j])
        
print("INT + # + STR_MERGED_AT",int_AT_str_merge_HASH)
print("\n\n\n\n\n")














# @

str_merge_int_HASH = []
str_merge_int_reversed_HASH = []


for item in str_merge:                                     # STR_MERGE * INT WITH #
    for j in range(0,len(details_int)):
        str_merge_int_HASH.append(item + "#" + details_int[j])
    
print( "STR_MERGED * INT  with # -->>",str_merge_int_HASH)
print("\n\n\n\n\n\n\n\n\n\n_________________________________________________________________________________________________________________________________________________")



for item in details_int:                             # INT * STR_MERGE WITH #
    for j in range(0,len(str_merge)):
        str_merge_int_reversed_HASH.append(item + "#" + str_merge[j])
        
        
print("INT * STR_MERGE WITH # --->>",str_merge_int_reversed_HASH)
print("\n\n\n\n\n\n\n\n\n\n_________________________________________________________________________________________________________________________________________________")


# @

multiplication_HASH = []
multiplication_reversed_HASH=[]

for item in details_str:                        #   STR * INT WITH #
    for j in range(0,len(details_int)):
        multiplication_HASH.append(item + "#" +details_int[j])

print(" STR * INT WITH #------->>>",multiplication_HASH)

print("\n\n\n\n\n\n\n\n\n\n_________________________________________________________________________________________________________________________________________________")


for item in details_int:                      # INT * STR WITH #
    for j in range(0,len(details_str)):
        multiplication_reversed_HASH.append(item + "#" + details_str[j])
        
print("INT * STR WITH # ------>>>",multiplication_reversed_HASH)
print("\n\n\n\n\n\n\n\n\n\n_________________________________________________________________________________________________________________________________________________")



                                                                                   #############################
                                                                                   #   (iiI)  WITH DOT(.)      #
                                                                                   #                           #
                                                                                   #############################


str_merge_DOT = []
for item in details_str:
    
    for j in range(0,len(details_str)):              # WITH .
        str_merge_DOT.append(item + "." + details_str[j])
                
print("DOT STR MERGE ----------->>>>",str_merge_DOT)            
print("\n\n\n\n\n\n\n\n\n\n_________________________________________________________________________________________________________________________________________________")

# str_merged_ with DOT(.) + details_int

str_merge_DOT_DOT_int = []
int_DOT_str_merge_DOT = []

for item in str_merge_DOT:
    for j in range(0,len(details_int)):
        str_merge_DOT_DOT_int.append(item + "." + details_int[j])


for item in details_int:
    for j in range(0,len(str_merge_DOT)):
        int_DOT_str_merge_DOT.append(item + "." + str_merge_DOT[j])
        


# str_merge  * int with #     ||  int * str_merge with #

str_merge_AT_int_DOT =[]
int_DOT_str_merge_AT = []




for item in str_merge_AT:
    for j in range(0,len(details_int)):
        str_merge_AT_int_DOT.append(item + "." + details_int[j])
        
print("STR_MERGE + DOT(.)+ INT--------------->>>>>>>>",str_merge_AT_int_DOT)
print("\n\n\n\n\n")

for item in details_int:
    for j in range(0,len(str_merge_AT)):
        int_DOT_str_merge_AT.append(item + "." + str_merge_AT[j])
        
print("INT + DOT(.) + STR_MERGED_AT",int_DOT_str_merge_AT)


print("\n\n\n\n\n\n\n\n\n\n_________________________________________________________________________________________________________________________________________________")



str_merge_HASH_int_DOT =[]
int_DOT_str_merge_HASH = []



for item in str_merge_HASH:
    for j in range(0,len(details_int)):
        str_merge_HASH_int_DOT.append(item + "." + details_int[j])
        
print("STR_MERGE + # + INT--------------->>>>>>>>",str_merge_HASH_int_DOT)
print("\n\n\n\n\n")

for item in details_int:
    for j in range(0,len(str_merge_HASH)):
        int_DOT_str_merge_HASH.append(item + "." + str_merge_HASH[j])
        
print("INT + # + STR_MERGED_AT",int_DOT_str_merge_HASH)
print("\n\n\n\n\n")


str_merge_DOT_int_DOT =[]
int_DOT_str_merge_DOT = []



for item in str_merge_DOT:
    for j in range(0,len(details_int)):
        str_merge_DOT_int_DOT.append(item + "." + details_int[j])
        
print("STR_MERGE + # + INT--------------->>>>>>>>",str_merge_DOT_int_DOT)
print("\n\n\n\n\n")

for item in details_int:
    for j in range(0,len(str_merge_DOT)):
        int_DOT_str_merge_DOT.append(item + "." + str_merge_DOT[j])
        
print("INT + # + STR_MERGED_AT",int_DOT_str_merge_DOT)
print("\n\n\n\n\n")




str_merge_DOT_int =[]
int_DOT_str_merge =[]

for item in str_merge:
    for j in range(0,len(details_int)):
        str_merge_DOT_int.append(item + "." + details_int[j])

print("merged str + DOT(.) + INT --------->>>",str_merge_DOT_int)
print("----------------------------------------------------------------------------------------------------------------------------------------\n\n\n\n\n\n\n\n")



for item in details_int:
    for j in range(0,len(str_merge)):
        int_DOT_str_merge.append(item  + "." + str_merge[j])
        
print("\n\n\n\\n\n\n\n INT + DOT(.) + STR_MERGE--->>",int_DOT_str_merge)




str_merge_DOT_int_AT = []
int_AT_str_merge_DOT = []

for item in str_merge_DOT:
    for j in range(0,len(details_int)):
        str_merge_DOT_int_AT.append(item + "@"+details_int[j])
        
        
for item in details_int:
    for j in range(0,len(str_merge_DOT)):
        int_AT_str_merge_DOT.append(item + "@"+ str_merge_DOT[j])
        
print("\n\n\n\n\n*************************************\n\n\n\n\n")
print(f"{str_merge_DOT_int_AT}\n{int_AT_str_merge_DOT}")




str_merge_DOT_int_HASH = []
int_HASH_str_merge_DOT= []

for item in str_merge_DOT:
    for j in range(0,len(details_int)):
        str_merge_DOT_int_HASH.append(item + "#"+details_int[j])
        
        
for item in details_int:
    for j in range(0,len(str_merge_DOT)):
        int_HASH_str_merge_DOT.append(item + "#"+ str_merge_DOT[j])
        
print("\n\n\n\n\n*************************************\n\n\n\n\n")
print(f"{str_merge_DOT_int_AT}\n{int_AT_str_merge_DOT}")



                                                                                   ##############################
                                                                                   #   (iv)  WITH COMMON - 123  #
                                                                                   #                            #
                                                                                   ##############################

# 1)----->> AT (@) + 123 ==>> @123
 
str_merge_AT_123 = []
str_merge_AT_AT_123 = []
str_merge_HASH_AT_123 = [] 
str_merge_DOT_AT_123 = []

for item in str_merge:
        str_merge_AT_123.append(item + "@123" )
        
for item in str_merge_AT:
    str_merge_AT_AT_123.append(item + "@123")
    

for item in str_merge_HASH:
    str_merge_HASH_AT_123.append(item + "@123")


for item in str_merge_DOT:
    str_merge_DOT_AT_123.append(item + "@123")
    
print(f"{str_merge_AT_123}\n {str_merge_AT_AT_123}\n {str_merge_HASH_AT_123}\n {str_merge_DOT_AT_123}")


# 2)----->> HASH (#) + 123 ==>> #123

str_merge_HASH_123 = []
str_merge_AT_HASH_123 = []
str_merge_HASH_HASH_123 = [] 
str_merge_DOT_HASH_123 = []

for item in str_merge:
        str_merge_HASH_123.append(item + "#123" )
        
for item in str_merge_AT:
    str_merge_AT_HASH_123.append(item + "#123")
    

for item in str_merge_HASH:
    str_merge_HASH_HASH_123.append(item + "#123")


for item in str_merge_DOT:
    str_merge_DOT_HASH_123.append(item + "#123")
    
print(f"{str_merge_HASH_123}\n {str_merge_AT_HASH_123}\n {str_merge_HASH_HASH_123}\n {str_merge_DOT_HASH_123}")



# 3)----->> DOT (.) + 123 ==>> .123

str_merge_DOT_123 = []
str_merge_AT_DOT_123 = []
str_merge_HASH_DOT_123 = [] 
str_merge_DOT_DOT_123 = []

for item in str_merge:
        str_merge_DOT_123.append(item + ".123" )
        
for item in str_merge_AT:
    str_merge_AT_DOT_123.append(item + ".123")
    

for item in str_merge_HASH:
    str_merge_HASH_DOT_123.append(item + ".123")


for item in str_merge_DOT:
    str_merge_DOT_DOT_123.append(item + ".123")

print("\n\n\n\n\n\n\n\n\n\n\n")    
print(f"{str_merge_DOT_123}\n {str_merge_AT_DOT_123}\n {str_merge_HASH_DOT_123}\n {str_merge_DOT_DOT_123}")


# BEFORE 123 THEN ITEM ===>>>> 123 + item

# 4)------->>  123 + AT (@) ===>>>   123@ + ITEM

_123_AT_str_merge = []
_123_AT_str_merge_AT = []
_123_AT_str_merge_HASH = []
_123_AT_str_merge_DOT = []

for item in str_merge:
    _123_AT_str_merge.append("123@" + item)
    
for item in str_merge_AT:
    _123_AT_str_merge_AT.append("123@" + item)
    
for item in str_merge_HASH:
    _123_AT_str_merge_HASH.append("123@" + item)
    
for item in str_merge_DOT:
    _123_AT_str_merge_DOT.append("123@" + item)
    
print("\n\n\n\n\n")
print(f"{_123_AT_str_merge}\n {_123_AT_str_merge_AT}\n {_123_AT_str_merge_HASH}\n {_123_AT_str_merge_DOT}")



for i in details_int:
    if len(i) == 10   or len(i) == 9 or len(i) == 11:
        print(f"mobile no : {i}")
        

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                    ** STORING EVERY PASSWORD_LISTS IN A SINGLE LIST   & CREATING PASSWORD FILE**
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Combine using itertools.chain and combining the LISTS
possible_passwords_list = list(itertools.chain( _123_AT_str_merge,  _123_AT_str_merge_AT, _123_AT_str_merge_HASH,  _123_AT_str_merge_DOT      ,int_DOT_str_merge_DOT      ,str_merge_DOT_DOT_int             ,str_merge_DOT_123, str_merge_AT_DOT_123,  str_merge_HASH_DOT_123, str_merge_DOT_DOT_123    ,str_merge_HASH_123, str_merge_AT_HASH_123, str_merge_HASH_HASH_123, str_merge_DOT_HASH_123      ,str_merge_AT_123, str_merge_AT_AT_123, str_merge_HASH_AT_123,   str_merge_DOT_AT_123    ,str_merge_DOT_int_HASH,  int_HASH_str_merge_DOT     ,  int_AT_str_merge_DOT      ,  str_merge_DOT_int_AT  ,str_merge_DOT_int,   int_DOT_str_merge, str_merge_DOT_int_DOT, int_DOT_str_merge_DOT   ,str_merge_HASH_int_DOT ,int_DOT_str_merge_HASH    , str_merge_AT_int_DOT     ,int_DOT_str_merge_AT   , details_str,  details_int, str_merge, str_merge_DOT,   multiplication, multiplication_reversed, str_merge_int ,str_merge_int_reversed,  str_merge_AT, str_merge_AT_int_AT, int_AT_str_merge_AT, str_merge_AT,  str_merge_int_AT, str_merge_int_reversed_AT,   multiplication_AT, multiplication_reversed_AT,   str_merge_HASH,  str_merge_AT_int_HASH , int_HASH_str_merge_AT,    str_merge_HASH_int_HASH,   int_HASH_str_merge_HASH,   str_merge_HASH_int_AT,   int_AT_str_merge_HASH,    str_merge_int_HASH,  str_merge_int_reversed_HASH    , multiplication_HASH,  multiplication_reversed_HASH  ))

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

print("ALL POSSIBLE PASSWORDS OBTAINED ACCORDING TO THE DATA GIVEN BY YOU ARE AS FOLLOWS :")
print("-->>",possible_passwords_list)



# Create and open a file in write mode ('w')


with open("MAIN PASSWORDS LISTS OR DICTIONERY.txt", "w") as file:
                 # Write each item from the list to the file
                 for detail in possible_passwords_list:
                        file.write(detail + "\n")  # Add a newline after each detail
                        
                        

print("Details successfully written to user_details.txt")

app = QApplication(sys.argv)
window = HackingToolGUI()
window.show()
sys.exit(app.exec_())





