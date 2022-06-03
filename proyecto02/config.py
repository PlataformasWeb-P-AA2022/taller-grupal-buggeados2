"""
"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# sqlite
#enlace = 'sqlite:///' + os.path.join(basedir, 'databaseV.db')

# mysql
enlace = "mysql+mysqlconnector://mateo:12345@localhost:3306/taller02"
