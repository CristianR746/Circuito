from setuptools import setup

readme = open("./README.md", "r")


setup(
     name='CircuitoProyecto',
    packages=['circuitoProyecto'],  # this must be the same as the name above
    version='1.0.0',
    description='Esta es la descripcion de mi paquete',
    author= 'Cristian Rivera, Keren pajon, Marcos David',
    url='https://github.com/CristianR746/Circuito.git',
    license='MIT',
    include_package_data=True
)
