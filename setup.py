from setuptools import setup
setup(
    name='pyopenvz',
    version='0.1',
    url='http://github.com/mviera/pyopenvz',
    license='LGPLv3',
    description='A Python remote API RESTful for OpenVZ',
    author='Manuel Viera <manuel.viera.tirado@gmail.es>, Sixto Martin <pitbulk@gmail.com>',
    classifiers=[
        'Development Status :: early stages',
        'Intended Audience :: Developers',
        'License :: EUPL',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=[
        'distribute==0.6.14',
    ],
)
