from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'audiomix',
    version = '0.0.1',
    author = 'Daniel Allen',
    author_email = 'daallen303@gmail.com',
    license = 'MIT License',
    description = 'add audio effects to wav files',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/daallen303/spotify-pedalboard-fun',
    py_modules = ['audio_mix', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        audiomix=audio_mix:main
    '''
)