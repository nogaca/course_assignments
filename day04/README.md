# Day 04 Assignment

In this week's assignment, we learned how to create a web application using Flask.

## What I did

I continued working on my project from Day 03, where I wrote a Python script to calculate protein lengths from FASTA sequences.

I copied the project into the day04 folder and used AI in VS Code to turn it into a web application using Flask.

## How to run the web application

1. Download or clone this repository from GitHub.
2. Open a terminal and navigate to the `day04` folder.
3. Install the required Python packages:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```bash
   python3 app.py
   ```

5. Open a web browser and go to:

   http://127.0.0.1:5000/

## How to use the application

The application allows users to analyze protein sequences in two ways:

- Upload a FASTA file containing one or more protein sequences.
- Paste FASTA sequences directly into the text box.

Click "Analyze sequences" to calculate the length of each protein.

The results will appear in a table showing the protein names and their lengths in amino acids.

To stop the application, press Ctrl+C in the terminal.