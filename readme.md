##Auto Reader.

Parses any text and pipes pipes it into say with alternating voices.

###Utility:
- Hack on it to cure boredom.
- Have your macbook read you a bed time story.
- Practice your regular expressions.
    - (hint: there's always a shorter way to do what you've spent
      an hour trying to do)
- Start a speech to text company or something /s

###Usage:

**Quick start**:

0. Use OSX and have at least two voices installed.
1. clone this repository && cd into it.
2. ```cat AliceInWonderland/chapter1.txt | ./narrator.py```
3. (optional) Fall asleep as Siri and that other guy read to you

**Cloud Enabled (R) (beta)**

```curl http://www.gutenberg.org/files/11/11.txt | ./narrator.py```

- It is a known issue that it actually finished parsing the while file and then start reading it
- It *might* be something to do with a certain file buffer size changing say's behavior
- yeah

**Generate you own audio books (alpha)***
0. submit a PR / wait for me to do this in a week.
1. add a -f flag and a file to the say subprocess call

**Command line options**

- ```help``` :: display Usage
- ```
