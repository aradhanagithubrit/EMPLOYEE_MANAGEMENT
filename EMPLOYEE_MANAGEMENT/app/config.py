import os
base_dir=os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KET = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'employee.dib')
    SQLALCHEMY_TRACK_MODIFICATIONS = False