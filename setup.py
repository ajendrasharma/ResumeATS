from setuptools import setup

setup(
    # ... other setup configurations ...

    # Include a custom command to download the language model
    cmdclass={
        'install': CustomInstallCommand
    }
)
