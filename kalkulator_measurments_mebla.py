import re
import tkinter as tk
from tkinter import messagebox
def show_message():
    messagebox.showinfo("INSTRUKCJA", "Wprowadzając dane musisz pamiętać by były rozdzielone jakim kolwiek znakiem lub spacją."
    "\n\nWartości nie mogą do siebie przylegać bez separacji.\nPrzykład 23,5-10-20 lub 23,5 10 20 lub W 95 X D 36.75 X H 33\n"
    "\nMożesz skopiować krotkę z ML lub wiersz z Ticket'u i wkleić go bezpośrednio tutaj."
    "\n\nDla pewności sprawdź kolejność wartości Width-Depth-Height.")
# Głowna funkcja programu
def calculate_dimensions():
    # Definiujemy ustawienia pola input
    string = input_field.get("1.0", "end-1c")

    # Prewencyjnie zamieniamy wszystkie "," na "." by uniknąć rozdzielenia liczby zmiennoprzecinkowej
    string = string.replace(",", ".")

    # Funkcja .split tworzy nam lsite rozdzielaną według " " - jeśli nie uda się rozdzielić zrobi to re.findall poniżej.
    string_values = string.split(" ")

    # W wyrażeniu regularnym \d+(?:\.\d+)? wyciągamy liczby z lub bez ułamków, więc otrzymujemy tylko ciąg znaków zawierających liczby oraz liczby zmienno przecinkowe
    # re.findall powoduje również stworzenie listy. Natomiast my tworzymy ją poprzez .split powyżej.
    string_values = re.findall(r'\d+(?:\.\d+)?', string)

    # Tworzymy liste w której przechowamy wartości w Typie Float, robi to za pomocą pętli for by dodać kolejne indexy listy
    float_values = []
    for value in string_values:
        float_values.append(float(value))

    # Przypisujemy do zmiennych odpowiedni indexy z listy float_values w kolejności 0 -> Width 1 -> Depth 2 -> Height i mnożymy przez stałą 2,54 by otrzymać wynik w CM
    width = float_values[0] * 2.54
    depth = float_values[1] * 2.54
    height = float_values[2] * 2.54

    # Formatujemy sposób wyświetlania wyniku.
    result = "Width: {:.3f} cm\nDepth: {:.3f} cm\nHeight: {:.3f} cm".format(width, depth, height)

    # Ustawiamy config pola wyniku najpierw normal by wpisać tam wynik.
    result_field.configure(state="normal")
    result_field.delete("1.0", tk.END)
    result_field.insert(tk.END, result)

    # Następnie blokujemy pole by przypadkowo nie zmienić wartości podanego przez program wyniku
    result_field.configure(state="disabled")

# Ustawiamy root dla top_lvl widget
root = tk.Tk()
# Tytuł okna
root.title("Kalkulator Measurments Mebla")
# Wymiary okna
root.geometry("400x250")

# Ustawiamy Label dla input'a  +  Pakujemy widget do widgeta rodzica
input_label = tk.Label(root, text="PODAJ WYMIARY W KOLEJNOŚCI WIDTH - DEPTH - HEIGHT")
input_label.pack()

# Ustawiamy Text field dla wyniku by móc go skopiować  +  pakujemy widget do widgeta rodzica
input_field = tk.Text(root, height=3, width=30)
input_field.pack()

# Tworzymy przycisk który wywołuje nam wcześniej zdefiniowaną funkcje calculate_dimensions
calculate_button = tk.Button(root, text="Przelicz", command=calculate_dimensions)
calculate_button.pack()

# Ustawiamy Label dla tekstu "Wynik:"  +  Pakujemy widget do widgeta rodzica
result_label = tk.Label(root, text="Wynik:")
result_label.pack()

# Ustawiamy Text field dla wyniku by móc go skopiować  +  pakujemy widget do widgeta rodzica
result_field = tk.Text(root, height=3, width=30)
result_field.configure(state="disabled")
result_field.pack()


button = tk.Button(root, text="INSTRUKCJA", command=show_message)
button.pack()


# Odtwarzamy okno apliakcji
root.mainloop()
