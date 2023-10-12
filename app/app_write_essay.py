from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from time import time

start_second = 0


def spent_time():
    global start_second
    if start_second == 0:
        start_second = time()
    time_second = int(time()) - int(start_second)
    hour = time_second // 3600
    minute = (time_second % 3600) // 60
    second = time_second % 60
    label_time_spent.config(text=f'Spent time:{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}')
    if int(label_written_words['text'][-1]) < int(get_task().get('min_words')):
        label_time_spent.after(200, lambda: spent_time())


def get_task() -> dict:
    return {
        'min_words': int(entry_min_words.get()),
        'max_words': int(entry_max_words.get()),
        'sentence_len': int(entry_sentence_len.get()),
    }


def count_items(value: str, sep='!.?\n\r') -> int:
    previous, current = '', ''
    counter = 0
    for item in value:
        if previous.isalnum() and current in sep:
            counter += 1
        previous = current
        current = item
    return counter


def update_status():
    text_content = text.get('1.0', 'end-1c')
    amount_word = count_items(value=text_content, sep=' !.?\n\r') + 1 if text_content else 0
    amount_sentence = count_items(text_content) + 1 if text_content else 0

    label_written_words.config(text=f'Written words: {amount_word}')
    label_written_sentences.config(text=f'Written sentences: {amount_sentence}')

    paragraphs = text_content.split('\n')
    sentence_start = count_items(paragraphs[0]) + 1 if paragraphs[0] else 0
    sentences_main = count_items('.'.join(paragraphs[1:-1])) + 1 if len(paragraphs) > 1 else 0
    sentence_end = count_items(paragraphs[-1]) + 1 if len(paragraphs) > 2 else 0

    label_written_sentence_start.config(text=f'Written start sentences: {sentence_start}')
    label_written_sentence_main.config(text=f'Written main sentences: {sentences_main}')
    label_written_sentence_end.config(text=f'Written end sentences: {sentence_end}')
    update_result()


def update_result():
    status = ['Result: Less...', 'Result: Ready!', 'Result: Much...']
    min_words = get_task().get('min_words')
    current_words = int(label_written_words['text'].split(':')[1].strip())
    if current_words <= min_words * 0.25:
        label_result.config(text=status[0])
    elif min_words * 0.25 < current_words <= min_words * 0.5:
        label_result.config(text=status[1])
    elif current_words >= min_words:
        label_result.config(text=status[2])


def set_task_sentences():
    min_sentences = int(get_task().get('min_words')) // int(get_task().get('sentence_len'))
    max_sentences = int(get_task().get('max_words')) // int(get_task().get('sentence_len'))

    amount_sentence = f'{int(min_sentences * 0.25)} - {int(max_sentences * 0.25)}'
    amount_main_sentence = f'{int(min_sentences * 0.5)} - {int(max_sentences * 0.5)}'

    label_sentence_start.config(text=f'Number of start sentences: {amount_sentence}')
    label_sentence_main.config(text=f'Number of main sentences: {amount_main_sentence}')
    label_sentence_end.config(text=f'Number of end sentences: {amount_sentence}')


def check_fields(second=0) -> bool:
    global start_second
    if entry_sentence_len.get().isdigit() and entry_max_words.get().isdigit() and entry_min_words.get().isdigit():
        start_second = second
        return True
    else:
        messagebox.showerror('Message error title', 'Enter integer positive numbers in fields')
        return False


root = Tk()
root.title('Literary note')

text = Text(wrap=WORD, width=30)
text.pack(side=LEFT, expand=1, fill=BOTH)
scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)

frame_right = Frame()
frame_right.pack(side=LEFT, fill=Y)

frame_task = LabelFrame(frame_right, text='Task:')
frame_task.pack(fill=X)

Label(frame_task, text='Min words:').pack()
entry_min_words = Entry(frame_task, justify=RIGHT)
entry_min_words.pack(fill=X)

Label(frame_task, text='Max words:').pack()
entry_max_words = Entry(frame_task, justify=RIGHT)
entry_max_words.pack(fill=X)

Label(frame_task, text='Number of words in a sentence:').pack()
entry_sentence_len = Entry(frame_task, justify=RIGHT)
entry_sentence_len.pack(fill=X)

label_sentence_start = Label(frame_task, text="Number of start sentences: 0")
label_sentence_start.pack(fill=X)
label_sentence_main = Label(frame_task, text="Number of main sentences: 0")
label_sentence_main.pack(fill=X)
label_sentence_end = Label(frame_task, text="Number of end sentences: 0")
label_sentence_end.pack(fill=X)

frame_status = LabelFrame(frame_right, text='Status:')
frame_status.pack(fill=X)
label_written_words = Label(frame_status, text='Written words: 0')
label_written_words.pack(fill=X)
label_written_sentences = Label(frame_status, text='Written sentences: 0')
label_written_sentences.pack(fill=X)

label_written_sentence_start = Label(frame_status, text="Written start sentences: 0")
label_written_sentence_start.pack(fill=X)
label_written_sentence_main = Label(frame_status, text="Written main sentences: 0")
label_written_sentence_main.pack(fill=X)
label_written_sentence_end = Label(frame_status, text="Written end sentences: 0")
label_written_sentence_end.pack(fill=X)

frame_result = LabelFrame(frame_right, text='Result:')
frame_result.pack(fill=X)
label_time_spent = Label(frame_result, text='Spent time: 00:00:00')
label_time_spent.pack(fill=X)
label_result = Label(frame_result, text="Result: Start...")
label_result.pack(fill=X)

entry_sentence_len.bind('<Return>', lambda event: set_task_sentences() if check_fields() else None)
text.bind('<Button-1>', lambda event: spent_time() if check_fields(start_second) else None)
text.bind('<Key>', lambda event: update_status() if check_fields(start_second) else None)
# text.bind('<Key>', lambda event: update_result() if check_fields(start_second) else None)

root.mainloop()
