# A Commit Message Hook for Datatables

## Example Commit Message

```
Do not do bad thing

Previously we did a bad thing. Now we no longer do that bad thing, thus 
resolving the issue.

DT-1234
```

## Current Checks Performed

* Message includes a summary
* Summary length is <= 50 characters
* Summary does not end in punctuation
* Summary is one line
* Description line length is <= 72 characters
* A Jira ticket is the last part of the message

## Installation

From the root directory of the repo in which you wish to use this:

```bash
$ cd .git/hooks
$ curl -O https://raw.githubusercontent.com/adamhammes-wf/commit-msg/master/commit-msg.py
$ chmod +x commit-msg.py
```

