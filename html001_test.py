# Szerző: Englert Ervin Brunó
# Copyright © 2025, Englert Ervin Brunó
# Licenc: CC BY-SA 4.0

import pytest
from bs4 import BeautifulSoup

@pytest.fixture
def html_content():
    with open("index.html", "r", encoding="utf-8") as file:
        return file.read()

def test_html_language(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    assert soup.html.get("lang") == "hu", "Az oldal nyelve nincs magyarra állítva."

def test_title(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    assert soup.title.string == "Szoliman", "A böngészőfül címe nem 'Szoliman'."

def test_main_heading(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    main_heading = soup.find("h1")
    assert main_heading and main_heading.string == "Szoliman", "Az oldal főcíme hibás vagy hiányzik."

def test_section_headings(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    headings = soup.find_all("h2")
    expected_headings = ["A szemrehányás", "A szentkönyv", "A leborulás"]
    assert len(headings) == len(expected_headings), "Nem található megfelelő számú másodszintű fejezetcím."
    for heading, expected in zip(headings, expected_headings):
        assert heading.string == expected, f"A '{expected}' fejezetcím nem megfelelő."

def test_paragraphs(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    paragraphs = soup.find_all("p")
    assert len(paragraphs) == 3, "Nem található három bekezdés."

def test_emphasized_text(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    em_text = soup.find("em")
    assert em_text and em_text.string == "tekintete azalatt", "A dőlt szöveg hibás vagy hiányzik az első bekezdésben."

def test_strong_text(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    strong_texts = soup.find_all("strong")
    expected_text = "A szultán"
    assert len(strong_texts) == 2, "Nem található két kiemelt 'A szultán' szöveg a harmadik bekezdésben."
    for strong in strong_texts:
        assert strong.string == expected_text, "A kiemelt 'A szultán' szöveg hibás."

def test_comment_presence(html_content):
    assert "<!-- Vizsgafeladat -->" in html_content, "A megjegyzés nem található a forráskódban."
