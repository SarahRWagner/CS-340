# CS 340: Interactive Dashboard for Austin Animal Center Outcomes

**Author:** Sarah Wagner  
**Date:** 02/23/25  

## Project Overview

This project implements a CRUD (Create, Read, Update, Delete) system using Python and MongoDB to interact with the Austin Animal Center (AAC) Outcomes dataset. Additionally, it includes an interactive dashboard for Grazioso Salvare to analyze and visualize animal outcomes.

### The dashboard provides:
- Interactive filtering for different animal types and rescue categories.
- Dynamic data table that updates based on selected filters.
- Geolocation map displaying selected animal locations.
- Interactive charts, including a pie chart for top animal breeds and a bar chart for age distribution.
- Reset button to clear applied filters.
- Branding with the Grazioso Salvare logo and unique identifier (Sarah Wagner).
- Filters to identify suitable dogs for specific types of rescue training:
  - Dogs under 2 years old.
  - Dogs categorized by rescue type (Water Rescue, Mountain Rescue, Tracking).
  - Top breeds suited for each rescue category based on historical outcomes.

## Motivation

This project aims to integrate Python and MongoDB to develop a data-driven web application. The key objectives include:
- Demonstrating CRUD operations using PyMongo.
- Implementing reusable Python modules for database interactions.
- Creating an interactive dashboard for data visualization and analysis.
- Exploring NoSQL database benefits for handling semi-structured data.

MongoDB was chosen for its flexibility in storing unstructured animal data, scalability, and seamless integration with Python. PyMongo enables efficient CRUD operations, while Dash provides an intuitive interface for data visualization.

## Tools and Technologies Used

### 1. MongoDB (Model Component)
- **Flexibility:** Stores animal records efficiently.
- **Scalability:** Handles large datasets.
- **Python Compatibility:** Integrates with PyMongo for seamless data retrieval.

### 2. Dash Framework (View & Controller)
- Rapid development of interactive dashboards.
- Integration with Plotly for visualizations.
- Simple UI components linked with callbacks.

### 3. Additional Libraries
- `dash` – UI components and callbacks.
- `dash_leaflet` – Geolocation mapping.
- `dash_table` – Interactive data table.
- `plotly.express` – Pie and bar chart visualizations.
- `pandas` – Data manipulation.
- `base64` – Encoding for displaying the logo.

## Installation and Setup

### Prerequisites

Ensure the following tools are installed:
- **Python 3.7+**
- **MongoDB (Version 6.0 or newer) with AAC dataset**
- **Required Python libraries** (installed via `requirements.txt`)

### Steps to Set Up the Project

#### 1. Install Python
Download and install Python 3.10+ from Python's official site. Ensure Python is added to your system PATH.

Verify installation:
```sh
python --version
```
Expected Output:
```sh
Python 3.10.x
```

#### 2. Install MongoDB
Download MongoDB Community Edition from MongoDB Download Center.

Verify installation:
```sh
mongod --version
```
Expected Output:
```sh
db version v6.0.x
```

#### 3. Set Up the MongoDB Database

Import the AAC dataset:
```sh
mongoimport --host localhost --port 27017 --db AAC --collection animals --type csv --headerline --file aac_shelter_outcomes.csv
```
Expected Output:
```sh
imported {x} documents
```

Create a MongoDB User for Authentication:
```sh
mongosh
use AAC
db.createUser({
  user: "aacuser",
  pwd: "pwd123",
  roles: [{ role: "readWrite", db: "AAC" }]
})
```
Expected Output:
```sh
Successfully added user: { "user" : "aacuser", "roles" : [ "readWrite" ] }
```

#### 4. Clone the Repository and Install Dependencies for Dashboard use
```sh
git clone https://github.com/SarahRWagner/CS-340.git
cd grazioso-dashboard
pip install -r requirements.txt
```

#### 5. Configure MongoDB Credentials
Edit `crud_mongodb.py` and update connection details:
```python
self.client = pymongo.MongoClient("mongodb://aacuser:password@localhost:27017/AAC")
```

#### 6. Connect to Jupyter Lab and Run Dashboard file
Open [http://127.0.0.1:8050/](http://127.0.0.1:8050/) in a web browser to interact with the dashboard.

## Features and Functionality

### CRUD Operations
The `AnimalShelter` class in `crud_mongodb.py` provides:
- `create(data)`: Inserts a document.
- `read(query)`: Retrieves documents based on a filter.
- `update(query, update_data)`: Updates documents and returns the number modified.
- `delete(query)`: Deletes documents and returns the number removed.

### Dashboard Components
- **Interactive Filtering:** Users can select animal types or rescue categories.
- **Data Table:** Displays sorted and filtered animal records.
- **Geolocation Map:** Shows selected animal locations.
- **Pie Chart:** Displays the top 5 breeds.
- **Bar Chart:** Shows age distribution.
- **Reset Button:** Clears all filters.

## Challenges and Solutions

### Handling Large Datasets in MongoDB Queries
- **Challenge:** Initial queries retrieved too much data, causing performance issues.
- **Solution:** Used query filters to limit data retrieval and improve responsiveness.

### Ensuring Map Updates Correctly
- **Challenge:** Map failed to update when no location data was available.
- **Solution:** Implemented error handling and default coordinates when data was missing.

### Styling and Layout Issues
- **Challenge:** UI elements were not aligned properly.
- **Solution:** Used CSS flexbox to maintain a consistent layout across screen sizes.

## Testing

### Running the Tests
- Open `test_crud.ipynb` in Jupyter Notebook.
- Ensure MongoDB is running and the AAC database is accessible.
- Run all notebook cells to validate functionality.

### Expected Test Outputs
- **Insert Test:** Should return `Insert Successful: True`.
- **Read Test:** Should return a list containing the inserted document.
- **Update Test:** Should return `Documents Updated: [number_of_modified_documents]`.
- **Delete Test:** Should return `Documents Deleted: [number_of_deleted_documents]`.

## Conclusion

This project successfully integrates MongoDB with Dash to create an interactive data visualization tool for Grazioso Salvare. The dashboard enables real-time analysis of animal outcomes, making it a valuable resource for rescue operations.

## Reflection

### Writing Maintainable, Readable, and Adaptable Programs

Keeping code reusable and well-documented makes it easier to maintain over time. In Project One, I built a CRUD Python module to handle database interactions with MongoDB, keeping all database logic separate from the dashboard in Project Two. This approach made the dashboard more scalable and easier to debug since any database updates could be made in one place without touching the UI. It also helped with error handling and kept things clean and organized.

This CRUD module isn’t just useful for this project. It could be reused in other applications that need to interact with MongoDB. It could also be expanded to support new features like data aggregation or even turned into a REST API, so multiple applications could connect to it.

### Approaching a Problem as a Computer Scientist

When tackling a problem, I break it down into smaller steps. For this project, I started by understanding what data Grazioso Salvare needed, then created the MongoDB database for efficient searches. After that, I built the CRUD functions, dashboard components, and interactive charts step by step. This project was different from past assignments because it required full-stack thinking, integrating a database with an interactive UI instead of just writing backend logic or algorithms.

In future projects, I’d focus on scalability and security from the start, using API-based database access, indexing for performance, and role-based access control. These strategies would make databases faster, more secure, and easier to integrate with other systems.

### Why Computer Science Matters

Computer scientists solve real-world problems with data and technology. This project helps Grazioso Salvare make better decisions faster by organizing animal shelter data in a way that’s quick to filter and visualize. Instead of manually sorting through data, staff can instantly find the best dogs for rescue training.

Beyond this, software like this can help organizations work smarter, whether it’s in healthcare, finance, or research. By making information easier to access and analyze, we help people focus on what really matters—in this case, saving lives through search-and-rescue training.

