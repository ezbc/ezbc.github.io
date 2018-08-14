---
author: Elijah Bernstein-Cooper
category:
- professional
- tech
comments: true
date: 2018-08-07 00:00:00
layout: post
tags:
- entity-extraction
- python
- spacy
title: Drug Adverse Event Entity Extraction
use_math: false
published: true
image: 
  feature: /media/2018/08/05/text-mining.png
  credit: mcmurryjulie
  creditlink: "https://pixabay.com/en/text-mining-entity-extraction-1476780/"
---

This post walks through steps to create a demo web application,
[https://drug-portal.appspot.com](https://drug-portal.appspot.com), using an
entity extraction model trained with the Python spacy library to reduce the
time spent manufacturers code adverse event reports.

<!--more-->

# Drug Adverse Event Background

Drug adverse events are reported as unstructured notes by physicians when a
patient is experiencing complications from one or more drugs. The physician
submits the report which ends up to the drug manufacturers. The drug
manufacturers must then code the physician's report for side effects. The drug
manufacturer may update the drug product label for patient use.

Product labels of drugs on the market from the FDA provide an enormous
opportunity for researchers for further drug development. The real-world data
can enable researchers to

1. determine new purpose for drug (i.e. new indication for a drug)

1. predict performance of new drugs with similar chemicals.

1. identify drug interactions

1. identify post-market adverse reactions not found in clinical trials

1. identify causal relationships between drugs and adverse reactions

In this post we walk through steps to create an entity extraction service from
FDA drug labels to identify adverse events. The post walks through engineering
a training dataset from a database of tagged drug labels, training a Python
spacy named entity recognition (NER) pipeline, then deploying a web service to
predict adverse event entities in free text.

# Building an Entity Extraction Model with Spacy

## Training Data

Demner-Fushman et al. (2018) provided an exhaustive labeled dataset of adverse
reactions for 200 labels of the most recently-approved drugs. Their dataset is
intended as a benchmarking dataset for other models with benchmarking
resources provided
[here](https://bionlp.nlm.nih.gov/tac2017adversereactions/). However in this
demo we use their database to train our model. 

For each drug label they provided a structured XML document annotated with
entity labels, e.g. Severity or AdverseReaction. For example, for the AdreView
drug label a sample of the label and annotations look like the following:

<script src="https://gist.github.com/ezbc/cb582afcbfe11dfe30e2e62e2d8af265.js"></script>

Download the full labeled dataset [here](https://bionlp.nlm.nih.gov/tac2017adversereactions/train_xml.tar.gz).

## Transforming Annotated Documents

First I transformed the labeled dataset suitable for training a Python spacy
pipeline. For the above example XML the training data would be formatted in the
following way:

<script src="https://gist.github.com/ezbc/52f3a11a32a9d5dfdc920811f529f3a1.js"></script>

I uploaded the annotated XML documents to Google Cloud Storage. Next I
loaded the annotated documents in the following way

<script src="https://gist.github.com/ezbc/cb48038b60aaf4e744dd87b33f8a69b6.js"></script>

I parsed the XML into the spacy [annotated offset scheme](https://spacy.io/api/goldparse#biluo_tags_from_offsets).

<script src="https://gist.github.com/ezbc/f867bf391d64b1c0abb696b77e16394b.js"></script>

Finally, I split the DATA into a test and training dataset

<script src="https://gist.github.com/ezbc/d653167892d08025f0a178fa830a588f.js"></script>

## Training the Entity Extraction Model

Next, I trained a new NER pipeline model in spacy. I passed the train data and
entity labels to train a new pipeline. Note I was not concerned about the
entities in the default spacy model so I did not include training examples
from the default model. For more info read about the [catastrophic forgetting problem](https://explosion.ai/blog/pseudo-rehearsal-catastrophic-forgetting).

<script src="https://gist.github.com/ezbc/36091d84464b2d53ad547e803a6bc990.js"></script>

I saved the model to disk to be deployed later.

## Testing the Model

I evaluated the efficacy of the model against the test data by using the
`spacy.scorer` API.

<script src="https://gist.github.com/ezbc/51badf7fcd818189fa6f200cfa2650ed.js"></script>

We find a recall of 96% and a precision of 100%. The model performs well,
however a precision of 100% is suspicious. Obviously I need to further
investigation the test/train data or the evaluation method.

<!--{'las': 0.0, 'ents_r': 96.42857142857143, 'ents_p': 100.0, 'ents_f': 98.18181818181819, 'uas': 0.0, 'tags_acc': 0.0, 'token_acc': 100.0}-->

## Deploying the Model

Docker allows easier distribution of the model since the model is quite large,
on order of a few hundred megabytes. We can pull the docker image and copy the
model.

The Dockerfile for the model image is simple. It includes steps to copy a
model from the host to the docker image.

{% highlight docker %}
FROM alpine:latest

COPY models .
{% endhighlight %}

Next build the docker image with the model and push it to Google Container
Registry (GCR).

{% highlight bash %}
docker build -t drug-model:1.0.0 .
docker push drug-model:1.0.0 gcr.io/drug-portal/spacy/models/drug:1.0.0
{% endhighlight %}

The model is now available to incorporate into a runtime model. You can find the public repo [here](https://github.com/ezbc/drug-portal-ner-models).

# Building and Deploying a Web App for Entity Extraction

In this demo I serve the app using Google Cloud App Engine. The repo is
located [here](https://github.com/ezbc/drug-portal-ner-api). The app is a
lightlight Flask app running in a custom docker container.

The App Engine configuration `app.yaml` looks like the following:

{% highlight yaml %}
runtime: custom
env: flex
resources:
  cpu: 1
  memory_gb: 2
{% endhighlight %}

Note I specified the cpu and memory to be higher than the default since the
app directly loads the NER model into memory.

I built the docker image locally and pushed the image to GCR.

{% highlight bash %}
docker build -t drug-app:1.0.0 .
docker push drug-app:1.0.0 gcr.io/drug-portal/app:1.0.0
{% endhighlight %}

Finally I deployed the app to App Engine specifying the docker image to use:

{% highlight bash %}
gcloud app deploy --image-url=gcr.io/drug-portal/app:1.0.0
{% endhighlight %}

We can now provide free text for the engine to predict adverse event entity
labels. The app is deployed to the following URL:

<a href="https://drug-portal.appspot.com" style="font-size:12pt">https://drug-portal.appspot.com</a>

## Example Text for Entity Extraction

Submitting the following text from a drug label:

{% highlight bash %}
LABA, such as vilanterol, one of the active ingredients in BREO ELLIPTA, increase the risk of asthma-related death. Currently available data are inadequate to determine whether concurrent use of inhaled corticosteroids or other long-term asthma control drugs mitigates the increased risk of asthma-related death from LABA. Available data from controlled clinical trials suggest that LABA increase the risk of asthma-related hospitalization in pediatric and adolescent patients. Data from a large placebo-controlled US trial that compared the safety of another LABA (salmeterol) or placebo added to usual asthma therapy showed an increase in asthma-related deaths in subjects receiving salmeterol.  [See Warnings and Precautions (5.1).] 
{% endhighlight %}

Predicts the following entities:

<script src="https://gist.github.com/ezbc/8f287f126009883d79cc2faf152b598c.js"></script>

## API

You can also retrieve entities programatically with a simple JSON API to
`https://drug-portal.appspot.com/ner/drug.json`. Submit a request like the following:

<script src="https://gist.github.com/ezbc/7dde186e3c231f8c0ea7d6c05ed3b8c1.js"></script>

# Conclusion

This post walked through steps to create a demo web application using an
entity extraction model. I trained Python spacy entity-recognition pipeline on
an annotated drug label dataset. I deployed a simple web app to easily label
free text with adverse event labels. 

This demo application shows the potential for automatically identifying
adverse events in free text.
