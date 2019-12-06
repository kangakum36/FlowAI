# FlowAI
AI project for Flow Cytometry Analysis

All of the data in the files we process is de-identified, meaning there is nothing in the files that links the data to the patient.  However, in the interest of being ultra-cautious and HIPPA compliant, we will not be
pushing the testcases(patient files) to github.  If you would like them, contact us and we will go through the proper channels to get you access.

# Data Processing:
We start by using FlowCytometryTools (https://eyurtsev.github.io/FlowCytometryTools/install.html) to convert fcs files to pandas dataframes and then numpy arrays.
Then, using the James A Haley Veterans Hospital's Flow Cytometry spreadsheet, we match each tube's flourochromes with the corresponding antibodies.  As a result, we are able to generate a numpy array for each patient.

Then using fancyimpute's (https://github.com/iskandr/fancyimpute) softimpute algorithm, which is meant for large, sparsely populated matrices (ours are 10^6 x 33, with 39.4% or 10^7 observed entries) , we impute the missing data into each's patients array.

# Training using Keras:
WIP
