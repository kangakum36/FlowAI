### Organization updates to this repo and additional models coming soon

# FlowAI
AI project for Flow Cytometry Analysis </br>

This project is aimed at classifying flow cytometry data from 116 patients as either CLL (Chronic Lymphocytic Leukemia) or non-CLL using various Machine Learning methods.  Data is provided by the James A. Haley VA in collaboration with Drs. Andrew Borkowski, Phil Foulis, and Loveleen Kang.</br>

## Prerequisites and Setup
These steps have been tested on macOS 10.15 (Catalina)
Make sure you have python and pip installed: For Mac, first [install homebrew](https://brew.sh/) and then
```
brew install python3
```
Also make sure you have virtualenv installed: </br>
```
python3 -m pip install --user virtualenv
```

Next clone the repo:</br>
```
git clone https://github.com/kangakum36/FlowAI.git
```
Make a new virtual environment and activate it
```
cd FlowAI
python3 -m venv FlowAI
source FlowAI/bin/activate
```
Next install requirements</br>
```
pip3 install -r requirements.txt
```

Currently, the only way to get access to the data is by emailing me (kangakum [at] gmail [dot] com) for access to a google drive containing the case data.  Once you have access, in the FlowAI folder enter: </br>
```
mkdir data
mv <location of FlowCasesDeidentify120519 folder> /data
```

## Making a new model
1. In the Models folder, create a new file (e.g. `<your_model_name>.py`).  Create a class for your model that inherits `BaseModel`.
2. Override the train and test functions.</br>
3. In `main.py`, add an abbreviation for your model to the choices for valid abbreviations in the `parse_args` method.</br>
4. In the main method, there is a series of cascading if statements.  Add your model to this series and do any necessary data processing and training.

## Testing a model
To test a model on the data, </br>
```
python3 -W ignore main.py -m [model tag]
```
Current model tags are 'rfc': Random Forest Classifier, 'dtc': Decision Tree Classifier, 'nn': Keras Neural Net

Our best accuracy to date is the Random Forest Classifier with 83% test accuracy.
