Este necesar pentru folosirea proiectului sa instalati librariile necesare folosind urmatoarea comanda : pip install -r requirements.txt .
Comanda de rulare este urmatoarea : behave -f html -o raportName.html -- tags=tagName .
Numele tag-ului il puteti gasi deasupra scenariuli pe care vreti sa il testati , de exemplu : @test22


Structura Proiectului
features/: Conține scenariile de testare definite în fișiere .
steps/: Conține implementările pașilor de testare.
pages/: Conține clasele pentru paginile web (LoginPage, InventoryPage, CartPage, CheckoutPage).
browser.py: Inițializează și configurează WebDriver-ul.
environment.py: Setează și curăță contextul de testare.

Funcționalități Testate
Coș de Cumpărături: Verificarea butoanelor "Continue Shopping" și "Checkout".
Checkout: Verificarea butonului "Cancel", mesajelor de eroare și finalizarea checkout-ului.
Inventar: Navigarea între produse, afișarea meniului de setări și adăugarea produselor în coș.
Autentificare: Verificarea autentificării și a mesajelor de eroare.


Limbaj Folosit
Proiectul este scris în Python, un limbaj de programare puternic și flexibil, folosit adesea pentru automatizarea testării datorită sintaxei sale clare și a bibliotecilor disponibile, cum ar fi Selenium pentru interacțiunea cu browserul și Behave pentru testarea BDD (Behavior Driven Development).
