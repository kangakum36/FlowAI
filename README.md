# FlowAI
AI project for Flow Cytometry Analysis

# Data Processing:
We start by using FlowCytometryTools (https://eyurtsev.github.io/FlowCytometryTools/install.html) to convert fcs files to pandas dataframes and then numpy arrays.
Then, using the James A Haley Veterans Hospital's Flow Cytometry spreadsheet, we match each tube's flourochromes with the corresponding antibodies.  As a result, we are able to generate a numpy array for each patient.

Then using fancyimpute's (https://github.com/iskandr/fancyimpute) softimpute algorithm, which is meant for large, sparsely populated matrices (ours are 10^6 x 33, with 39.4% or 10^7 observed entries) , we impute the missing data into each's patients array.

# Training using Keras
WIP
