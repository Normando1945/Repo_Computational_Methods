<p align="center">
  <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbTgzZGc0czVnY3ByZWZkZnlkaGlqeGJiaWU2cTZxOWNzdzgybGl0byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LPWgnWIytRmDH4OvTl/giphy.gif" width="50%" alt="Seismic Desing Banner">
</p>

# Seismic-Resistant Design

### Educational Repository for Seismic Design and Structural Engineering

**Author:** Msc. Ing. Carlos Andrés Celi Sánchez  
**Semester:** FEB – 2026

This repository has been created to support the teaching process of the **Seismic-Resistant Design** course during the current academic semester. It will progressively include theoretical notes, design criteria, Python-based educational tools, numerical examples, and class materials related to the structural dynimics and seismic analysis of structures.

This repository is **currently under construction** and will continue to be updated throughout the semester as new topics are covered in class.

## Course Roadmap

This repository is expected to progressively cover topics such as:

- Fundamental concepts of earthquake engineering
- Seismic hazard and design philosophy
- Structural regularity and irregularity
- Lateral force-resisting systems
- Equivalent lateral force procedures
- Modal analysis concepts
- Design spectra and seismic parameters
- Drift control and serviceability checks


## Current Contents

At its current stage, the repository includes:

- The initial base structure of the course repository
- Introductory files for future class materials
- A progressive framework for organizing notebooks, notes, and design examples
- Setup files for future computational implementations

## Repository Structure

    Repo_Seismic_Desing/
    │── examples/
    │── notes/
    │── seismic_design/
    │   └── __init__.py
    │── README.md
    │── requirements.txt
    │── setup.py

> **Note:** The repository structure may evolve during the semester as new material is incorporated.

## Prerequisites

Before working with this repository, students should make sure that the following software is installed on their computers:

- **Python 3.10 or newer**
- **Git**
- **Visual Studio Code**
- **Python extension for VS Code**
- **Jupyter extension for VS Code**

These tools are necessary to clone the repository, create the Python environment, open the project correctly in Visual Studio Code, and run both Python scripts and notebooks.

## Installation Guide for Windows and VS Code

This section explains how to correctly install and run the repository on **Windows** using **Visual Studio Code**.

### Step 1. Open the Windows terminal

Before doing anything else, students should first open a standard **Windows terminal**.

They may use any of the following:

- **Command Prompt**
- **Windows PowerShell**

For this course, the recommended option is:

> **Command Prompt**

This helps avoid confusion with terminal commands, file paths, and virtual environment activation steps.

### Step 2. Clone the repository

Once the Windows terminal is open, run:

```bash
    git clone https://github.com/Normando1945/Repo_Seismic_Desing.git
```

This command will download the repository to the current folder.

### Step 3. Move into the repository folder

After cloning the repository, enter the project folder with:
```bash
    cd Repo_Seismic_Desing
```
From this point on, all commands should be executed inside this folder.

### Step 4. Open the repository in Visual Studio Code

Now that the repository already exists on the computer, open it in **Visual Studio Code** by running:
```bash
    code .
```
If this command does not work, students can simply open **Visual Studio Code** manually and then select the cloned repository folder.

### Step 5. Open the integrated terminal in VS Code

Once the repository has been opened in VS Code, it is recommended that students continue working from the **integrated terminal** inside VS Code.

To open the terminal in VS Code:

- Press **Ctrl + Shift + `**
- Or go to the top menu and select:  
  **Terminal > New Terminal**

A terminal panel will appear at the bottom of Visual Studio Code.

### Step 6. Verify that the terminal is Command Prompt

Inside VS Code, verify that the selected terminal is:

- **Command Prompt**

If another terminal appears and students want to change it:

1. Click the dropdown menu in the terminal panel
2. Select **Command Prompt**
3. Open a new terminal

From this point on, it is recommended that all commands be executed from this terminal in VS Code.

### Step 7. Create a virtual environment

It is strongly recommended to create a virtual environment so that all students work with the same isolated Python setup.

Run:
```bash
    python -m venv venv
```
This command will create a folder called `venv` inside the repository.

### Step 8. Activate the virtual environment in Windows

If students are using **Command Prompt**, run:
```bash
    venv\Scripts\activate
```
After activation, `(venv)` should appear at the beginning of the terminal line. This indicates that the virtual environment is active.

### Step 9. Install the required dependencies

Once the virtual environment has been activated, install the required Python libraries with:
```bash
    pip install -r requirements.txt
```
This step installs all the packages needed by the repository.

### Step 10. Install the repository in editable mode

To allow Python to recognize the package correctly while developing and testing the code, run:
```bash
    pip install -e .
```
This is useful because the package can be modified during the semester without reinstalling it every time.

### Step 11. Install Jupyter support inside the environment

If students are going to work with notebooks in VS Code, it is recommended to also install `ipykernel`:
```bash
    pip install ipykernel
```
Then register the environment as a Jupyter kernel:
```bash
    python -m ipykernel install --user --name=venv --display-name "Python (Seismic Design)"
```
This will allow students to select the correct Python environment when opening notebooks.

### Step 12. Select the correct interpreter in VS Code

Inside **Visual Studio Code**, follow these steps:

1. Press **Ctrl + Shift + P**
2. Search for: `Python: Select Interpreter`
3. Choose the interpreter corresponding to the `venv` environment

If a notebook is opened, also make sure that the selected kernel is:

`Python (Seismic Design)`

### Step 13. Verify that the installation works correctly

A simple way to verify the installation is to open Python and try importing the main package.

Run:
```bash
    python
```
Then type:
```bash
    import seismic_design
    print("Package imported successfully")
```
If no error appears, the installation was completed correctly.

## First Stage of the Repository

Since the repository is still being developed, the first stage is focused on building a solid educational base for the course. This may include:

- Introductory notes
- Basic seismic design concepts
- Initial numerical examples
- Class-based Python tools for future applications
- Progressive organization of notebooks and supporting files

As the semester advances, more files and examples will be added.

## Recommended Workflow for Students

For each class session, students are encouraged to follow the workflow below:

1. Open the repository folder in VS Code
2. Open the integrated Command Prompt terminal
3. Activate the virtual environment
4. Verify that the correct Python interpreter has been selected
5. Open the corresponding notebook or Python file
6. Run the examples step by step
7. Modify the examples progressively as discussed in class
8. Save the updated work in an organized manner

This workflow helps maintain consistency during the semester and reduces the most common installation and execution errors.

## Updating the Repository

Since the repository will be updated progressively during the semester, students should regularly download the latest changes from GitHub.

### Step 1. Open the terminal

Open **Command Prompt** or the **integrated terminal in VS Code**.

### Step 2. Move into the repository folder
```bash
    cd Repo_Seismic_Desing
```
### Step 3. Activate the virtual environment

If students are using **Command Prompt**, run:
```bash
    venv\Scripts\activate
```
### Step 4. Pull the latest changes
```bash
    git pull
```
This command downloads and merges the most recent changes from the remote repository into the local copy.

### Recommendation

Students are encouraged to run `git pull` before starting each class session in order to work with the latest version of the repository.

## Summary of the Main Installation and Update Commands

### First-time installation
```bash
    git clone https://github.com/Normando1945/Repo_Seismic_Desing.git
    cd Repo_Seismic_Desing
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    pip install -e .
```
### Regular update before class
```bash
    cd Repo_Seismic_Desing
    venv\Scripts\activate
    git pull
```
## Additional Notes

- If Git is not recognized in the terminal, it must be installed and added correctly to the system path.
- If Python is not recognized in the terminal, verify that Python was installed correctly and added to the system path.
- If a notebook does not run, first verify that the correct Python interpreter and Jupyter kernel have been selected.
- It is recommended that all package installations be done only after activating the virtual environment.
- Students should avoid installing packages globally unless it is absolutely necessary.
- Since the repository is installed in editable mode, updates to the package files will be reflected directly without reinstalling the package in most cases.
- Because the repository is still under development, some folders or files may appear progressively during the semester.

## Important Note for Students

This repository is maintained exclusively by the course author.

Students are expected to clone the repository and update their local copies during the semester. They should not modify the original online repository.

If students wish to experiment with the code, they are encouraged to do so in their local copies or in personal forks of the repository.

## How to Cite

If you use this repository in academic work, class projects, reports, or educational material, please cite it as follows.

### BibTeX

    @misc{celi2026seismicdesign,
      author       = {Carlos Andrés Celi Sánchez},
      title        = {Seismic-Resistant Design: Educational Repository for Seismic Design and Structural Engineering},
      year         = {2026},
      publisher    = {GitHub},
      journal      = {GitHub repository},
      howpublished = {\url{https://github.com/Normando1945/Repo_Seismic_Desing}}
    }

### APA (7th Edition)

Celi Sánchez, C. A. (2026). *Seismic-Resistant Design: Educational Repository for Seismic Design and Structural Engineering* [Structural Engineering]. GitHub. https://github.com/Normando1945/Repo_Seismic_Desing

## License
<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License">
</p>

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

This repository is maintained by the author as the official course repository for **Seismic-Resistant Design**.

Students are encouraged to use the repository, report bugs, and suggest improvements whenever necessary. Nevertheless, the official development and organization of the repository remain under the supervision of the author.

Suggestions for improvement may be shared through issues or pull requests, which will be reviewed before any change is incorporated into the repository.

## General Recommendation

Students are encouraged to keep this repository updated throughout the semester and use it as the main reference point for class notes, numerical examples, design criteria, and the progressive development of seismic-resistant design tools and concepts.
