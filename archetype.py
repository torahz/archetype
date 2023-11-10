import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    stop_words = set(stopwords.words('portuguese'))
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return ' '.join(filtered_tokens)

def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def train_bot(file_path):
    data = load_data(file_path)

    while True:
        user_input = input("Você: ")
        preprocessed_input = preprocess_text(user_input)

        if preprocessed_input.lower() == 'sair':
            print("Até logo!")
            break

        found = False
        for entry in data:
          if preprocessed_input in entry['question']:
                found = True  
                print("Bot:", entry['answer'])
                break

        if not found:
            print("Bot: Desculpe, eu não entendi. Por favor, escolha uma opção:")
            for i, entry in enumerate(data, 1):
                print(f"{i}. {entry['question']}")

            while True:
                try:
                    choice = int(input("Escolha o número correspondente à sua pergunta: "))
                    if 1 <= choice <= len(data):
                        print("Bot:", data[choice - 1]['answer'])
                        break
                    else:
                        print("Escolha um número válido.")
                except ValueError:
                    print("Por favor, insira um número válido.")

        feedback = input("A resposta foi útil? (Sim/Não): ").lower()
        if feedback == 'não':
            new_entry = {'question': preprocessed_input, 'answer': input("Por favor, forneça a resposta adequada: ")}
            data.append(new_entry)
            save_data(file_path, data)

if __name__ == "__main__":
    file_path = "training_data.json"
    train_bot(file_path)
