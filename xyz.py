import requests
url = "https://shailshrii2000-commits.github.io/RajSanitary-Rewa/"  # Replace with the website URL
response = requests.get(url)
from bs4 import BeautifulSoup

html_content = response.text  # Get the HTML from the response
soup = BeautifulSoup(html_content, "html.parser")  # Parse the HTML

print(soup.prettify())