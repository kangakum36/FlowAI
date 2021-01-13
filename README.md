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
Finally, you have to install libomp for xgboost to work, on Mac this is:
```
brew install libomp
```


## Data Download
Currently, the only way to get access to the data is by emailing me (kangakum [at] gmail [dot] com) for access to a gcp storage bucket.  Although we have deidentified the data so it contains no information about the patients, we are trying to be **extremely careful** in regulating access. </br>

Once you have access, install the google cloud sdk by following [these](https://cloud.google.com/sdk/docs/install) instructions. </br>
Make sure to say yes when prompted to add ```gcloud``` to your PATH, as the data download script won't work otherwise. </br>
Then run </br>
```
gcloud init
```
Select the flowai project when prompted, you should already have access if you are at this step.
Next run
```
gcloud components update
```
Finally, run the following commands (you must have gcloud added to your PATH) </br>
```
chmod +x ./scripts/download_data.sh
mkdir data
cd scripts
./download_data.sh
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
You should see the an output similar to the following
```
Selected model accuracy is: 0.875
```

Current model tags are 'xgb': Gradient Boosted RF Classifier, 'dtc': Decision Tree Classifier, 'nn': Vanilla Neural Net, 'cnn': Convolutional NN

Once you train/test a model once, the processed dataset will be placed in a pickle (`.p`) file in the `data` folder. </br>
Using the `-p` flag on subsequent model tests will load the dataset from the saved file like so:</br>
```
python3 -W ignore main.py -m [model tag] -p load
```
This way you don't have to wait for the data to be processed every time </br>

## Results and Remarks
Currently, we have implemented cross validation for the XGB and 1D-Convolutional Neural Network Models. </br>
Additionally, we have grid-searched hyperparameters for the XGB model, as it was the most promising in initial tests. </br>
Best average accuracy: Gradient Boosted Classifier (XGB) - 80% (F1 Score also 0.8)
