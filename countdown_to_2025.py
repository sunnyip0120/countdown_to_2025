import tkinter as tk
from datetime import datetime, timedelta

class CountdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown to New Year")

        self.target_date = datetime(2025, 1, 1)
        self.update_interval = 1000  # milliseconds

        self.label = tk.Label(self.root, text="Countdown to New Year", font=("Arial", 24))
        self.label.pack(pady=20)

        self.countdown_frame = tk.Frame(self.root)
        self.countdown_frame.pack()

        self.parts = {
            "days": {"text": ["days", "day"], "dots": 30},
            "hours": {"text": ["hours", "hour"], "dots": 24},
            "minutes": {"text": ["minutes", "minute"], "dots": 60},
            "seconds": {"text": ["seconds", "second"], "dots": 60},
        }

        self.create_countdown_parts()

        self.update_countdown()

    def create_countdown_parts(self):
        for key, value in self.parts.items():
            part_frame = tk.Frame(self.countdown_frame)
            part_frame.pack()

            remaining_label = tk.Label(part_frame, text="", font=("Arial", 24))
            remaining_label.pack()

            text_label = tk.Label(part_frame, text="", font=("Arial", 14))
            text_label.pack()

            dot_frame = tk.Frame(part_frame)
            dot_frame.pack()

            dots = []
            for _ in range(value["dots"]):
                dot = tk.Label(dot_frame, bg="#0a0a0a", width=3, height=3)
                dot.pack(side=tk.LEFT, padx=2)
                dots.append(dot)

            self.parts[key]["remaining_label"] = remaining_label
            self.parts[key]["text_label"] = text_label
            self.parts[key]["dots"] = dots

    def update_countdown(self):
        now = datetime.now()
        remaining = (self.target_date - now).total_seconds()

        if remaining > 0:
            days = int(remaining // 86400)
            hours = int((remaining % 86400) // 3600)
            minutes = int((remaining % 3600) // 60)
            seconds = int(remaining % 60)

            for key, value in self.parts.items():
                if key == "days":
                    value["remaining_label"].config(text=str(days))
                    value["text_label"].config(text=value["text"][0] if days == 1 else value["text"][1])
                    for dot, idx in zip(value["dots"], range(len(value["dots"]))):
                        dot.config(bg="#00e0ff" if idx < days else "#0a0a0a")
                        dot.config(bg="#ff0000" if idx == days - 1 else dot["bg"])
                elif key == "hours":
                    value["remaining_label"].config(text=str(hours))
                    value["text_label"].config(text=value["text"][0] if hours == 1 else value["text"][1])
                    for dot, idx in zip(value["dots"], range(len(value["dots"]))):
                        dot.config(bg="#00e0ff" if idx < hours else "#0a0a0a")
                        dot.config(bg="#ff0000" if idx == hours - 1 else dot["bg"])
                elif key == "minutes":
                    value["remaining_label"].config(text=str(minutes))
                    value["text_label"].config(text=value["text"][0] if minutes == 1 else value["text"][1])
                    for dot, idx in zip(value["dots"], range(len(value["dots"]))):
                        dot.config(bg="#00e0ff" if idx < minutes else "#0a0a0a")
                        dot.config(bg="#ff0000" if idx == minutes - 1 else dot["bg"])
                elif key == "seconds":
                    value["remaining_label"].config(text=str(seconds))
                    value["text_label"].config(text=value["text"][0] if seconds == 1 else value["text"][1])
                    for dot, idx in zip(value["dots"], range(len(value["dots"]))):
                        dot.config(bg="#00e0ff" if idx < seconds else "#0a0a0a")
                        dot.config(bg="#ff0000" if idx == seconds - 1 else dot["bg"])

            self.root.after(self.update_interval, self.update_countdown)
        else:
            for key, value in self.parts.items():
                value["remaining_label"].config(text="00")
                value["text_label"].config(text="")
                for dot in value["dots"]:
                    dot.config(bg="#0a0a0a")

def main():
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
