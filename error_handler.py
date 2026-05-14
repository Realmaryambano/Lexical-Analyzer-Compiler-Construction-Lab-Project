class ErrorHandler:
    def __init__(self):
        self.errors = []

    def add_error(self, message, line, column):
        self.errors.append({
            "message": message,
            "line": line,
            "column": column
        })

    def has_errors(self):
        return len(self.errors) > 0

    def get_errors(self):
        return self.errors

    def display(self):
        if not self.errors:
            print("\nNo errors found.")
        else:
            print("\n--- ERROR LOG ---")
            print(f"{'Error':<40} {'Line':<10} {'Column':<10}")
            print("-" * 60)
            for error in self.errors:
                print(f"{error['message']:<40} {error['line']:<10} {error['column']:<10}")
                