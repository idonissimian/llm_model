# מייבא את המודולים הנדרשים לעבודה עם Flask, OpenAI והגדרת סביבה
from flask import Flask, request, render_template  # Flask - ניהול השרת והדפים, request - קריאת בקשות, render_template - להציג דפים
import openai  # ספריית OpenAI לשימוש במודלים כמו GPT-4
from dotenv import load_dotenv  # טעינת משתני סביבה מקובץ .env
import os  # מודול עזר לעבודה עם קבצים ומסלולים

# טוען את המידע מקובץ ה-.env (כדי שנוכל לגשת למפתח API בצורה בטוחה)
load_dotenv()  # טוען את קובץ ה-.env כך שמידע כמו המפתח יהיה נגיש בסביבה

# מקבל את המפתח מתוך קובץ ה-.env
openai.api_key = os.getenv('OPENAI_API_KEY')  # שולף את המפתח מהסביבה ומגדיר את מפתח ה-API של OpenAI

# יצירת האפליקציה של Flask
app = Flask(__name__)  # יוצר את האפליקציה של Flask

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

# Route שמציג את דף הבית של האפליקציה
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":  # אם זה בקשת POST (כלומר, הוצגה שאלה)
        question = request.form["question"]  # שולפים את השאלה מהטופס
        answer = get_answer(question)  # מקבלים את התשובה לשאלה
        return render_template("index.html", question=question, answer=answer)  # מחזירים את התשובה לדף ה-HTML
    return render_template("index.html", question=None, answer=None)  # אם זו בקשה GET, לא מציגים שאלה או תשובה

# הפעלת השרת
if __name__ == "__main__":  # אם זה קובץ הראשי (כלומר הפעלת הסקריפט ישירות)
    app.run(debug=True)  # מריץ את האפליקציה ב-mode debug (מה שמאפשר לדפדף ולראות שגיאות בזמן אמת)
