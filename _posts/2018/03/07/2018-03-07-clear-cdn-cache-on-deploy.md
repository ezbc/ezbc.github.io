---
author: Elijah Bernstein-Cooper
category:
- professional
- tech
comments: true
date: 2018-03-07 00:00:00
layout: post
tags:
- jekyll
- cloudflare
- travis-ci
title: Clearing Cloudflare CDN Cache After Deploy
use_math: false
published: true
image: 
  feature: /media/2018/03/07/world-map.svg
  credit: wooptoo, via Wikimedia Commons
  creditlink: "https://commons.wikimedia.org/wiki/File%3AWorld-map.svg"
---

Learn how to make updates to your site immediate when using a content delivery
network. This post walks you through steps to reduce your time to live with
Cloudflare.

<!--more-->

# Cloudflare Caching

Cloudflare's content delivery network (CDN) is a powerful service to decrease
the latency of user requests across the globe. Cloudflare hosts dozens of data
centers around the world to cache website assets. Most users are a just a few
hops away from one of Cloudflare's servers.

A CDN can delay updates to a website, however while the CDN is updating the
cache the long time-to-live (TTL) can be frustrating. One way to reduce the
TTL is to clear the Cloudflare cache. Clearing the Cloudflare cache will
require user requests to retrieve assets from the updated host origin.

Cloudflare supports clearing your site's cache in three ways:

  1. Purge individual files in the cache
  1. Purge all files in the cache
  1. Cache-Tags for granular control

Purging individual files or all files in the cache are features available to
free accounts while purging by Cache-Tags is an enterprise feature.

The simplest way to ensure immediate updates is to purge all files in the
cache. Purging all cached files will likely increase user requests to your
host origin. This post outlines how to clear all files in the cache, while a
more tactical solution would be to clear only the files necessary to push an
update.

# Clearing the Cloudflare Cache on Deploy

## Clearing Cache with the Cloudflare API

Cloudflare provides an [API](https://api.cloudflare.com/#zone-purge-all-files) to easily delete your website's zone cache. A request using curl to purge all files looks like the following:

{% highlight bash %}
curl -X DELETE "https://api.cloudflare.com/client/v4/zones/$ZONE/purge_cache" \
     -H "X-Auth-Email: $AUTH_EMAIL" \
     -H "X-Auth-Key: $AUTH_KEY" \
     -H "Content-Type: application/json" \
     --data '{"purge_everything":true}'
{% endhighlight %}

where `$ZONE` is the zone ID of your site, `$AUTH_EMAIL` is the email for the
account hosting the site and `$AUTH_KEY` is the API authentication key for
your user. 

## Adding Cache Clearing to Post-Deploy Step in Build

This post uses 

Clear cache [script](https://github.com/ezbc/ezbc.github.io/blob/a477321fbc9a252cd1b76bc2a50851a23eaf6927/scripts/clearcache.sh).



