from my_app import app

# app.config.from_pyfile('config.py') #Configuracion Global
# print(app.config['DEBUG'])
app.config.from_object('configuration.DevelopmentConfig') #Configuracion Modular


app.run()#debug=True
# app.config['debug']=True
# app.debug=True