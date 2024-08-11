import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob
import matplotlib.pyplot as plt
from flask import Flask
app = Flask(__name__)
nltk.download('stopwords')
nltk.download('punkt')
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words and word.isalpha()]
    return ' '.join(filtered_text)


@app.route('/analyze_sentiment')
def analyze_sentiment(text):
    # 示例文本
    text = "I am really sad to see you! "
    processed_text = preprocess_text(text)
    print("Processed Text:", processed_text)
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    sentiment_score = analyze_sentiment(processed_text)
    print("Sentiment Score:", sentiment_score)    
    return '123'

# def visualize_sentiment(sentiment_score):
#     plt.bar(['情感'], [sentiment_score], color=['blue'])
#     plt.ylim(-1, 1)
#     plt.ylabel('分数')
#     plt.title('情感识别结果')
#     plt.show()

# visualize_sentiment(sentiment_score)
if __name__ == '__main__':
    app.run(debug=True)