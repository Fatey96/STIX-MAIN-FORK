# UNCP-Synthetic-Cyber-Knowledge-Graph
The goal of this project is to synthetically generate cyber knowledge graphs to mimic real cyber knowledge graphs. The purpose of generating synthetic knowledge graphs is to train AI to triage large cyber datasets. Knowledge graphs are represented in STIX 2.1 format.

## STIX 2.1
- [Introduction to STIX](https://oasis-open.github.io/cti-documentation/stix/intro.html)

- [Documentation](https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html)

## Built With
- [Angular](https://angular.io/)

- [Django](https://www.djangoproject.com/)

- [STIX 2 Python API](https://stix2.readthedocs.io/en/latest/)

## Getting Started
### File Structure
This project is divided into a frontend and backend folder each with their own README files.
### Frontend
#### Prerequisites
- Install [Node.js](https://nodejs.org/en)

- Install the Angular CLI globally:
```bash
  npm install -g @angular/cli
```
#### Installation
1. Clone the repository:
```bash
  git clone https://github.com/LAS-NCSU/UNCP-Synthetic-Cyber-Knowledge-Graph.git
```
2. Navigate to the frontend folder:
```bash
  UNCP-Synthetic-Cyber-Knowledge-Graph\frontend
```
3. Install dependencies:
```bash
  npm install
```
### Backend
1. Navigate to the backend folder:
```bash
  UNCP-Synthetic-Cyber-Knowledge-Graph\backend
```
2. Install dependecies:
```bash
  pip install -r requirements.txt
```
#### Activate Website
1. Navigate to the frontend folder:
```bash
  UNCP-Synthetic-Cyber-Knowledge-Graph\frontend
```
2. Start Angular server:
```bash
  ng serve
```
3. Navigate to the backend folder:
```bash
  UNCP-Synthetic-Cyber-Knowledge-Graph\backend
```
4. Start Django server:
```bash
  py manage.py runserver
```
5. Go to http://localhost:4200/ in your browser.
