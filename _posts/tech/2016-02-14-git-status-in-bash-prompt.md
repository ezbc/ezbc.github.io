---
layout: post
title: Showing Git Status in Bash Prompt
author:
category: tech-project
tags: bash
comments: true
use_math: true
archive: false
example: tech-projects
index-example: tech
excerpt: <div class="/image-4of4-width"> <img src="/images/2016-02-14/example_prompt.png"/> </div> Show the status and branch of your git repo by the color of bash prompt.
---

In this post I demonstrate how to show the status and branch of the current git
repository in the bash prompt. This can be a time-saver for anyone who switches
branches constantly.

{% include toc.md %}

# Examples

First follow the [set up instructions](#set-up) to change the bash prompt. In
the example below I have added a new file `bashprompt.sh` to the repository.
This new file is untracked, so the prompt will be red. Next I add the new file
staged for committing, leading to a yellow prompt. Finally, I commit the new
file. At this point, all files are tracked and committed, so the prompt is
green.

<div class="image-4of4-width">
  <img src="/images/2016-02-14/example_prompt.png"/>
</div>

# Set up

To change the bash prompt we need to define a function which grabs the branch
and status of the git repository of the current directory. You can
[download](https://raw.githubusercontent.com/ezbc/dot_files/7335ac33804cd989eadac6041b325d21e3e6bce2/bashprompt.sh)
the following script from one of my github repos which defines the necessary
function.

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

    export PS1="${state}$__git_branch$__prompt_tail$__last_color "
}

# Tell bash to execute this function just before displaying its prompt.
PROMPT_COMMAND=prompt_command


{% endhighlight %}

Next source the script to change the bash prompt.

{% highlight bash %}

chmod 755 bashprompt.sh
source bashprompt.sh

{% endhighlight %}

If you want to change the prompt, edit the variable defintion for PS1. For
example to include the hostname and username in the prompt:

{% highlight bash %}
    export PS1="\u@\h${state}$__git_branch$__prompt_tail$__last_color "
{% endhighlight %}


