from setuptools import setup, find_packages

__version__ = '0.1.0'


setup(
    name='smoke_backend',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-restful',
        'flask-migrate',
        'flask-jwt-extended',
        'flask-marshmallow',
        'marshmallow-sqlalchemy',
        'python-dotenv',
        'passlib'
    ],
    entry_points={
        'console_scripts': [
            'smoke_backend = smoke_backend.manage:cli'
        ]
    }
)
