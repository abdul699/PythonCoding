import requests
import json

def dictionary(url):
    # get the content of url
    response = requests.get(url)

    # format the response to JSON style
    result = json.loads(response.text)

    # if the word isn't in dictionary then print the error title and message. Used title as a search key because title is not a key if response is 200(OK)
    if "title" in result:
        print(result["title"] + ". " + result["message"])
    else:
        #printint the word, partOfSpeech and definition
        print("Output: " + result[0]["word"] + ". " + result[0]["meanings"][0]["partOfSpeech"] + ". " + result[0]["meanings"][0]["definitions"][0]["definition"])


def main():
    # taking input word
    title = input("Word ? ")

    # Given api url + the input title
    url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"+title

    dictionary(url)

if __name__ == "__main__":     
    main()