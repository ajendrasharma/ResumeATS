from setuptools import setup

from custom_install import CustomInstallCommand

setup(
    # ... other setup configurations ...

    # Include a custom command to download the language model
    cmdclass={
        'install': CustomInstallCommand
    }
)
