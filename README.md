# 🚨 Cyber Incident Manager

A simple **Python-based Cyber Incident Management System** for creating, searching, updating, and deleting cybersecurity incidents.

The project is built as a **CLI application** and uses **JSON** for persistent data storage.

## ✨ Features

* ➕ Add new security incidents
* 📋 View all incidents
* 🔎 Search incidents by:

  * ID
  * Type
  * Severity
  * Status
* 🔄 Change incident status
* ⚠️ Change incident severity
* 🗑️ Delete incidents
* 💾 Persistent data storage using JSON
* 🆔 Automatic incident ID generation
* 🛡️ Supports common incident types such as:

  * Phishing
  * Malware
  * Brute Force
  * Unauthorized Access
  * Suspicious Login
  * Vulnerability
  * Other

## 🧩 Project Structure

```text
IncidentManager/
│
├── incident.py
├── incident_manager.py
└── Incident.json
```

### `incident.py`

Contains the `Incident` class and defines the structure of an incident, including its ID, title, type, severity, status, reporter, and description.

### `incident_manager.py`

Handles incident management operations such as creating, searching, updating, deleting, and saving incidents.

## ⚙️ Technologies

* Python 3
* JSON
* Object-Oriented Programming
* File Handling
* Exception Handling
* Command-Line Interface (CLI)

## 🚀 How to Run

Clone the repository:

```bash
git clone https://github.com/hemloblack/IncidentManager.git
```

Enter the project directory:

```bash
cd IncidentManager
```

Run the application:

```bash
python incident_manager.py
```

## 🎯 Project Goal

This project was created as a practical Python project to practice **Object-Oriented Programming, JSON data management, file handling, exception handling, and building a small security-focused application**.

It can also serve as a foundation for developing a more advanced incident management system with features such as authentication, databases, logging, APIs, and a web interface.

## 📌 Status

🚧 **In Development**

More features and improvements may be added in future versions.
