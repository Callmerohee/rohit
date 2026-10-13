def build_project(self):
    mode = self.compare_file.get()
    self.action(f"Build Project ({mode})")
