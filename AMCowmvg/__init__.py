from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'banana'

#from AMCowmvg import routes
import AMCowmvg.routes

#try:
#    import AMCowmvg.routes
#except:
#    print("Local Execution Occured")

#try:
#    import routes
#except:
#    print("Online Execution Occured")