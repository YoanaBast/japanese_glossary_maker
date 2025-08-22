import os
import re
import json

from janome.tokenizer import Tokenizer

class TextTransformer:
    def __init__(self):
        self.current_words = set()
        if os.path.exists("common.json"):
            try:
                with open("common.json", "r", encoding="utf-8") as f:
                    self.common = json.load(f)
            except json.JSONDecodeError:
                self.common = []
        else:
            self.common = []


    @staticmethod
    def refresh_text_file():
        if os.path.exists("db.json"):
            with open("db.json", "r", encoding="utf-8") as f:
                all_words = json.load(f)
        else:
            all_words = []

        with open('result.txt', 'w', encoding="utf-8") as r:
            for word in all_words:
                r.write(f"{word}\n")


    def take_unique_words_from_str(self, text):
        tokenizer = Tokenizer()
        tokens = [token.surface for token in tokenizer.tokenize(text)]
        japanese_words = [w for w in tokens if re.search(r'[\u3040-\u30FF\u4E00-\u9FFF]', w)]

        unique_words = list(filter(
            lambda x: x not in self.common, japanese_words))

        self.current_words.update(unique_words)


    def filter_words(self):
        if os.path.exists("db.json"):
            with open("db.json", "r", encoding="utf-8") as f:
                db_words = set(json.load(f))
        else:
            db_words = set()

        self.current_words -= db_words
        aw = db_words.union(self.current_words)

        return aw


    def add_words_to_db(self):
        all_words = self.filter_words()

        with open('db.json', 'w', encoding='utf-8') as f:
            json.dump(sorted(all_words), f, ensure_ascii=False, indent=2)

        print(f"Saved {len(self.current_words)} words to db.json.")

        self.refresh_text_file()
        self.current_words = set()


    def add_to_common_for_exclusion(self, *args):
        # Add word only if it is not already in the common set
        for word in args:
            if word not in self.common:
                self.common.append(word)
                # Save the updated common set back to JSON
                with open("common.json", "w", encoding="utf-8") as f:
                    json.dump(sorted(self.common), f, ensure_ascii=False, indent=2)
                    print(f"Saved {word} to common.json.")
