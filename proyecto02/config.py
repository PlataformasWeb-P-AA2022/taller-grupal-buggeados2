"""
"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# sqlite
enlace = 'sqlite:///' + os.path.join(basedir, 'databaseV.db')

# mysql
#enlace = "mysql+mysqlconnector://salai:12341234@localhost:3306/base_flask_001"
