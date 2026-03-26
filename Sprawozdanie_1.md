Sprawozdanie z etapu 1 powinno zawierać analizę danych, które będą przetwarzane przez
sieć neuronową. Dla zastosowań diagnostycznych należy podać listę nazw cech zawartych
w wektorze wejściowym (o ile są dostępne/możliwe do ustalenia), zakres zmienności tych
cech (dodatkowo np. histogramy wartości cech lub podstawowe parametry statystyczne
wartości cech: wartość średnią i odchylenie standardowe; dla zadań typowo
klasyfikacyjnych parametry statystyczne należy określić oddzielnie dla co najmniej dwóch
rozróżnianych klas) oraz proponowany sposób kodowania danych nienumerycznych. W
sprawozdaniu powinna być opisana proponowana metoda wstępnego przetwarzania
danych przed podaniem ich na wejście sieci (uwzględniająca np. normalizację/skalowanie
lub szczegóły postępowania w przypadku danych niekompletnych) oraz proponowany
podział zbioru danych na dane treningowe i testowe o ile nie został on narzucony z góry
(dla tematów projektów z danymi syntetycznymi wystarczające są oczywiście nazwy cech
typu cecha_1, cecha_2 itd.). W sprawozdaniu z etapu 1 powinna być również zawarta
koncepcja realizacji sieci neuronowej – jej struktura z podaniem liczby neuronów w każdej
z warstw, funkcja aktywacji oraz szczegóły algorytmu uczenia.


# Sprawozdanie SNZB cz. 1 - projekt nr. 2 - Diagnostyka cukrzycy za pomocą sieci uczonej z nauczycielem

## Analiza danych do przetworzenia
Na potrzeby wykonania projektu zostały nam dostarczone pliki `pima.te` oraz `pima.tr2`. Pliki te zawieraja dane medyczne dotyczące populacji młodych kobiet z plemienia Indian Pima, zamieszkujących okolice Phoenix w Arizonie. 

### Cechy zawarte w zbiorze
- `npreg` - liczbę ciąż, którą dana kobieta przeszła
- `glu` - stężenie glukozy w osoczu krwi ustalone w czasie doustnego testu obciążenia glukozą
- `bp` - ciśnienie rozkurczowe krwi [mmHg]
- `skin` - grubość fałdu skórnego tricepsa [mm]
- `bmi` - wartość wskaźnika BMI
- `ped` - funkcja predyspozycji genetycznej na cukrzycę
- `age` - wiek
- `type` - czy stwierdzono cukrzycę

Plik `pima.te` zawiera 332 wiersze danych testowych, natomiast `pima.tr2` zawiera 200 kompletnych wierszy i 100 niekompletnych. Pomimo zawarcia w pliku `Readme.txt` informacji o polu `ins`, nie znajduje sie ono ani w `pima.tr2` ani w `pima.te`, co daje nam 7 cech wejściowych. 

### Proponowany sposób kodowania danych nienumerycznych
Kolumna docelowa type zawierająca wartości tekstowe ("Yes" / "No") zostanie przekodowana na wartości binarne. Klasa "No" (brak cukrzycy) otrzyma wartość 0, natomiast klasa "Yes" (cukrzyca) otrzyma wartość 1.

### Proponowany podział zbioru danych
Podział na zbiór treningowy i testowy został narzucony z góry. Plik `pima.tr2` posłuży jako zbiór treningowy, a plik pima.te jako zbiór testowy.

### Przetwarzanie danych niekompletnych
Zbiór zawarty w `pima.tr2` jest niekompletny. Usunięcie niekompletnych wierszy znacząco pomniejszyłoby zbiór treningowy. Proponowanym rozwiązaniem jest zastąpienie brakujących wartości medianą lub średnią wyliczoną dla danej cechy.

### Normalizacja / Skalowanie danych
Ze względu na duże rozbieżności pomiędzy wartościami danych konieczne jest zastosowanie skalowania danych, aby uniknąć dominacji cech o wyższych wartościach nad tymi o niższych. Proponowanym sposobem skalowania jest metoda *Z-score*.

### Koncepcja realizacji sieci neuronowej

Struktura: 
- Warstwa wejściowa: 7 neuronów (odpowiadających 7 cechom wejściowym)
- Warstwa ukryta: 1 warstwa zawierająca 16 neuronów.
- Warstwa wyjściowa: 1 neuron.

Funkcje aktywacji: 
- W warstwie ukrytej - *ReLU* 
- W warstwie wyjściowej - *Sigmoid*

Algorytm uczenia:
- uczenie metoda propagacji wstecznej
- optymalizator - *Adam* lub *SGD*
- funkcja straty - binarna entropia krzyżowa

### Parametry statystyczne dla klasy: Brak cukrzycy (type = No)

| Statystyka | npreg | glu | bp | skin | bmi | ped | age |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Ilość danych** | 194.0 | 194.0 | 189.0 | 134.0 | 192.0 | 194.0 | 194.0 |
| **Średnia** | 3.237 | 113.021 | 70.799 | 27.142 | 30.671 | 0.398 | 31.113 |
| **Odchylenie std.** | 2.934 | 24.896 | 11.391 | 10.859 | 6.547 | 0.264 | 11.370 |
| **Minimum** | 0.0 | 56.0 | 38.0 | 8.0 | 18.2 | 0.078 | 21.0 |
| **1-wszy kwartyl** | 1.0 | 96.0 | 62.0 | 18.0 | 25.4 | 0.224 | 23.0 |
| **Mediana** | 2.0 | 110.5 | 70.0 | 27.0 | 30.3 | 0.301 | 27.0 |
| **3-ci kwartyl** | 5.0 | 127.750 | 78.0 | 34.0 | 35.075 | 0.524 | 36.750 |
| **Maksimum** | 13.0 | 193.0 | 110.0 | 60.0 | 47.9 | 1.698 | 72.0 |

### Parametry statystyczne dla klasy: Cukrzyca (type = Yes)

| Statystyka | npreg | glu | bp | skin | bmi | ped | age |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Ilość danych** | 106.0 | 106.0 | 98.0 | 68.0 | 105.0 | 106.0 | 106.0 |
| **Średnia** | 4.792 | 143.368 | 75.255 | 33.118 | 34.580 | 0.505 | 36.726 |
| **Odchylenie std.** | 3.705 | 28.710 | 11.799 | 12.302 | 5.595 | 0.335 | 11.115 |
| **Minimum** | 0.0 | 80.0 | 40.0 | 7.0 | 22.9 | 0.141 | 21.0 |
| **1-wszy kwartyl** | 1.0 | 124.0 | 68.0 | 26.0 | 30.9 | 0.258 | 28.250 |
| **Mediana** | 4.0 | 141.0 | 74.5 | 32.0 | 34.0 | 0.407 | 34.0 |
| **3-ci kwartyl** | 7.750 | 166.500 | 82.0 | 39.250 | 37.9 | 0.681 | 44.0 |
| **Maksimum** | 14.0 | 199.0 | 114.0 | 99.0 | 52.9 | 2.288 | 62.0 |

