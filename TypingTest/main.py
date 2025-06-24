import tkinter as tk
from tkinter import messagebox
import time

root = tk.Tk()
root.title("Typing Test")
sentence = ['Although some people might advocate for typing out', 'random words or short phrases, there are certain sentences', 'that are particularly good for typing practice.', 'One such sentence is "The quick brown fox jumps', 'over the lazy dog." This sentence uses every letter', 'of the alphabet, making it a great way to warm up your fingers', 'before embarking on a long typing session.', 'Including a variety of sentences to practice typing, such as this one,', 'will provide a comprehensive foundation for your typing skills.']
cut_sentence = ['Although', 'some', 'people', 'might', 'advocate', 'for', 'typing', 'out', 'random', 'words', 'or', 'short', 'phrases,', 'there', 'are', 'certain', 'sentences', 'that', 'are', 'particularly', 'good', 'for', 'typing', 'practice.', 'One', 'such', 'sentence', 'is', '"The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog."', 'This', 'sentence', 'uses', 'every', 'letter', 'of', 'the', 'alphabet,', 'making', 'it', 'a', 'great', 'way', 'to', 'warm', 'up', 'your', 'fingers', 'before', 'embarking', 'on', 'a', 'long', 'typing', 'session.', 'Including', 'a', 'variety', 'of', 'sentences', 'to', 'practice', 'typing,', 'such', 'as', 'this', 'one,', 'will', 'provide', 'a', 'comprehensive', 'foundation', 'for', 'your', 'typing', 'skills.']
i = 0

def start_timer(event):
    global start_time
    start_time = time.time()
    root.unbind("<space>")

def next_line(event):
    global i
    i += 1
    if i < len(sentence):
        l1.config(text=sentence[i])

    else:
        l1.config(text="Typing complete!")
        l1.config(state=tk.DISABLED)
        text = t1.get("1.0", "end-1c").split("\n")
        words = []
        for line in text:
            words += line.split(" ")


        end_time = time.time()
        elapsed_time = end_time - start_time
        words_per_minute = len(cut_sentence) / (elapsed_time / 60)


        accuracy = 0
        for x in range(len(words)):
            if words[x] in cut_sentence:
                accuracy += 1

        messagebox.showinfo("Your stats", f"Your time is: {elapsed_time:.2f}sec.\nWPM: {words_per_minute:.0f}\nYour accuracy is: {(accuracy / len(cut_sentence)) * 100:.0f}%")



root.bind("<Return>", next_line)
root.bind("<space>", start_timer)

l1 = tk.Label(root, text=sentence[i])
l1.pack(ipadx=100, ipady=50)

t1 = tk.Text(root, height=2, width=30)
t1.pack(ipadx=100, pady=30)




root.mainloop()