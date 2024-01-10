# Hotel Booking Web App

This is a simple hotel booking web application built using Flask.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Hotel Booking Web App is a Flask-based web application that allows users to search for hotels, view details, and make bookings. The application also includes features such as user authentication, special prices, and member benefits.

## Features

- Search for hotels based on location, dates, and number of guests.
- View detailed information about each hotel.
- Special prices section showcasing discounted hotel rates.
- User authentication for personalized experiences.
- Member benefits for registered users.
- Responsive design for various screen sizes.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/DenginDkn/Hotel_Booking_App.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database:

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

4. Run the application:

    ```bash
    python run.py
    ```

## Usage

1. Visit the application in your web browser at [http://localhost:5000/](http://localhost:5000/).
2. Explore the different sections, search for hotels, and interact with the features.

## Project Structure

The project structure follows a standard Flask application layout:

- `app/`: Contains the main application package.
    - `templates/`: HTML templates for rendering pages.
    - `static/`: Static files (CSS, images, JS).
    - `routes.py`: Defines the application routes.
    - `models.py`: Defines database models.
    - ...

- `config.py`: Configuration settings for the application.
- `run.py`: Entry point to run the application.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Submit a pull request.

## Project Explanation Video

The content of this project, including the code and documentation, is also available on YouTube. Watch the accompanying video: [Project Overview on YouTube](https://www.youtube.com/watch?v=_nbMkxICJjc).
