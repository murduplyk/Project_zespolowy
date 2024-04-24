# Project zespolowy
___

### Cel projektu:
Głównym celem projektu jest odzwierciedlenie pracy zespołowej i realizacja projektu z podziałem obowiązków. \
Jednym z głównych celów jest praktyka używania narzędzia Git i GitHub (narzędzia kontroli wersji). \
Ten aspekt jest fundamentalny w pracy programisty.
___
### Czym jest aplikacja projektu:
Aplikacja serwer-klient napisana w języku Python do zarządzania kontami użytkowników i transakcjami.

___

### Documentacja projektu:

- **Konfiguracja Serwera**
  - Serwer jest inicjalizowany przy użyciu gniazda TCP na lokalnym hoście `(localhost)` i porcie 50007 `(ADDR = ('localhost', 50007))`.
  - Nasłuchuje on na przychodzące połączenia `(SERVER.listen(0))` i tworzy nowy wątek do obsługi każdego połączenia klienta.

- **Protokół Komunikacyjny**
  - Komunikacja między serwerem a klientami opiera się na wiadomościach zakodowanych w formacie UTF-8 `(FORMAT = 'utf-8')`.
  - Każda wiadomość jest poprzedzona nagłówkiem o długości 5 bajtów, który określa długość wiadomości.

- **Zarządzanie Kontami Użytkowników**
  - Dane kont użytkowników są przechowywane w pliku JSON `(ACCOUNTS_DATA)`.
  - Funkcje takie jak `find_user`, `create_user`, `delete_user` i `change_user_data` służą do zarządzania kontami użytkowników. Funkcje te współdziałają z plikiem JSON, aby wykonywać operacje takie jak tworzenie, usuwanie i modyfikowanie danych użytkowników.

- **Autoryzacja Użytkowników**
  - Autoryzacja użytkowników jest obsługiwana za pomocą funkcji `authorization_user`. Użytkownicy podają swoją nazwę użytkownika i hasło, które są weryfikowane na podstawie przechowywanych danych użytkownika w pliku JSON. 

- **Zarządzanie Transakcjami**
  - Serwer obsługuje różne rodzaje transakcji, w tym:
    - Doładowywanie sald kont `(top_up_balance)`.
    - Wysyłanie pieniędzy do innych użytkowników `(send_money)`.
    - Sprawdzanie sald kont `(check_money)`.
    - Wypłacanie pieniędzy z kont `(withdraw)`.

- **Funkcjonalność Administracyjna**
  - Serwer zawiera proces autoryzacji administratora `(admin_authorization)`, który przyznaje uprawnienia administracyjne.

- **Wielowątkowość**
  - Wielowątkowość jest używana do obsługi wielu połączeń klientów równocześnie, zapewniając, że serwer może obsługiwać kilku klientów jednocześnie bez blokowania.

- **Obsługa Klienta**
  - Funkcja `handle_client` zarządza komunikacją z każdym klientem. Odbiera ona wiadomości od klientów i przekazuje odpowiednie funkcje na podstawie typu wiadomości.

- **Uruchamianie Serwera**
  - Serwer rozpoczyna nasłuchiwanie przychodzących połączeń w nieskończonej pętli (start()).

- **Punkt Wejścia
  - Blok `__name__ == '__main__'` zapewnia, że serwer rozpocznie działanie tylko wtedy, gdy skrypt zostanie wykonany bezpośrednio, a nie gdy zostanie zaimportowany jako moduł.**

