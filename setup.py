from setuptools import find_packages,setup


def get_requirements() -> list[str]:
    requirements_list=list[str]=[]

    return requirements_list

setup(
    name='Sensor',
    version='0.0.1',
    author="Akhil",
    author_email='markapuramakhil@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)