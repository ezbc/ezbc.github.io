---
author: Elijah Bernstein-Cooper
category:
- professional
- data-science
comments: true
date: 2016-02-13 00:00
excerpt: I outline my steps to predict user interest in traveling for Air B&B. I adopt
  a neural network regression routine in Python to predict which country a user will
  travel to next.
layout: post
tags:
- Kaggle
title: Predicting Air B&B User Travel
use_math: true
redirect_from:
- /data-science/2016/02/13/air-bnb-predictions
- /2016/02/13/air-bnb-predictions
---

I outline my steps to predict user interest in traveling for Air B&B. I adopt a
neural network regression routine in Python to predict which country a user will
travel to next. With just a rudimentary application of readily available Python
routines I am able to predict the majority of more than 60,000 countries an Air
B&B user will travel to next. You can find the source code here:
[https://github.com/ezbc/airbnb](https://github.com/ezbc/airbnb).



# Competition Description

I decided to have a go at the Kaggle competition for [predicting Air B&B user's
future travel](https://www.kaggle.com/c/airbnb-recruiting-new-user-bookings).
My goal is to predict the next country a user will visit given a small amount of
personal data about the user. Entries are evaluated with a [normalized
discounted cumulative
gain](https://www.kaggle.com/c/airbnb-recruiting-new-user-bookings/details/evaluation).

Air B&B provides several datasets, however the most integral data are the
training and test dataset. We will use the training dataset which include the
country the user will visit to fit our predictive model. We will then predict
the country a user will visit for each user in the test dataset. We could
improve our analysis by partitioning the training dataset into a validation
dataset to perform cross-validation with our model predictions. This would
ensure that we do not over-fit our model to the data.

# The Data

The data description can be found
[here](https://www.kaggle.com/c/airbnb-recruiting-new-user-bookings/data).

## Training Data

The train data possess fourteen attributes for about half a million users.

+ id: user id
+ date_account_created: the date of account creation
+ timestamp_first_active: timestamp of the first activity, note that it can be earlier than date_account_created or date_first_booking because a user can search before signing up
+ date_first_booking: date of first booking
+ gender
+ age
+ signup_method
+ signup_flow: the page a user came to signup up from
+ language: international language preference
+ affiliate_channel: what kind of paid marketing
+ affiliate_provider: where the marketing is e.g. google, craigslist, other
+ first_affiliate_tracked: whats the first marketing the user interacted with before the signing up
+ signup_app
+ first_device_type
+ first_browser
+ country_destination: this is the target variable you are to predict

### Test Data

The test set of users separate from the sample data. These data
do not contain the country_destination variable.

# Preparing the Data

I use the `pandas` library in Python to handle all subsequent analysis of the
data. First we must prep the data. This includes filtering empty user data, and
creating dummy categorical variables in order to perform a regression on the
data. To keep the data preparation simple I ignore all date-time variables in
the analysis.

For continuous variables, I convert empty user variable values to the mean value
of that variable for all users. This includes age and signup_flow.

Next, I create dummy variables for each categorical variable. For each
categorical variable I tally the number of unique values, then create a new
dummy variable for each unique value. I populate the dummy variables with either
a 1 if the categorical variable of a user contained the dummy variable value,
and a 0 if not.

We are now ready to predict user destinations.

# Applying the Predictive Model

I use the [`rep`](http://yandex.github.io/rep/) Python package as a wrapper for
the [`theanets`](https://pypi.python.org/pypi/theanets) Neural Network
Classification module. The particular
[application](http://theanets.readthedocs.org/en/stable/api/models.html) of
`theanets` as a neural network regressor involves minimizing the sum of the
squared error between the data and model plus a regularization term.  I use the
number of train users as the number of input
[http://theanets.readthedocs.org/en/stable/api/layers.html], and then number of
test users as the number of output layers. I adopt the default activation (loss)
function for each layer: a logistic function.

# Regression

The regression requires about 10 minutes on a standard laptop. I receive a
normalized discounted cumulative gain score of $0.67$. With just a rudimentary
application of readily available Python routines I am able to predict the
majority of more than 60,000 countries an Air B&B user will travel to next.