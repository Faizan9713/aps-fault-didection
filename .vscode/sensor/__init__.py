from setuptools import find_namespace_packages,setup

def get_requirements():
    pass



set(
  name="sensor",
  version="0.0.1",
  author="ineuron",
  author_email="mohammadfaizan9713",
  packages= find_packages(),
  install_requires=get_requirements(), 

)