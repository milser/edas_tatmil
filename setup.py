from setuptools import setup, find_packages

setup(
    name='Edas_tatmil',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'paquete-dependencia-1',
        'paquete-dependencia-2',
        # Lista de paquetes necesarios para tu proyecto
    ],
    # Metadatos adicionales del proyecto
    author='Tatiana Cazorla y Rubén Serrano',
    description='Tu EDA mas sencillo',
    url='https://github.com/milser/edas_tatmil',
    classifiers=[
        'Programming Language :: Python :: 3',
        # Lista de clasificaciones de compatibilidad con Python, SO, etc.
    ],
)
