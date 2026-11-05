# Day 03 Assigment
In this week'd assigment, we learned using AI copilot in VSCode to write a pythin program.

## What I did
I decided to work with protein sequences, since this is related to my PhD research.
I had a FASTA file containing sequences and asked the AI agent to write a script that reads the FASTA file, calculate the length of each protein and return a table with the protein's name and length. the output is in Excel file. 

## Prompts I used

My first prompt was:

> In the day03 there is a fasta file. Create a new excel where the first column is the protein name, the second column is the length of the protein.

At first, the AI only suggested code in the chat instead of creating the files. After switching to Agent mode, I used this prompt:

> In the day03 folder, I have a FASTA file called best-rhod_complete_seq.fasta containing multiple protein sequences. Please create a Python script that reads all the protein sequences, calculates the length of each protein in amino acids, and creates an Excel file with the results. Please create the Python file yourself, run the script, and make sure the Excel file is generated successfully.
