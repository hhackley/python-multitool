import requests
from bs4 import BeautifulSoup
import openai

def scrape_links(soup):
    links = soup.find_all("a")
    for link in links:
        print(link.get("href"))

def scrape_images(soup):
    images = soup.find_all("img")
    for image in images:
        print(image.get("src"))

def scrape_svgs(soup):
    svgs = soup.find_all("svg")
    for svg in svgs:
        print(svg)
        
def scrape_metadata(soup):
    metadata = soup.find_all('meta')
    for meta in metadata:
        print(meta.attrs)

def scrape_text(soup):
    text_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li'])
    for element in text_elements:
        print(element.get_text())
        
def scrape_scripts(soup):
    scripts = soup.find_all("script")
    for script in scripts:
        print(script)

def scrape_styles(soup):
    styles = soup.find_all("style")
    for style in styles:
        print(style)

def download_images(soup):
    images = soup.find_all("img")
    for i, image in enumerate(images):
        url = image.get("src")
        response = requests.get(url)
        with open(f'image{i}.jpg', 'wb') as f:
            f.write(response.content)



def web_scraper():
    while True:
        print("-- Please enter a website URL to scrape:  --")
        url = input()
        
        # Send a GET request to the website
        response = requests.get(url)

        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        print("-- What would you like to scrape? (links, images, download images, svgs, metadata, text, scripts, styles) --")
        choice = input()

        if choice == "links":
            scrape_links(soup)
        elif choice == "images":
            scrape_images(soup)
        elif choice == "svgs":
            scrape_svgs(soup)
        elif choice == "metadata":
            scrape_metadata(soup)
        elif choice == "text":
            scrape_text(soup)
        elif choice == "scripts":
            scrape_scripts(soup)
        elif choice == "styles":
            scrape_styles(soup) 
        elif choice == "download images":
            download_images(soup)   
        else:
            print("\n-- Invalid choice. Please enter 'links', 'images', or 'svgs'. --")

        print("\n-- Would you like to scrape another website? (yes, no) --")
        repeat = input()
        if repeat.lower() != "yes":
            break

def chat_with_ai():
    openai.api_key = 'Enter your API key here'
    model_engine = "gpt-3.5-turbo" 

    while True:
        print("-- What would you like to do? (chat, translate, summarize, exit) --")
        action = input().lower()

        if action == 'chat':
            while True:
                print("-- Please enter a prompt: --")
                prompt = input()
                response = openai.ChatCompletion.create(
                    model=model_engine,
                    messages=[
                        {"role": "user", "content": prompt},
                    ])

                message = response.choices[0]['message']
                print("\nResponse: {}".format(message['content']))
                
                print("\n-- Would you like to ask another question? (y/n) --")
                if input().lower() != "y":
                    break

        elif action == 'translate':
            print("-- Please enter the you want to translate to another language: --")
            text = input()
            print("-- Please enter the language you want to translate you text to: --")
            target_language = input()
            response = openai.ChatCompletion.create(
                model=model_engine,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Translate the following English text to {target_language}: {text}"},
                ])

            message = response.choices[0]['message']
            print("\nTranslation: {}\n".format(message['content']))

        elif action == 'summarize':
            print("-- Please enter a long piece of text to summarize: --")
            text = input()
            response = openai.ChatCompletion.create(
                model=model_engine,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Summarize the following text: {text}"},
                ])

            message = response.choices[0]['message']
            print("\nSummary: {}".format(message['content']))

        elif action == 'exit':
            print("\n-- Thank you for using our AI assistant! --\n")
            break

        else:
            print("-- Invalid action. Please enter 'chat', 'translate', 'summarize', or 'exit'. --")

    
while True:
    print("-- What would you like to do? (scrape, ai-tools, exit) --")
    action = input().lower()

    if action == 'scrape':
        web_scraper()
    elif action == 'ai-tools':
        chat_with_ai()
    elif action == 'exit':
        print("-- Thank you for using my program! --")
        break
    else:
        print("-- Invalid action. Please enter 'scrape', 'chat', or 'exit'. --")
