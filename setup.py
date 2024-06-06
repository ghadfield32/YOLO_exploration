from setuptools import setup, find_packages

setup(
    name="your_project_name",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "supervision",
        "yolo",
        "roboflow",
        "ipykernel",
        "ultralytics",
        "requests",
        "ipython",
    ],
    extras_require={
        "cuda": [
            "torch==1.13.1+cu121",  # Ensure the version matches the one you use
            "torchvision==0.14.1+cu121",
            "torchaudio==0.13.1",
        ],
    },
    dependency_links=[
        "https://download.pytorch.org/whl/cu121"
    ],
    entry_points={
        "console_scripts": [
            "your_script_name=your_module:main_function",
        ],
    },
    author="Your Name",
    author_email="your_email@example.com",
    description="A short description of your project",
    url="http://your_project_homepage.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
