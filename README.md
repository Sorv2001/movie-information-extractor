# 🎬 Movie Information Extractor

An AI-powered application that extracts structured movie information from unstructured text using Large Language Models (LLMs).

---

## 🚀 Features

- Extracts key movie details from a paragraph:
  - 🎥 Title  
  - 📅 Release Year  
  - 🎭 Genre  
  - 🎬 Director  
  - ⭐ Rating  
  - 👥 Cast  
  - 📝 Summary  

- Clean and interactive UI built with Streamlit  
- Structured JSON output with expandable view  
- Fast and accurate extraction using Mistral AI  

---

## 🛠 Tech Stack

- Python  
- Streamlit  
- LangChain  
- Mistral AI (LLM)  
- Pydantic  

---

## 📸 Demo

Paste a movie paragraph and get structured output instantly.

Example Input:3 Idiots is a critically acclaimed Bollywood comedy-drama film directed by Rajkumar Hirani and released in 2009. The film stars Aamir Khan, R. Madhavan, and Sharman Joshi in lead roles, with Kareena Kapoor and Boman Irani in supporting roles. Set in an engineering college, the story follows three friends as they navigate academic pressure, strict education systems, and their personal dreams. The film explores themes of friendship, innovation, and pursuing passion over societal expectations, making it one of the most loved Indian films.




Example Output:
```json
{
  "title": "3 Idiots",
  "release_year": 2009,
  "genre": ["Comedy", "Drama"],
  "director": "Rajkumar Hirani",
  "cast": ["Aamir Khan", "R. Madhavan", "Sharman Joshi"],
  "rating": 8.4,
  "summary": "A story of three friends navigating college life..."
}