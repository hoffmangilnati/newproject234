class UISochen:
    """
    מחלקה המייצגת סוכן UI בסיסי.
    """

    def __init__(self, name="סוכן UI"):
        self.name = name
        self.state = {}

    def render(self, component, props=None):
        """
        שיטת הדמיה/הצגה של קומפוננטה.
        :param component: str - שם הקומפוננטה
        :param props: dict - תכונות של הקומפוננטה
        """
        if props is None:
            props = {}
        print(f"[{self.name}] מציג את הקומפוננטה: {component} עם מאפיינים: {props}")

    def handle_event(self, event_name, callback):
        """
        רישום תגובה לאירוע UI כלשהו.
        :param event_name: str - שם האירוע
        :param callback: function - פונקציית קריאה חזרה לטיפול באירוע
        """
        print(f"[{self.name}] מחובר לאירוע: {event_name}")
        # הדמיית קריאה חזרה
        callback()

    def update_state(self, key, value):
        """
        עדכון סטייט פנימי לסוכן ה-UI.
        """
        self.state[key] = value
        print(f"[{self.name}] עדכן סטייט: {key} = {value}")


# דוגמת שימוש בסיסית:
if __name__ == "__main__":
    ui_agent = UISochen("סוכן ראשי")
    ui_agent.render("כפתור", {"label": "שלח"})
    ui_agent.handle_event("onClick", lambda: print("הכפתור נלחץ!"))
    ui_agent.update_state("clicked", True)