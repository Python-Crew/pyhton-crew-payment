import setuptools

CLASSIFIERS = [
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
    "Topic :: Software Development :: Libraries :: Python Modules",
]



with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="python-crew-payment",
    version="0.0.1",
    author="Python Crew",
    author_email="s.tohidi22@gmail.com",
    description="A Django Packeges for Payment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Python-Crew/pyhton-crew-payment",
    project_urls={
        "Bug Tracker": "https://github.com/Python-Crew/pyhton-crew-payment",
    },
    classifiers=CLASSIFIERS,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        "Django>=2.2,<4",
        "prices>=1.0.0",
        "django-prices>=2.2.0",
        "stripe>=2.63.0",
        "requests>=2.26.0",
        "enmerkar>=0.7.1",
    ],
    platforms=["any"],
    zip_safe=False,
    include_package_data=True,

)
