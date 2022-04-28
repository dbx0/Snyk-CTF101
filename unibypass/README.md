# UniBypass

If you wanna be my parser, you gotta get with my friend.

## Objective

The objective of this challenge is to exploit JSON Parsing to retrieve the flag.

## Exploring the challenge

The website and the API is pretty simple, you can send a value and the API will return you with either a message like `"computer says no"` or `"it's not that simple"` when prompted with the value `flag` as `file_name`. 

By breaking the JSON you can see some details about the app, like the lib used to parse the content.

## Solution

To my surprise, I was able to solve this challenge pretty quickly by exploiting key collisions using character truncation. 
In my case, just by adding a character like `\ud888` at the end of the `file_name` value I was able to bypass the block that was not allowing the API to return the flag.

Payload used:
```json
{
	"file_name": "flag\ud888"
}

```