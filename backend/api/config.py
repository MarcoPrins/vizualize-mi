# Configurations for base , developement , testing environment


class BaseConfig:
    """Base configuration"""
    TESTING = False
    SECRET_KEY = "door2door"


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    pass


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
