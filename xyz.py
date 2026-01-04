import requests
url = "https://rk-creater-ctrl.github.io/CodeNexus/index.html"  # Replace with the website URL
response = requests.get(url)
from bs4 import BeautifulSoup

html_content = response.text  # Get the HTML from the response
soup = BeautifulSoup(html_content, "html.parser")  # Parse the HTML

print(soup.prettify())