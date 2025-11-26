class Application:

    def __init__(self,application_name,category,company,app_size,no_of_users,ratings):
        self.application_name=application_name
        self.category=category
        self.company=company
        self.app_size=app_size
        self.no_of_users=no_of_users
        self.ratings=ratings

    def signup(self):
        print(f"Signup done, {self.application_name}")

    def login(self):
        print(f"Welcome to {self.application_name}")

    def logout(self):
        print(f"Thank you for using {self.application_name}")

    def info(self):
        print(f"application_name: {self.application_name}\n category: {self.category}\n company: {self.company}\n app_size: {self.app_size}\n no_of_users: {self.no_of_users}\n ratings: {self.ratings}\n")

app1=Application("Instagram","Social media","meta",42.47,100000,4.4)

app2=Application("Facebook","Social media","meta",50.47,120000,4.5)

app3=Application("Whatsapp","Social media","meta",48.47,100000,4.7)

app1.signup()
app1.login()
app1.logout()
app1.info()

app2.signup()
app2.login()
app2.logout()
app2.info()

app3.signup()
app3.login()
app3.logout()
app3.info()