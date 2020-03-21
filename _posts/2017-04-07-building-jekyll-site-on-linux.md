---
author: Elijah Bernstein-Cooper
category:
- professional
- tech
comments: true
date: 2017-04-07 00:00:00
excerpt: Outlines steps to build this site locally on Fedora with Jekyll.
layout: post
tags:
- bash
title: Building this blog locally
use_math: true
image:
  feature: /media/2017/04/07/hammer.png
  credit: Wikipedia
  creditlink: https://commons.wikimedia.org/wiki/File:Hammer_-_Noun_project_1306.svg
  width: 50%
redirect_from:
- /tech-project/2017/04/07/building-this-site
- /2017/04/06/building-this-site
---

# Install Packages

Jekyll runs on ruby. Get the ruby development library:

{% highlight bash %}

  sudo dnf install ruby-devel

{% endhighlight %}

Make sure you have the C compiler:

{% highlight bash %}

  sudo dnf group install "C Development Tools and Libraries"

{% endhighlight %}

Ensure that your Fedora image contains the redhat-rpm-config package 
necessary for your gcc compiler:

{% highlight bash %}

  sudo dnf install redhat-rpm-config

{% endhighlight %}

# Install Gems

Clone the repository

{% highlight bash %}

  git clone git@github.com:ezbc/ezbc.github.io.git

{% endhighlight %}

Install jekyll and bundler gems

{% highlight bash %}

  gem install jekyll bundler

{% endhighlight %}

Change directories to the site project and install the site gems with:

{% highlight bash %}

  cd ezbc.github.io
  bundle install

{% endhighlight %}

Make sure the following line is in _config.yaml so that the installed
dependencies from bundle are ignored while building the site:

{% highlight yaml %}

  exclude [env]

{% endhighlight %}

Now serve the site locally at default port 4000:

{% highlight bash %}

  bundle exec jekyll serve 

{% endhighlight %}

Hopefully you will see the site at
(http://localhost:4000)[http://localhost:4000]