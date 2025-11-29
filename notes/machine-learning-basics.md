from docutils.nodes import classifier

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
- DBSCAN: Density based spatial clustering of applications with noise, doesn't require clusters to be specified in
  advance. Instead needs definition of what makes a cluster and minimum number of observations in one cluster.

## Anomaly detection

- Find outliers. Outliers are observations that significantly differ from normal patterns. Eg. Error code

## Association

- Find relationship between observations. Which objects are bought together? For example, people that bought bread
  are more likely to buy butter, cheese or peanuts along with it in their shopping list.

## Common issues while evaluating a model's performance

- Overfitting: Model performs well on training data set but is unable to perform on test data set because the features
  were highly customized for perfect classification that can't be done with real-time data.
- Accuracy - number of correct predictions / total observations
- Sensitivity - a measure of overall true positives, false positives and false negatives.
- Error: The distance between the point (actual) and the line (expected)

## Improving model performance

3 Terms: Dimensionality reduction, Hyperparameter tuning, Ensemble methods

- Dimensionality reduction: Reduce the number of features - more features can make it more complex and error-prone if
  correlation between features is very low.
- Hyperparameter tuning: Imagine the machine learning model is like a music console, depending on the genre of
  music to be produced it needs different settings to produce good music. In this case, data set is like the genre.
- Ensemble methods: The word "ensemble" means a group of dancers/musicians that perform together. Ensemble methods take
  the same idea, we will use different models to achieve consensus on a prediction either by taking best of three or
  averaging depending on regression use case.

## Deep Learning

- Uses neural networks similar to how human brain works.
- Best suited for unstructured data like large amount of text or images.
- Due to the unstructured nature, this needs large amount of computing power to get effective results.

### Deep learning process

Data acquisition process for deep learning process happens through:

- Computer vision: to visually receive the data on images to see and understand image content (self-driving cars)
- Sensors: Like temperature data, fire-alarms, smoke-alarms (gather features and data)
- Robotics: touch and perception
- Natural Language processing: To process conversations
- Machine Learning: To process the data from everything

## Natural Language processing

- The goal of NLP is to understand human language
- Many NLP techniques and algorithms exist - for example: bag of n-grams, word embeddings etc.,

## Challenges in deep learning space

A lot of deep learning models commercially developed are black box models. We get the model performance data, but
we do not know what data was used for training the data, and why it arrives at a specific prediction.

### Explainability

- Why did this model make this prediction?
- xAI : Explainable AI - Improve democratization of data
- Be transparent about the data and explain how the model applies reasoning
- Bias detection

### Interpretability

- How did this model arrive at this prediction?
- Understand the inner details of the model, its weights and technical details of what makes it a good model
- For a lot of black box models, the weights are not open source.

## Using Huggingface

- Platform with a lot of opensource models
- The `transformers` library is from Huggingface
- Provides pipeline libraries and datasets
- The Huggingface datasets use Apache Arrow which uses columnar format instead of row based, doesn't play well with
  Pandas/DataFrames. Huggingface provides its own python library to `load_dataset`, read and create pipelines.

## Machine Learning - Huggingface pipelines

- Huggingface pipelines accept `task` and `model` as input. There are many `text-classification` models in
  `pipeline` library that helps address many machine learning tasks

```python
from transformers import pipeline

classifier = pipeline(task="text-classification", model="specify-special-model-name-here")
output = classifier("Provide the text input here for classification, when pipeline runs it contains output")
print(output)
```

## Machine Language Task: Text Classification

Text classification involves assigning predefined categories to text. The types are broadly divided to:

- Sentiment Analysis (e.g. positive review vs negative review)
- Grammatical correctness (e.g. grammar checkers, learning tools)
- QNLI (Question Natural Language Inference) (e.g. Few shot prompt where question and answer context is provided)
- Dynamic Category assignment (eg. Zero shot prompting) - this type doesn't always produce accurate results because it
  hasn't been trained on specific labels.

Challenges in text classification:

- Multilingual support is hard, needs robust models
- Text complexities are sometimes hard to classify when one text has many interpretations or meanings.
- Sarcasm, irony and emotional tones are not accurately classified.

## Machine Language Task: Text Summarization

Text Summarization is a process to reduce a large piece of text into smaller one without losing key information.

- This is of two types:
  **Extractive**: Key sentences from text is used for creating summary
  **Abstractive**: New text is generated to summarize the content in a very concise way.
- Pipelines task will specify type `summarization`, optional parameters such as `min_new_tokens` and `max_new_tokens`
  control the length of generated content.
