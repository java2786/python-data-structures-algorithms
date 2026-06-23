class User:
    def __init__(self, n, e, p):
        self.name = n
        self.email = e
        self.pwd = p

class TweetApp:
    users = []
    def register(self, n, e, p):
        u = User(n,e,p)
        self.users.append(u)

    def login(self, e, p):
        isValid = False
        for i in range(len(self.users)):
            user = self.users[i]
            if(user.email == e and user.pwd == p):
                isValid = True
                break

        return isValid

            



app = TweetApp()
name = "ramesh"
email = "ramesh@gmail.com"
pwd = "ram@123"

app.register(name, email, pwd)
isValid = app.login(email, pwd)