# my_gpa_app

A sleek, professional GPA Management System built with **Streamlit** and **Supabase**. This portal allows students to calculate their semester GPA, track cumulative progress, and securely save their academic data to the cloud.

## Features
* **Secure Authentication:** Custom Login/Register system using Supabase.
* **GPA Calculator:** Real-time calculation of semester and cumulative GPA.
* **Cloud Sync:** Automatically saves and retrieves your grades from a secure database.
* **Modern UI:** A clean, "Academic Purple" custom-styled interface.
* **Data Export:** Capability to view academic history in a clean, organized table.

## Tech Stack
* **Frontend:** Streamlit (Python-based Web Framework)
* **Backend:** Supabase (PostgreSQL Database & Auth)
* **Styling:** Custom CSS for a professional portal experience.

## How to Run Locally
1. Clone this repository.
2. Install requirements: `pip install -r requirements.txt`.
3. Create a `.streamlit/secrets.toml` file with your Supabase credentials.
4. Run the app: `streamlit run Home.py`.

