# Python Multi-tool
This project contains two main parts currently, a Web Scraper and an AI Chatbot, each with its own distinct functionality.

# Web Scraper
The Web Scraper is a tool designed to scrape different types of data from websites. The user is prompted to enter a website URL, after which they can choose the type of data they wish to scrape from the website. The options are:

**Links**: Extracts and prints all hyperlink references on the page.

**Images**: Finds all image source URLs on the page and prints them.

**SVGs**: Extracts and prints all SVG (scalable vector graphics) elements on the page.

**Metadata**: Extracts and prints all metadata from the page.

**Text**: Extracts and prints all textual content from the page, including paragraph text and headers.

**Scripts**: Extracts and prints all JavaScript embedded or linked on the page.

**Styles**: Extracts and prints all CSS styles embedded or linked on the page.

**Download Images**: Downloads all images from the page and saves them locally.

After each scraping operation, the user can choose to scrape another website or exit the program.

# AI Chatbot
The AI Chatbot uses OpenAI's GPT-3.5-turbo model to generate human-like text responses. After setting the OpenAI API key and model engine, the user can choose to:

**Chat**: The user can enter a prompt, and the AI will generate a response.

**Translate**: The user can enter a piece of text and specify a target language, and the AI will translate the text into the target language.

**Summarize**: The user can enter a long piece of text, and the AI will provide a summarized version of it.
The user can continue interacting with the AI or choose to exit the program.

# Overall 
This program provides a useful interface for web scraping tasks and AI-powered conversation or text processing. It requires the **requests**, **beautifulsoup4**, and **openai** Python libraries.

Please note that for the AI Chatbot, ***you'll need to provide your own OpenAI API key***, and usage of the AI model may incur costs according to OpenAI's pricing policy.
