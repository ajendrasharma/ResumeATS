from setuptools.command.install import install
from subprocess import check_call

class CustomInstallCommand(install):
    def run(self):
        # Run the language model download command
        check_call(['python', '-m', 'spacy', 'download', 'en_core_web_sm'])

        # Continue with the regular installation
        install.run(self)
