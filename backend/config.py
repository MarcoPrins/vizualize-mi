# Configurations for base , developement , testing environment
import os

class BaseConfig:
    """Base configuration"""
    TESTING = False
    SECRET_KEY = "door2door"
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DB_NAME = "simulation.db"

class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    DB_NAME = "simulation_test.db"

class ProductionConfig(BaseConfig):
    """Production configuration"""
    DB_NAME = "simulation_prod.db"
