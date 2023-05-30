import tkinter as tk
from tkinter import ttk
import requests

def get_games_owned(steam_id, api_key):
    url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={steam_id}&format=json&include_appinfo=1"
    response = requests.get(url)
    data = response.json()
    games_owned = []
    for game in data["response"]["games"]:
        game_info = {
            "name": game["name"],
            "app_id": game["appid"]
        }
        games_owned.append(game_info)
    return games_owned

def save_games_owned():
    api_key = api_key_entry.get()
    steam_id = steam_id_entry.get()

    games_owned = get_games_owned(steam_id, api_key)

    game_list.delete(0, tk.END)  # Clear previous game list

    for game in games_owned:
        game_list.insert(tk.END, f"{game['name']} (App ID: {game['app_id']})")

    total_games_label.config(text=f"Total Games Owned: {len(games_owned)}")
    result_label.config(text="List of games displayed below.")

# Create the main window
window = tk.Tk()
window.title("Steam Games Owned")
window.geometry("400x400")

# API Key label and entry
api_key_label = tk.Label(window, text="API Key:")
api_key_label.pack()
api_key_entry = tk.Entry(window)
api_key_entry.pack()

# Steam ID label and entry
steam_id_label = tk.Label(window, text="Steam ID:")
steam_id_label.pack()
steam_id_entry = tk.Entry(window)
steam_id_entry.pack()

# Save button
save_button = tk.Button(window, text="List Games", command=save_games_owned)
save_button.pack()

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

# Total games label
total_games_label = tk.Label(window, text="Total Games Owned: 0")
total_games_label.pack()

# Game list
game_list_label = tk.Label(window, text="Games Owned:")
game_list_label.pack()

# Create a scrolled listbox widget
game_list_frame = ttk.Frame(window)
game_list_frame.pack(fill=tk.BOTH, expand=True)

game_list = tk.Listbox(game_list_frame)
game_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add scrollbar to the listbox
scrollbar = ttk.Scrollbar(game_list_frame, orient=tk.VERTICAL, command=game_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
game_list.configure(yscrollcommand=scrollbar.set)

# Connect the scrollbar to the listbox
game_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=game_list.yview)

# Start the GUI event loop
window.mainloop()
