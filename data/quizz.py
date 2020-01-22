import ipywidgets as widgets
import sys
from IPython.display import display
from IPython.display import clear_output

def create_multipleChoice_widget(description, options, correct_answer):
    if correct_answer not in options:
        options.append(correct_answer)
    
    correct_answer_index = options.index(correct_answer)
    
    radio_options = [(words, i) for i, words in enumerate(options)]
    alternativ = widgets.RadioButtons(
        options = radio_options,
        description = '',
        disabled = False
    )
    
    description_out = widgets.Output()
    with description_out:
        print(description)
        
    feedback_out = widgets.Output()

    def check_selection(b):
        a = int(alternativ.value)
        if a==correct_answer_index:
            s = '\x1b[6;30;42m' + "Ok." + '\x1b[0m' +"\n" #green color
        else:
            s = '\x1b[5;30;41m' + "Źle. " + '\x1b[0m' +"\n" #red color
        with feedback_out:
            clear_output()
            print(s)
        return
    
    check = widgets.Button(description="submit")
    check.on_click(check_selection)
    
    
    return widgets.VBox([description_out, alternativ, check, feedback_out])

Q1 = create_multipleChoice_widget(
    """Programy powiązane z blokującymi połączeniami (I/O-bound) spędzają dużo czasu na dokonywaniu obliczeń.""",
    ['Prawda', 'Fałsz'], 'Fałsz')
Q2 = create_multipleChoice_widget(
    'Jaki rodzaj współbieżności jest najlepszy dla programów związanych z CPU',
    ['Asyncio', 'Threading', 'Multiprocessing', 'Dictionaries'], 'Multiprocessing')
Q3 = create_multipleChoice_widget(
    """Jeśli masz program związany z procesorem i zamierzasz korzystać z biblioteki multiprocessing, 
    jaką liczbę procesów najlepiej utworzyć?""",
    ['100', 'Po 1 dla CPU', '1', "Jak najwięcej"], 'Po 1 dla CPU')
Q4 = create_multipleChoice_widget(
    """Jeśli mamy program związany z operacjami I/O, którego uruchomienie zajmuje około 2 sekund 
    i który uruchamia się tylko raz w tygodniu. Z jakiej biblioteki współbieżności należałoby korzystać?""",
    ["Threading", "Asyncio", "Multiprocessing", "Żaden"],
    "Żaden"
)

Q5 = create_multipleChoice_widget(
    """Adding concurrency to your program will always speed it up?""",
    ["Prawda", "Fałsz"],
    "Fałsz"
)

Q6 = create_multipleChoice_widget(
    """Które stwierdzenie najlepiej definiuje „współbieżność”?""",
    [
        'Stworzenie poprawnej strukutury danych dla problemu',
        'Robienie wielu rzeczy jednocześnie',
        'Robienie rzeczy pojedyńczo',
    ],
    "Robienie wielu rzeczy jednocześnie"
)

Q7 = create_multipleChoice_widget(
    """Jak dużo CPU użyje standardowy program asyncio?""",
    ["1", "0", "Tak dużo jak mu wskażemy", "Tyle ile ma komputer", "2"],
    "1"
)
