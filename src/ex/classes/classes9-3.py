class User:
    def __init__ (self, first, last, email, password):
        self.first = first
        self.last = last
        self.email = email
        self.password = password

        self.fullName = first+" "+last

    def describe_user (self):
        print(f"Your user info: {self.first},{self.last},{self.email},{self.password}")

    def greet_user (self):
        print(f"Welcome! {self.fullName}")


alice = User("Alice","Perego","aliceperego@icloud.com","12345678")

alice.describe_user()
alice.greet_user()