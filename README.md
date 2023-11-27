# Degrees of Separation

The "Degrees of Separation" project finds the shortest path between two people based on the movies they have starred in, using data from the IMDB dataset.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

This project utilizes a breadth-first search algorithm to determine the shortest path between two people in terms of the movies they have starred in. It reads data from IMDB dataset CSV files to build a graph of relationships between people and movies.

## Features

- Find the shortest path between two people
- Utilizes IMDB dataset for accurate movie and person information
- Flexible directory input for dataset loading

## Getting Started

### Prerequisites

- Python 3.x
- Git (optional)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/degrees-of-separation.git
    ```

    Or download the ZIP file and extract it.

2. Navigate to the project directory:

    ```bash
    cd degrees-of-separation
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the program:

    ```bash
    python degrees.py [directory]
    ```

    If no directory is provided, the default is "large".

2. Follow the on-screen prompts to enter the names of the source and target persons.

3. View the result, including the degrees of separation and the path details.

## Data

The project uses data from three CSV files: `people.csv`, `movies.csv`, and `stars.csv`. Ensure these files are present in the dataset directory.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- Thanks to the creators of the IMDB dataset for providing valuable data.
- This project is inspired by the concept of six degrees of separation.
