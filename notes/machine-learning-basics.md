## Machine Learning basics

- Predicting the outcome of future events
- Machine Learning takes the concepts from computer science, Artificial Intelligence takes concepts from statistics.

## Three types of machine learning

- Supervised Learning :
    - SubTypes: Classification and Regression
    - Supervised Learning works with Labelled data, model is trained on labelled dataset extracted features
- Unsupervised Learning:
    - SubTypes: Clustering (K-Means clustering, DBSCAN), Anomaly Detection
    - Model trains itself by observing patterns and dividing data into groups
- Reinforcement learning: Eval loop

## Machine learning workflow

- Take dataset (Patient health history)
- Extract features from the data set (Age, habits, lifestyle, health factors)
- Split to training data set, test data set (2/3 of data for training, 1/3 for testing)
- Train the model using training data set (any method - supervised or unsupervised)
- Test the model using test data set
- Run eval loop to improve prediction rate

## What is the difference between Classification and regression?

- Classification assigns a fixed category (e.g. a bird, a dog)
- Regression assigns a continuous variable (e.g. How long can this bird fly during summer?)

### Key Terms

- Features: different pieces of information that help predict the target (Eg. Age, Cholesterol, health factors)
- Target: What needs to be measured/predicted (Eg: Heart disease)
- Label: Category how to divide the given dataset (True or False, Yes or No)

## Unsupervised learning

- Model trains itself by spotting patterns or groups of data
- Some clustering algorithms like K-means require to specify clusters ahead of time
- DBSCAN: Density based spatial clustering of applications with noise, doesn't require clusters to be specified in advance.
- Instead define what makes a cluster and minimum number of observations in one cluster.

## Anomaly detection
- Find outliers. Outliers are observations that significantly differ from normal patterns. Eg. Error code

## Association
-  Find relationship between observations. Which objects are bought together? For example, people that bought bread
are more likely to buy butter, cheese or peanuts along with it in their shopping list.

## Common issues while evaluating a model's performance
- Overfitting: Model performs well on training data set but is unable to perform on test data set because the features
were highly customized for perfect classification that can't be done with real-time data.
