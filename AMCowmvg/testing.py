#from AMCowmvg import app
from AMCowmvg.__init__ import app

#try:
#    from __init__ import app
#except:
#    print("")

#try:
#    from AMCowmvg.__init__ import app
#except:
#    print("")    
#testing testing


def runApp():
    #if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')

runApp()