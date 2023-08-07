""" This is the base class for configuring Django applications. 
It allows you to specify various settings and configurations for your app."""
from django.apps import AppConfig

"""This attribute specifies the default auto field to be used for model primary keys. In this case, 
'django.db.models.BigAutoField' is set as the default auto field. 
This means that any models you define in the base app will use BigAutoField as the default primary key field."""
class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base' # This attribute specifies the name of the app. In this case, the app is named 'base'.
