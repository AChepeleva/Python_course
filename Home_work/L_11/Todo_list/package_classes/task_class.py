class Task:
    def __init__(self, tname, tpriority):
        self.tname = tname
        self.tpriority = tpriority

    def __str__(self):
        return f"name: {self.tname} | priority: {self.tpriority}"
        
