import tkinter as tk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon (only needed once)
nltk.download('vader_lexicon')


# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Analyze sentiment logic
def analyze_sentiment():
    text = text_input.get("1.0", "end-1c")
    if not text.strip():
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    scores = analyzer.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.05:
        sentiment = "Positive 😊"
        color = "#c8f7c5"
    elif compound <= -0.05:
        sentiment = "Negative 😞"
        color = "#f7c5c5"
    else:
        sentiment = "Neutral 😐"
        color = "#f7f4c5"

    result_box.config(state="normal")
    result_box.delete("1.0", "end")
    result_box.insert("end", f"Sentiment: {sentiment}\nConfidence: {compound:.2f}")
    result_box.config(bg=color, state="disabled")

# GUI setup
app = tk.Tk()
app.title("AI Sentiment Analyzer")
app.geometry("600x400")
app.configure(bg="#f0f0f0")
app.resizable(False, False)

# Widgets
title = tk.Label(app, text="AI-Based Sentiment Analyzer", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title.pack(pady=15)

text_input = tk.Text(app, height=6, width=65, font=("Helvetica", 12))
text_input.pack(padx=20, pady=10)

analyze_btn = tk.Button(app, text="Analyze Sentiment", command=analyze_sentiment,
                        font=("Helvetica", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
analyze_btn.pack(pady=10)

result_box = tk.Text(app, height=4, width=50, font=("Helvetica", 12), state="disabled")
result_box.pack(pady=10)

footer = tk.Label(app, text="Built by Kiran Joshi • MCA Student", font=("Helvetica", 9), bg="#f0f0f0")
footer.pack(pady=5)

# Run GUI
app.mainloop()
