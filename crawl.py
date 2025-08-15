import requests
from bs4 import BeautifulSoup
import urllib.parse

def crawl_url(url):
    try:
        # Send HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all text content
        text_content = soup.get_text(separator='\n', strip=True)
        
        # Extract all links
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            # Convert relative URLs to absolute
            absolute_url = urllib.parse.urljoin(url, href)
            links.append(absolute_url)
        
        return {
            'url': url,
            'text_content': text_content,
            'links': links,
            'html': response.text
        }
    
    except requests.RequestException as e:
        return {'error': f'Failed to crawl {url}: {str(e)}'}

def main():
    # Example usage
    target_url = input("Enter the URL to crawl: ")
    result = crawl_url(target_url)
    
    if 'error' in result:
        print(result['error'])
        return
    
    print(f"\nCrawled URL: {result['url']}")
    print("\nExtracted Text Content:")
    print("-" * 50)
    print(result['text_content'])
    print("\nFound Links:")
    print("-" * 50)
    for link in result['links']:
        print(link)
    
    # Optionally save HTML content to file
    with open('crawled_page.html', 'w', encoding='utf-8') as f:
        f.write(result['html'])

if __name__ == "__main__":
    main()