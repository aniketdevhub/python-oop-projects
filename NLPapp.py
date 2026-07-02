import os
from dotenv import load_dotenv
import nlpcloud

load_dotenv()

API_KEY = os.getenv("NLP_API_KEY")


class NLPapp:

    def __init__(self):

        self.__database = {
            "aniket@gmail.come": ["Aniket", 1234],
            "navnit@gmai.com": ["Navnit", 3435],
            "ashish@gmail.com": ["Ashish", 9876],
        }
        self.first_menu()

    def first_menu(self):
        print("Welcome to the App .............")
        print("""
                        1. Register :
                        2. Login :
                        3. Exit : """)
        user_input = input("Enter your choice : ")

        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            print("Thanks for using this software ..")
            exit()

    def second_menu(self):
        print("""
                1. NER
                2. Comment Sentiment 
                3. log out """)
        sec_input = input("Enter the choice : ")

        if sec_input == "1":
            self.NER()
        elif sec_input == "2":
            self.comment_sentiment()
        else:
            print("Thanks for using this software ....")
            exit()

    def register(self):
        name = input("Enter your name : ")
        email = input("Enter your email : ")
        password = input("Enter your password : ")

        if email in self.__database:
            print("This email is already in use..")
        else:
            self.__database[email] = [name, password]
            self.first_menu()

    def login(self):
        email = input("Enter your email : ")
        password = int(input("Enter your password : "))
        if email in self.__database:
            if self.__database[email][1] == password:
                self.second_menu()
            else:
                print("Wrong Password ...")
                self.first_menu()
        else:
            print("This email is not registor ....")
            self.first_menu()

    def NER(self):
        para = input("Enter your paragraph : ")
        search = input("Enter what you want to search in above paragraph : ")
        try:
            client = nlpcloud.Client("gpt-oss-120b", API_KEY, gpu=True)
            response = client.entities(para, searched_entity=search)
            print(response)

        except Exception as e:
            print("=" * 40)
            print("Failed to connect to the NLP Cloud API.")
            print(f"Error: {e}")
            print("=" * 40)

    def comment_sentiment(self):
        para = input("Enter the paragraph : ")
        try:
            client = nlpcloud.Client("gpt-oss-120b", API_KEY, gpu=True)
            response = client.sentiment(para, target="NLP Cloud")
            print(response)

        except Exception as e:
            print("=" * 40)
            print("Failed to connect to the NLP Cloud API.")
            print(f"Error: {e}")
            print("=" * 40)


obj = NLPapp()
