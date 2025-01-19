import pytest
from bs4 import BeautifulSoup

@pytest.fixture
def html_content():
    with open("/Users/englertervin/Documents/GitHub/html001/szoliman.html", "r", encoding="utf-8") as file:
        return file.read()

def test_title(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    assert soup.title.string == "Szoliman"

def test_language(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    assert soup.html['lang'] == "hu"

def test_headings(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    h1 = soup.find('h1')
    assert h1.string == "Szoliman"
    
    h2 = soup.find_all('h2')
    assert len(h2) == 3
    assert h2[0].string == "A szemrehányás"
    assert h2[1].string == "A szentkönyv"
    assert h2[2].string == "A leborulás"

def test_italic_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    italic_text = soup.find('i')
    assert italic_text.string == "tekintete azalatt"

def test_strong_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    strong_texts = soup.find_all('strong')
    assert len(strong_texts) == 2
    assert strong_texts[0].string == "A szultán"
    assert strong_texts[1].string == "A szultán"

if __name__ == "__main__":
    pytest.main()