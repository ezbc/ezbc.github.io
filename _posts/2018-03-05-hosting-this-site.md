---
author: Elijah Bernstein-Cooper
category:
- professional
- tech
comments: true
date: 2018-03-05 00:00:00
layout: post
tags:
- jekyll
- firebase
- travis-ci
title: Continuous Integration of this Blog in Firebase 
use_math: false
published: true
image: 
  feature: /media/2018/03/05/next-level.jpg
  credit: Max Pixel
  creditlink: "http://maxpixel.freegreatpicture.com/Stairs-Architecture-Level-Emergence-2904871"
redirect_from:
- /2018/03/04/hosting-this-site
---

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

[Travis-CI](https://travis-ci.org/) is an managed continuous integration
service to build and deploy projects in Github. Travis-CI is *free* for public
projects on Github. The service offers flexible build configurations and
integrates with many popular products for [deployment](https://docs.travis-
ci.com/user/deployment).

I develop this site locally and push changes to Github, Github notifies
Travis- CI, Travis-CI builds this site in a container and deploys to Firebase
to host the static content.

# Getting Started

## Firebase Hosting Setup

### Install Firebase

You will need to install the [Firebase CLI](https://firebase.google.com/docs/hosting/quickstart). The Firebase CLI is a node package easily installed with npm.

### Initialize App

Change directories into your Jekyll project directory. Initialize the Firebase
settings within the project directory with

{% highlight bash %}
firebase init
{% endhighlight %}

The initialization will create a file in the root of current directoy called
`firebase.json`. You may [customize](https://firebase.google.com/docs/hosting/url-redirects-rewrites) the hosting behavior in this file with URL redirects and rewriters.

### Generate Authentication Token for Travis-CI

Travis-CI will need to be able to authenticate with your Firebase app.
Generate an authentication token for your project by using the continuous
integration login feature with Firebase CLI

{% highlight bash %}
firebase login:ci
{% endhighlight %}

When complete an authentication token should be printed to the terminal. Save
the key in a safe and private location for later.

## Travis-CI Deployment Setup

### Add Travis Build for your Github Repository

Setup a Travis-CI build for your Github project. If you were using Github
pages this would be `<username>.github.io` where `<username>` is your Github
username. See the getting started docs for Travis-CI 
[docs](https://docs.travis-ci.com/user/getting-started/).

### Test a Simple Build on Travis-CI.

Add a file `.travis.yml` to your project in a feature branch. The following
simple build will use a container with Ruby v2.3.1 installed, pull the Github
project branch with new changes, install the dependencies for the project,
build the Jekyll site and list the contents of the site.

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
project. Login to Travis-CI and navigate to the main dashboard. You should see
a build starting for your feature branch. After the build completes you should
see the contents of the compiled static site listed in the log.

### Deploy Site to Firebase

#### Install Travis-CI CLI

We will need to use the Travis CLI to encrypt the Firebase authentication
token. Install Travis CLI with ruby by installing the gem

{% highlight bash %}
gem install travis
{% endhighlight %}

Login to the Travis CLI client.

{% highlight bash %}
travis login
{% endhighlight %}

Enable the Github repo with Travis-CI. When a repo is enabled in Travis-CI Github
will push notifications to Travis-CI whenever a change is made to the repo.

{% highlight bash %}
travis enable
{% endhighlight %}

#### Encrypt the Firebase Authentication Token

If you are hosting this repo publically you will need to encrypt the Firebase
authentication token in the Travis-CI build file.

{% highlight bash %}
travis encrypt
{% endhighlight %}

Follow the instructions to encrypt the key from the terminal. When complete
you should see a YML snippet with the encrypted key.

{% highlight yml %}
  secure: "ssvo3M4Th2ULi...
{% endhighlight %}

Use this key in the next step.

#### Add Deployment in Travis-CI Build

Travis-CI has many plugins for deploying to other services including
[Firebase](https://docs.travis-ci.com/user/deployment/firebase/). The
deployment plugins allow for easy configuration of common deployment
scenarios. For example in this blog build I am able to deploy to a Firebase
project only from a build off a specific branch and maintain an encrypted
authentication token for the Firebase API.

After the build step in the `.travis.yml` file add the following:

{% highlight yml %}
deploy:
  provider: firebase
  token:
    secure: "YOUR ENCRYPTED token"
  project: "myproject"
  skip_cleanup: true
  on:
    branch: feature/firebase

{% endhighlight %}

This configuration tells Travis-CI to deploy the contents built in the script
step to Firebase. The `token/secure` should be the encrypted token generated
by the Travis CLI in the previous step. The `project` should be the Firebase
project you wish to host the static files on. `skip_cleanup` instructs Tracis-
CI to leave any generated artifacts alone. The `on/branch` configuration
instructs Travis-CI to only deploy when the build branch is
'feature/firebase'.

The `.travis.yml` file should look like the following:

{% highlight yml %}

language: ruby
rvm:
 - 2.3.1
install:
- bundle install
- gem install jekyll
script:
- bundle exec jekyll build
deploy:
  provider: firebase
  token:
    secure: "YOUR ENCRYPTED token"
  project: "myproject"
  skip_cleanup: true
  on:
    branch: feature/firebase
  	
{% endhighlight %}

Finally you will need to configure which files to deploy to the Firebase
project. Edit the `firebase.json` file to instruct Firebase to deploy the
contents of `_site`, the Jekyll-generated static files.

{% highlight json %}
{
  "hosting": {
    "public": "_site"
  }
}

{% endhighlight %}

## Final Result 

You made a change to your Jekyll site. You committed the change and pushed the
change to your Github project. Github notifies Travis-CI to start a build.
Travis-CI finds the `.travis.yml` file in your repo. Travis-CI spins up a
container with Ruby installed, installs the gems required by your project,
installs Jekyll then runs a Jekyll build. Travis-CI authenticates with
Firebase then deploys the static files built from the `feature/firebase`
branch. Firebase hosts your website effortlessly for you.

# Conclusion

The continuous integration solution with Travis-CI and Firebase used for
hosting gives you greater control over development of your site. Firebase
empowers you to manage multiple environments, extend your static site to a web
application and rewrite URLs in the way you need. Travis-CI allows for full
control of your build and deploy process. This hosting solution will unlock
possibilites for you static blog.