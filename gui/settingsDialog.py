import tkinter as tk


class SettingsDialog():

    def __init__(self, root, settings) -> None:
        self.settings = settings
        self.root = root

    def showSettings(self):
        self.pop = tk.Toplevel(self.root)
        self.mainUrl = tk.Entry(self.pop)
        self.username = tk.Entry(self.pop)
        self.password = tk.Entry(self.pop)
        self.pop.title("Einstellungen")
        self.pop.geometry("400x550")
        self.pop.config(bg="white")
        # Create a Label Text
        label = tk.Label(self.pop, text="Zugangsdaten",
                         font=('Aerial', 12), background="white")
        label.pack(pady=20, padx=20, anchor="w")

        mainUrlLabel = tk.Label(
            self.pop, text="Studip-Instanz:", background="white")
        self.mainUrl.insert(0, self.settings.getMainUrl())
        mainUrlLabel.pack(pady=5, padx=20, anchor="w")
        self.mainUrl.pack(pady=0, padx=20, anchor="w")

        usernameLabel = tk.Label(
            self.pop, text="Benutzername:", background="white")
        self.username.insert(0, self.settings.getUsername())
        usernameLabel.pack(pady=5, padx=20, anchor="w")
        self.username.pack(pady=0, padx=20, anchor="w")

        passwordLabel = tk.Label(
            self.pop, text="Passwort:", background="white")
        self.password = tk.Entry(self.pop)
        self.password.insert(0, self.settings.getPassword())
        passwordLabel.pack(pady=5, padx=20, anchor="w")
        self.password.pack(pady=0, padx=20, anchor="w")

        save = tk.Button(self.pop, text="Speichern", command=self.saveSettings)
        save.pack(pady=20, padx=20, anchor="w")

    def saveSettings(self):
        self.settings.setPassword(self.password.get())
        self.settings.setUsername(self.username.get())
        self.settings.setMainUrl(self.mainUrl.get())
        self.pop.destroy()
        self.pop.update()
