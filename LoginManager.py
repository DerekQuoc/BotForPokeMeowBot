import pickle

class LoginManager():
    def getLogin(self):
        try:
            file = open("login_info","rb")
            info = pickle.load(file)
            file.close

            return info
        
        except:
            return False

    def storeLoginInfo(self, info):
        try:
            file = open("login_info","wb")
            pickle.dump(info,file)
            file.close
            print("Saved login info to login_info")
        except:
            print("Error saving login info!")
