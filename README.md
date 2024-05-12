# Tokenizer
Prosty tokenizer w Pythonie dzielący tekst na słowa.

Opis implementacji
Implementacja programu polega na prostym dzieleniu podanego przez użytkownika tekstu na słowa. W tym celu używamy modułu wyrażeń regularnych żeby usunąć niechciane  znaki interpunkcyjne, pozostawiając litery, w tym te polskie, z „ogonkami”.. Tekst jest dzielony na słowa przy pomocy spacji. Wynik zapisuje się do pliku .txt (z kodowaniem UTF-8, dla poprawnego zapisania polskich znaków).
Wybór metody
Najprościej mówiąc, metoda została wybrana ze względu na jej prostotę, ale zarazem uniwersalne działanie. Wyrażenia regularne + kodowanie UTF-8 pozwala programowi Tokenizer na pracę z różnymi językami i OS, przez co jest prostym ale wszechstronnym narzędziem.
Trudności
Zasadniczo opisane powyżej – żeby obsłużyć różne znaki interpunkcyjne musiałem zastosować moduł re, opcja z iterowaniem przez każdy znak byłaby nieefektywna i skomplikowana w przypadku tekstów z różnorodnymi znakami. 
Aby natomiast zapewnić poprawność przetwarzania polskich znaków trzeba było użyć kodowania UTF-8 przy zapisie wyników do pliku .txt.

