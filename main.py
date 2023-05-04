import requests
import json
import tkinter as tk

HEIGHT = 400
WIDTH = 800

def get_channel_subscriber_count(id):
    url = f'https://api.superplaycounts.repl.co/api/youtube-channel-counter/user/{id}'
    response = requests.get(url)
    data = json.loads(response.text)
    subscriber_count = data['statistics'][0]['counts'][0]['count']
    channel_name = data['statistics'][0]['user'][0]['count']
    return subscriber_count, channel_name

def search_channel_id(channel_name):
    url = f'https://api.superplaycounts.repl.co/api/youtube-channel-counter/search/{channel_name}'
    response = requests.get(url)
    data = json.loads(response.text)
    channel_id = data['list'][0][2]
    return channel_id

def get_subscriber_count():
    channel_name = channel_name_entry.get()
    channel_id = search_channel_id(channel_name)
    subscriber_count, channel_name = get_channel_subscriber_count(channel_id)
    channel_name_label['text'] = "{}".format(channel_name)
    subscriber_count_label['text'] = "{:,} subscribers".format(subscriber_count)
    root.after(5000, get_subscriber_count)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("YT Channel Sub Count Phyton")
canvas.pack()

frame = tk.Frame(root, bg='#80C1FF')
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.2, anchor='n')

channel_name_entry = tk.Entry(frame, font=('Courier', 18))
channel_name_entry.place(relx=0.05, rely=0.1, relwidth=0.6, relheight=0.8)

go_button = tk.Button(frame, text='Go', font=('Courier', 18), command=get_subscriber_count)
go_button.place(relx=0.7, rely=0.1, relwidth=0.25, relheight=0.8)

subscriber_count_label = tk.Label(root, font=('Courier', 48))
subscriber_count_label.pack()

channel_name_label = tk.Label(root, font=('Courier', 24))
channel_name_label.pack()

root.mainloop()
get_subscriber_count()
