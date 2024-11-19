import json
import os
import pickle
import sys


def decipher_phrase(phrase, lexicon_filename, abc_filename):
    print(f'Starting deciphering using {lexicon_filename} and {abc_filename}')
    words = phrase.split(" ")
    if words[0] == '' and len(words) == 1:
        return {"status": 2, "orig_phrase": '', "K": -1}

    # Check if files exist
    if not os.path.exists(lexicon_filename):
        print(f"Error: File '{lexicon_filename}' does not exist.")
        sys.exit(1)
    if not os.path.exists(abc_filename):
        print(f"Error: File '{abc_filename}' does not exist.")
        sys.exit(1)

    try:
        with open(lexicon_filename, 'rb') as lex_file:
            lexicon = set(pickle.load(lex_file))
        with open(abc_filename, 'r', encoding='utf-8') as abc_file:
            alphabet = abc_file.read().replace("\n", "").strip()
            result_list = [0] * 26

            def decipher_char(c, k):
                if c not in alphabet:
                    return c  # Non-alphabet characters remain unchanged
                index = (alphabet.index(c) - k) % len(alphabet)
                return alphabet[index]

            for k in range(26):
                temp_sentence = ""
                for i in range(len(words)):
                    temp_str = ""
                    for j in range(len(words[i])):
                        temp_str += decipher_char(words[i][j], k)
                    temp_sentence += " " + temp_str
                    if temp_str in lexicon:
                        print(temp_str)
                        result_list[k] += 1
                if result_list[k] == len(words):
                    return {"status": 0, "orig_phrase": temp_sentence.strip(), "K": k}
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    return {"status": 1, "orig_phrase": '', "K": -1}


students = {'id1': '209342278', 'id2': '207748518'}

if __name__ == '__main__':
    with open('config-decipher.json', 'r') as json_file:
        config = json.load(json_file)

    # note that lexicon.pkl is a serialized list of 10,000 most common English words
    result = decipher_phrase(config['secret_phrase'],
                             config['lexicon_filename'],
                             config['abc_filename'])

    assert result["status"] in {0, 1, 2}

    if result["status"] == 0:
        print(f'deciphered phrase: {result["orig_phrase"]}, K: {result["K"]}')
    elif result["status"] == 1:
        print("cannot decipher the phrase!")
    else:  # result["status"] == 2:
        print("empty phrase")