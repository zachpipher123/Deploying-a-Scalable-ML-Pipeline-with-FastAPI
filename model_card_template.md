# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
The model is a random forest classifier from scikit-learn on data about income
## Intended Use
The purpose of this model is to forumlate a individuals salery based on many factors. This could be used to collect important information with reletive accuracy.
## Training Data
Data provided by Udacity, census.csv will be used to train the model with a split of 80% and 20% committed to training and testing respectively.
## Evaluation Data
Data provided by Udacity, census.csv will be used to train the model with a split of 80% and 20% committed to training and testing respectively.
## Metrics
_Please include the metrics used and your model's performance on those metrics._
Precision : 0.7416
Recall: 0.6488
F1 Score: 0.6898
## Ethical Considerations
The dataset used could have inherant biases that should be considered when using a model for this purposes as it could give unfair assessments for the unaccounted for population of people.
## Caveats and Recommendations
The model can only be as accurate as the data is up to date. Since the information is older its important to supply more up to date information to be more accurate