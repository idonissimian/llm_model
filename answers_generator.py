import openai

openai.api_key = 'YOUR_API_KEY'  # הכנס את המפתח שלך כאן

def get_answer(question):
    # נוודא שהשאלה ממוקדת ל-Python או ל-Machine Learning
    if "python" in question.lower():
        prompt = f"Please answer this Python-related question in detail: {question}"
    elif "machine learning" in question.lower() or "ml" in question.lower():
        prompt = f"Please answer this Machine Learning-related question in detail: {question}"
    else:
        prompt = f"Please answer this technical question in detail: {question}"

    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=200,
        temperature=0.5  # שליטה על יצירת התשובה
    )
    return response.choices[0].text.strip()

# דוגמת שאלות
questions = [
    "מה זה list comprehension ב-Python?",
    "מה זה overfitting ב-Machine Learning?",
    "מה ההבדל בין tuple ל-list ב-Python?",
    "מה זה cross-validation ב-Machine Learning?"
]

for question in questions:
    answer = get_answer(question)
    print(f"Question: {question}\nAnswer: {answer}\n")