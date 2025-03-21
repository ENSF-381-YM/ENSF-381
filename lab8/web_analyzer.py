import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt

def main():
    url = "https://en.wikipedia.org/wiki/University_of_Calgary"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensures the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')
        print(f"Successfully fetched content from {url}")
    except Exception as e:
        print(f"Error fetching content: {e}")
        return
    
    headings = soup.find_all(re.compile('^h[1-6]$'))
    num_headings = len(headings)
    
    links = soup.find_all('a')
    num_links = len(links)
    
    paragraphs = soup.find_all('p')
    num_paragraphs = len(paragraphs)
    
    print(f"Number of headings (h1 to h6): {num_headings}")
    print(f"Number of links (<a> tags): {num_links}")
    print(f"Number of paragraphs (<p> tags): {num_paragraphs}")

    keyword = str(input("Keyword: "))
    keyword_count = len(re.findall(keyword, response.text, re.IGNORECASE))
    print(f"Keyword '{keyword}' appears {keyword_count} times in the content")

    pagetext = soup.get_text()
    words = [word.lower() for word in pagetext.split() if len(word) > 0]

    freq = 0
    res = ""

    for i in range(0, len(words)):
        count = 0
        for j in range(i + 1, len(words)):
            if words[j] == words[i]:
                count += 1

        if count >= freq:
            res = words[i]
            freq = count

    print("The word that occurs most is: " + str(res))
    print("No of times: " + str(freq))


    labels = ['Headings', 'Links', 'Paragraphs']
    values = [num_headings, num_links, num_paragraphs]
    plt.bar(labels, values)
    plt.title('Group 43')
    plt.ylabel('Count')
    plt.show()

if __name__ == "__main__":
    main()
