# WorkLog

#### Video Demo:  [**link**](https://www.youtube.com/watch?v=5b9B64svKok)

## Project information

- **Name**: Lorenzo Fattori
- **GitHub username**: lorenzo-fattori
- **edX username**: lorenzo.fattori@icloud.com
- **City and country**: Rimini, Italy
- **Video recording date**: September 30, 2026
**WorkLog** is a web application designed to make it simple to track and manage working hours throughout the month.

## Overview

With WorkLog, users can record their working shifts by entering the relevant information, such as the date, starting time, ending time, and break duration. The application automatically calculates the total number of hours worked and organizes the information in a clear and structured way.

The application is designed around a simple principle: **tracking working hours should be quick, intuitive, and require as little manual work as possible.**

WorkLog can be particularly useful for people who work variable shifts or have schedules that change throughout the month. Instead of manually calculating the total hours worked, users can enter their shifts and let the application handle the calculations.

## Main Features

* Add and manage individual work shifts
* Record starting and ending times
* Account for breaks during a shift
* Automatically calculate total working hours
* Organize shifts by date and month
* View an overview of monthly working hours
* Delete or modify recorded shifts
* Simple and responsive user interface

## Technologies

WorkLog was developed using several technologies and concepts covered throughout **CS50x**:

* **Python** – main programming language
* **Flask** – web framework used for the backend
* **SQLite** – database used to store working hours
* **SQL** – used to interact with the database
* **HTML** – structure of the web pages
* **CSS** – styling and layout
* **JavaScript** – client-side functionality and interactivity
* **Jinja** – templating engine used by Flask

## How It Works

When a user adds a new shift, the application receives the relevant information through a form. Flask processes the request and stores the data in the SQLite database.

The application then calculates the duration of the shift, taking breaks into account, and displays the information in the appropriate section of the application.

By storing each shift in a database, WorkLog can keep track of working activity over time and provide a clearer overview of the user's monthly workload.

## Project Purpose

WorkLog was created as my **final project for Harvard University's CS50x**, with the goal of applying the programming concepts and technologies learned throughout the course to a practical, real-world application.

The project allowed me to work with a complete web application stack, from the frontend interface to backend logic and database management.

More importantly, I wanted to build something that could be useful beyond the scope of the course. WorkLog is based on a real everyday need: keeping track of working hours in a simple and reliable way.

## Future Improvements

There are several features that could be added in future versions of WorkLog, such as:

* User authentication and individual accounts
* Exporting working hours to CSV or PDF
* Monthly and yearly statistics
* Salary and earnings calculations
* Custom hourly rates
* Mobile-focused improvements
* Cloud-based data storage
* Notifications and reminders

## Author

**Lorenzo Fattori**

WorkLog was developed as the final project for **CS50x – Introduction to Computer Science**.
