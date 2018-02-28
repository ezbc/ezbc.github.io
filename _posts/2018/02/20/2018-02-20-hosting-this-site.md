---
author: Elijah Bernstein-Cooper
category:
- professional
- tech
comments: true
date: 2018-02-20 00:00:00
layout: post
tags:
- jekyll
- firebase
- travis-ci
title: Continuous Integration of this Blog in Firebase 
use_math: false
published: true
---

<img src="/media/2018/02/18/next-level.jpg">

Ready to take your Jekyll site to the next level from Github pages? Learn how
to use Firebase's global content delivery system to have complete control over
your development process and hosting.

<!--more-->

# Reasons to Use Firebase

[Firebase](https://firebase.google.com/) is a mobile and web application
development platform. Firebase provides static website hosting, just like
Github pages. Below are a few reasons you may want to consider Firebase over
Github for hosting your static site:

1. *Manage Multiple Environments* --- Interested in testing SSL certificates
   before deploying to production? How about search engine indexing?
   Interested in testing in an environment not production? Github pages offers
   one hosted site per user. This means no development site unless owning two
   Github accounts sounds is appealing. In Firebase you can host multiple
   projects. One project can host a development site. One project can host
   your production site.

1. *Web Application Hosting* --- If the time comes to expand your static
   website to a web application [Firebase 
   functions](https://firebase.google.com/docs/functions/) will seamlessly
   allow you to build out your webapp from the comfort of your static site.
   For example if you want to create dynamic content in a portfolio you could
   route the requests to the portfolio page to Firebase functions which would
   serve up your dynamic content.

1. *Deployment Control* --- Did you just deploy a huge mistake to production
   and need to rollback? With Firebase, just login to the console, find the
   latest deployment, and click the rollback button. Simple. In Github pages
   you would need to revert to a previously stable commit and push the branch
   to Github.

1. *Route Control* --- Firebase provides flexible static
   website hosting. You can configure
   [routes](https://firebase.google.com/docs/hosting/url-redirects-rewrites)
   easily in Firebase.

# Hosting Overview with Jekyll, Travis-CI, and Firebase

[Jeykll](https://jekyllrb.com) is a static site generator. The product is a
simple and flexible solution for bloggers. 

[Travis CI](https://travis-ci.org/) is an managed continuous integration
service to build and deploy projects in Github. Travis CI is *free* for public
projects on Github. The service offers flexible build configurations and
integrates with many popular products for [deployment](https://docs.travis-
ci.com/user/deployment).

I develop this site locally and push changes to Github, Github notifies Travis-
CI, Travis-CI builds this site in a container and deploys to Firebase to host
the static content.

# Getting Started

## Firebase Setup

Firebase 

The [Firebase CLI](https://firebase.google.com/docs/cli/)

Login to firebase to get auth key for non-interactive.
`firebase login:ci`

{% highlight raw %}
You're about to initialize a Firebase project in this directory:

  <directory>

? Which Firebase CLI features do you want to setup for this folder? Press Space 
to select features, then Enter to confirm your choices. (Press <space> to select
)
❯◯ Database: Deploy Firebase Realtime Database Rules
 ◯ Firestore: Deploy rules and create indexes for Firestore
 ◯ Functions: Configure and deploy Cloud Functions
 ◯ Hosting: Configure and deploy Firebase Hosting sites
 ◯ Storage: Deploy Cloud Storage security rules
{% endhighlight %}

Select the hosting option. The CLI will take you ask which project to select

{% highlight raw %}
? Select a default Firebase project for this directory: (Use arrow keys)
❯ [don't setup a default project] 
  MyProject (myproject) 
  [create a new project] 
{% endhighlight %}

Select the hosting option. The CLI will ask which project to select. Either create a new project or select an existing one.

```
? Select a default Firebase project for this directory: (Use arrow keys)
❯ [don't setup a default project] 
  MyProject (myproject) 
  [create a new project] 
```

Create a new project or select a previous project 

```
? What do you want to use as your public directory? public
? Configure as a single-page app (rewrite all urls to /index.html)? No
```



## Follow the firebase deployment commands for travis ci
https://docs.travis-ci.com/user/deployment/firebase/

## Travis-CI setup

### Add Travis build for your Github repository

Setup a Travis CI build for your Github project. If you were using Github
pages this would be `<username>.github.io` where `<username>` is your Github
username. See the getting started docs for Travis CI 
[docs](https://docs.travis-ci.com/user/getting-started/).

### Test a simple build on Travis CI.

Add a file `.travis.yml` to your project in a feature branch. The following
simple build will use a container with Ruby v2.3.1 installed, pull the Github
project branch with new changes, install the dependencies for the project,
then build the Jekyll site:

{% highlight yml %}

language: ruby
rvm:
 - 2.3.1
install:
- bundle install
- gem install jekyll
script:
- bundle exec jekyll build
- ls _site/

{% endhighlight %}

Commit the `.travis.yml` file and push the feature branch to your Github
project. Login to Travis CI and navigate to the main dashboard. You should see
a build starting for your feature branch. After the build completes you should
see the contents of the compiled static site listed in the log.

### setup travis cli
login
`travis login`

enable repo
`travis enable`

create project in Firebase for each environment

login to firebase for each project, generate a separate key for each one
`firebase use devezbcme`
`firebase login:ci`

generate encrypted key
`travis encrypt`

### add conditions for each environment
```
before_install:
  - if [ $TRAVIS_BRANCH = 'develop' ]; TRAVIS_BUILD_ENV="dev"; fi
  - if [ $TRAVIS_BRANCH = 'master' ]; TRAVIS_BUILD_ENV="prod"; fi
```

Can't auth through proxy as of 01/2018
https://github.com/firebase/firebase-tools/issues/155
