An intelligent web application that helps users discover the most suitable career options based on their skills, interests, personality traits, and work style. The app uses NLP, vector similarity, and optional GPT-based explanations to recommend career paths — along with course suggestions and visual insights.

🚀 Features
🔍 Personalized Career Matching using TF-IDF + Cosine Similarity

📊 Match Percentage Bar Chart

🎓 Recommended Courses (Coursera / edX) per career

🤖 (Optional) GPT-4 Career Explanations

🧾 Clean UI with Streamlit

🖼️ Demo Screenshot

🛠️ Tech Stack
Python 3.10+

Streamlit

Scikit-learn

Matplotlib

OpenAI GPT-3.5 (optional)

📁 Project Structure

career_path_predictor/
├── app.py                  # Streamlit frontend
├── predictor.py            # AI logic + GPT + data
├── careers.csv       # Dependencies
✅ How to Run
Clone the repo


git clone https://github.com/yourusername/career-path-predictor.git
cd career-path-predictor
Install dependencies


pip install -r requirements.txt
Add your OpenAI API key

Open predictor.py

Replace "your-openai-api-key-here" with your key

python
Copy
Edit
openai.api_key = "sk-xxxxxx"
Launch the app


streamlit run app.py
📚 Sample Input
"I enjoy creative thinking, working independently, and designing user-friendly experiences. I prefer visual tasks and value flexibility."

🔎 Sample Output
UX Designer — 95%

Software Engineer — 82%

Business Analyst — 78%

📌 Future Additions
Export results to PDF

Login system with user history

Public deployment (Streamlit Cloud / Hugging Face Spaces)

Broader career database integration

🙋‍♀️ Author
Rishmitha Kalapureddy
B.Tech, Vignan Institute of Information Technology
