---
layout: post
title: Predicting Air B&B User Travel
author:
category: data-science
tags: Kaggle
comments: true
use_math: true
archive: false
example: data-science-projects 
index-example: data-science 
excerpt: I outline my steps to predict user interest in traveling for Air B&B. I adopt a neural network classifier routine in Python to predict which country a user will travel to next.
---


{% include toc.md %}

# Competition Description

I decided to have a go at the Kaggle competition for [predicting Air B&B user's
future travel](https://www.kaggle.com/c/airbnb-recruiting-new-user-bookings).

# The Data

The data description can be found
[here](https://www.kaggle.com/c/airbnb-recruiting-new-user-bookings/data).

## Training Data

  train_users.csv - the training set of users

## The Sample Data

The sample data consists of three segmented data sets

### Test Data

test_users.csv - the test set of users

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

### User Data

+ sessions.csv - web sessions log for users
  + user_id: to be joined with the column 'id' in users table
  + action
  + action_type
  + action_detail
  + device_type
  + secs_elapsed

### Population Data

+ age_gender_bkts.csv - summary statistics of users' age group, gender, country 
                        of destination

### Country Data

+ countries.csv - summary statistics of destination countries in this dataset
                  and their locations

# First Examination of the Data

# Predictions of the Data

We should convert the labels into dummy variables and individually predict for
each country. Then join the results together.




