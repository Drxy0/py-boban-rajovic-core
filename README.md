# py-boban-rajovic-song-injector

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
`py_boban_rajovic_song_injector` is a Python library designed to help developers integrate and manage Boban Rajović's songs in their Flask applications with SQLAlchemy. It provides a simple way to inject random songs or unique songs into a database for demonstration or entertainment purposes.

## Features
- **Inject random songs**: Add a specified number of songs from Boban Rajović's discography into your database.
- **Avoid duplicates**: Option to inject unique songs without repetition.
- **Flask and SQLAlchemy support**: Seamless integration with Flask applications using SQLAlchemy.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Drxy0/py-boban-rajovic-song-injector
   cd py-boban-rajovic-song-injector
   ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
Before usage a valid database connection needs to be established using Flask-SQLAlchemy.
To use the core functionalities, import the module and call the desired functions:
```python
from py_boban_rajovic_song_injector import BobanRajovicSongInjector

    injector = BobanRajovicSongInjector()
    injector.inject_songs(10)
    injector.inject_songs_no_repeat(10)
```
## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.
## License
This project is licensed under the MIT License.