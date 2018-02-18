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
---

Ready to take your Jekyll site to the next level from Github pages? This post takes you to the next level where you have complete control over your deployment process and hosting.

<!-- more -->

# Setup Firebase 

(Install Firebase CLI)[https://firebase.google.com/docs/cli/]

Login to firebase to get auth key for non-interactive.
`firebase login:ci`

# Follow the firebase deployment commands for travis ci
https://docs.travis-ci.com/user/deployment/firebase/

## setup travis cli
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

# add conditions for each environment
```
before_install:
  - if [ $TRAVIS_BRANCH = 'develop' ]; TRAVIS_BUILD_ENV="dev"; fi
  - if [ $TRAVIS_BRANCH = 'master' ]; TRAVIS_BUILD_ENV="prod"; fi
```

Can't auth through proxy as of 01/2018
https://github.com/firebase/firebase-tools/issues/155


