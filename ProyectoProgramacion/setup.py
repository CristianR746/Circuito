from setuptools import setup

readme = open("./README.md", "r")


setup(
    name='CircuitoProyecto',
    packages=['circuitoProyecto'],  # this must be the same as the name above
    version='0.1',
    description='Esta es la descripcion de mi paquete',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='Nelson Hernandez',
    author_email='',
    # use the URL to the github repo
    url='https://github.com/CristianR746/Circuito.git',
    download_url='https://github.com/CristianR746/Circuito.git',
    keywords=['testing', 'logging', 'example'],
    classifiers=[ ],
    license='MIT',
    include_package_data=True
)



