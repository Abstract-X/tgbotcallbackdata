import setuptools


def get_long_description() -> str:

    with open("README.md", encoding="UTF-8") as stream:
        return stream.read()


setuptools.setup(
    name="tgbotcallbackdata",
    version="1.0.1",
    packages=setuptools.find_packages(exclude=("tests", "docs")),
    url="https://github.com/Abstract-X/tgbotcallbackdata",
    license="MIT",
    author="Abstract-X",
    author_email="abstract-x-mail@protonmail.com",
    description="Creating callback data for the InlineKeyboardButton in Telegram bots.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    install_requires=[
        "xcept>=2.0.0",
    ],
    python_requires='>=3.7',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11"
    ]
)
