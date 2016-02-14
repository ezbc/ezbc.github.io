---
layout: post
title: Showing Git Status in Bash Prompt
author:
category: tech-projects
tags: bash, git
comments: true
use_math: true
archive: false
example: tech-projects 
index-example: data-science 
excerpt: <div class="/image-4of4-width"> <img src="images/2016-02-14/example_prompt.png/></div> Show the status and branch of your git repo by the color of bash prompt.
---

{% include toc.md %}

# Examples

<div class="image-4of4-width">
  <img src="/images/2016-02-14/example_prompt.png"/>
</div>

# Set up

You can
[download](https://raw.githubusercontent.com/ezbc/dot_files/7335ac33804cd989eadac6041b325d21e3e6bce2/bashprompt.sh)
the following script from one of my github repos.

{% highlight bash %}

  prompt_command () {
    # Capture the output of the "git status" command.
    git_status="$(git status 2> /dev/null)"
    local __git_branch='`git branch 2> /dev/null | grep -e ^* | sed -E  s/^\\\\\*\ \(.+\)$/\(\\\\\1\)\ /`'
    local __prompt_tail="\[\033[35m\]$"
    local __last_color="\[\033[00m\]"

    # Set color based on clean/staged/dirty.
    if [[ ${git_status} =~ "working directory clean" ]]; then
        state="${GREEN}"
    elif [[ ${git_status} =~ "Changes to be committed" ]]; then
        state="${YELLOW}"
    else
        state="${RED}"
    fi

    export PS1="${state}$__git_branch$__prompt_tail$__last_color $"
  }

  # Tell bash to execute this function just before displaying its prompt.
  PROMPT_COMMAND=prompt_command_laptop

{% endhighlight %}



{% highlight bash %}

chmod 755 bashprompt.sh
source bashprompt.sh

{% endhighlight %}











