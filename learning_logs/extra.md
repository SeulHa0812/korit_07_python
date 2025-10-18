## Crawling 
- 인터넷상의 웹페이지(HTML 문서)에서 원하는 데이터(텍스트, 이미지, 링크 등) 를 자동으로 가져오는 기술

### 크롤링이 동작하는 기본 원리
1. 요청(Request)
- requests 모듈을 사용해 브라우저처럼 웹사이트에 접근
2. 응답(Response)
- 서버가 HTML 문서를 반환
3. 파싱(Parsing)
- HTML은 단순한 텍스트이기 때문에, 구조를 이해하려면 분석해야 함
- BeautifulSoup이나 lxml 같은 라이브러리로 HTML을 구조화해서 필요한 부분만 추출
4. 저장(Save)
- 가져온 데이터를 CSV, JSON, DB 등 원하는 형태로 저장
---
웹 크롤링 (Web Crawling)	인터넷 상의 여러 웹페이지를 자동으로 탐색하며 링크를 따라가 데이터를 수집하는 과정  
웹 스크래핑 (Web Scraping)	하나의 웹페이지(혹은 일부 페이지)에서 원하는 정보만 추출하는 과정
    - 데이터를 찾을 때 beautifulsoup와 같은 라이브러리 활용하고, CSS Selector와 같은 데이터 위치를 표시하는 기법 사용
크롤링은 “웹페이지를 찾으러 다니는 과정”  
스크래핑은 “그 웹페이지에서 데이터를 잘라내는 과정”
---
### robots.txt
- 웹 사이트 소유자가 크롤러에게 제공하는 지침서
- 접근할 수 있는 영역과 접근할 수 없는 영역 명확히 정의
ex.
```txt
User-agent: *   // 모든 크롤러에게 적용
Disallow: /private/
Allow: /public/
Sitemap: https://example.com/sitemap.xml 
```

