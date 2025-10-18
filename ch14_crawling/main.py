import requests
from bs4 import BeautifulSoup

# 1. url 설정
url = "https://quotes.toscrape.com"

# 2. 웹페이지 요청
response = requests.get(url)
html = response.text

# 3. BeautifulSoup으로 HTML 파싱
soup = BeautifulSoup(html, "html.parser")

# 4. 필요한 부분 선택 (명언과 작가)
# quotes = soup.select(".quote") # css selector로 모든 class="quote"
quotes = soup.find_all("div", class_="quote")
# 리스트로 저장

# 5. 결과 출력
for q in quotes:
    text = q.find("span", class_="text").get_text(strip=True)
    author = q.find("small", class_="author").get_text(strip=True)
    # get_text(strip=True) : HTML 태그 제거 + 양쪽 공백 제거
    print(f"{author} : {text}")

