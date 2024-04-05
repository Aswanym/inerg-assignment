# Annual data calculation - Assignment

## introduction
#### This project will insert an Excel file data into a sqlite database and can access the data from it using django api.

## Getting Started

### Prerequisites
- Python (version 3.9.7)
- Django (version 4.2.11)

### Installation

1. Clone the repository:
   ```bash
   https://github.com/Aswanym/inerg-assignment.git
   
2. Create virtual environment
   ```bash
      virtualenv venv
   
3. activate virtualenv (windows)
   ```bash
      venv/Scripts/activate
   
4. Install dependencies
   ```bash
      pip install -r requirements.txt
      
   
5. Configuration
- Create a .env file in the project root. 
- Add the following environment variables to the .env file:

   ```bash
  SECRET_KEY=your_secret_key
  PATH_TO_EXCEL_FILE=your_excel_file_location
  DB_LOCATION=your_db_loacation_in_local
  
- Replace the placeholder values with your actual values.

6. Running script to load data to db
    ```bash
      python annual_data\db_data_population_script.py 
7. Database Migration
   ```bash
   python manage.py migrate
   
8. Running the Server - Start the development server:
   ```bash
   python main.py

9. Visit http://localhost:8080/ in your browser to view project.
