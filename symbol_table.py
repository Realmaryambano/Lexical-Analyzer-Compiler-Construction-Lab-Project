class SymbolTable:
    def __init__(self):
        self.table = {}

    def add(self, name, line):
        if name not in self.table:
            self.table[name] = {"line": line, "references": 1}
        else:
            self.table[name]["references"] += 1

    def get_table(self):
        return self.table

    def display(self):
        print("\n--- SYMBOL TABLE ---")
        print(f"{'Name':<20} {'First Line':<15} {'References':<10}")
        print("-" * 45)
        for name, info in self.table.items():
            print(f"{name:<20} {info['line']:<15} {info['references']:<10}")