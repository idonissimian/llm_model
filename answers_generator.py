import openai

openai.api_key = 'YOUR_API_KEY'  # הכנס את המפתח שלך כאן

# פונקציה שמקבלת שאלה ומחזירה תשובה על פי GPT-4
def get_answer(question):
    # נוודא שהשאלה ממוקדת ל-Python או ל-Machine Learning
    if "python" in question.lower():  # אם השאלה קשורה ל-Python
        prompt = f"Please answer this Python-related question in detail: {question}"
    elif "machine learning" in question.lower() or "ml" in question.lower():  # אם השאלה קשורה ל-Machine Learning
        prompt = f"Please answer this Machine Learning-related question in detail: {question}"
    else:  # אם השאלה לא קשורה ישירות לשניים, תשובה טכנית כללית
        prompt = f"Please answer this technical question in detail: {question}"

    # שולח את השאלה ל-API של OpenAI כדי לקבל תשובה
    response = openai.Completion.create(
        model="gpt-4",  # בוחר במודל GPT-4
        prompt=prompt,  # השאלה שהכנסנו
        max_tokens=200,  # הגבלת מספר המילים בתשובה
        temperature=0.5  # הגדרת רמת היצירתיות (0.5 היא רמת אמצע)
    )

    # מחזיר את התשובה שהתקבלה מהמודל
    return response.choices[0].text.strip()  # לוקח את התשובה ומנקה רווחים מיותרים

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
