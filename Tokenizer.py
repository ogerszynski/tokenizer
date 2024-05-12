import re # moduł wyrażeń regularnych - znaki PL!

def Tokenizer(text):
    text_clean = re.sub(r'[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]', '', text) # ususwanie znaków interpunkcyjnych
    
    tokens = text_clean.split() # podział tekstu na wyrazy
    return tokens

def main(): # informacje na powitanie dla usera
    print("Jestem prostym progrmem do tokenizacji")
    print("Dzielę wprowadzony tekst na słowa i zapisuję wynik do pliku .txt.")
    print("Wprowadź tekst (obsługuję polskie znaki! :):")
    
    user_input = input() # wczytanie tesktu
    
    tokens = Tokenizer(user_input) # tokenizacja
    
    with open('Teskt_po_tokenizacji.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(tokens)) # zapis do pliku - dodane kodowanie utf8 do znaków PL
    
    print("tokenizacja wykonana, wyniki zapisano do pliku .txt w folderze programu. Dziękuję!")

if __name__ == "__main__":
    main() #uruchomienie funkcji main jako głównego progrmu
