# IDS706-Week_2_Mini-project 

[![Python Stats CI](https://github.com/nogibjj/IDS-Week2_MiniProject_us26/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/IDS-Week2_MiniProject_us26/actions/workflows/main.yml)

<p align="center">
  <img width="250" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Standard_Normal_Distribution.png/1920px-Standard_Normal_Distribution.png" alt="My Image">
</p>

## Overview

This repo has been created using my week 1 mini project as the template which has all the necessary steps to automate the process and I will be using that repo for my future projects as well. 
The current repo is for creating _*Pandas Descriptive Statistics Script*_ using DevOps principles.


## Code Description

1. stats_descriptive.py - This python file contains 3 function to calculate mean , median and mode
2. test_stats.py - This python file contains a dummy data that test the functions and asserts the true value


## CI/CD Automation files

1. requirements.txt - Contains all the required python packages
2. Makfefile - Using make to automate different parts of developing a Python project, like -
   
       1. running tests
       2. cleaning builds
       3. installing dependencies
   
   Integrating it into my routine, so can save time and avoid errors.
   
5. .github/workflows - This directory in a Python project (or any GitHub repository) is used for creating and storing GitHub Actions workflows. GitHub Actions is a continuous integration and continuous delivery                           (CI/CD) platform provided by GitHub. The workflow is triggered on pushes to the main branch. It sets up :
   
       1. Python environment
       2. Installs project dependencies
       3. Install packages
       4. Linitng
       5. Runs tests
       6. Format
    

