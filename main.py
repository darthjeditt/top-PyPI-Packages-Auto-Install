# Installs the top 50 python packages from PyPI api and their dependencies
import requests
import os
import subprocess
from bs4 import BeautifulSoup as bs

def install_python_packages(limit=10):
    '''Fetches the top PyPI packages from URL and installs them'''

    res = requests.get('https://hugovk.github.io/top-pypi-packages/')
    soup = bs(res.content, 'html.parser')

    package_content = soup.select('ol li a')
    packages = [pkg.text for pkg in package_content][:limit]

    return packages

def setup_env_and_install_python_packages(packages):
    '''Setup virtual environment and install packages'''

    venv = 'topPackagesEnv'
    subprocess.run(['python', '-m', 'venv', venv]) 

    pip_path = os.path.join(venv, 'bin', 'pip')
    subprocess.run([pip_path, 'install'] + packages)


if __name__ == "__main__":
    top_packages = install_python_packages(10)
    print('The top 10 PyPI packages are:')
    print(top_packages)

    setup_env_and_install_python_packages()
    print(f"\nPackages installed in the virtual environment: {os.path.abspath('top_packages_venv')}")
