def beyond_compare(self):
    mode = self.compare_file.get()
    self.action(f"Beyond Compare ({mode})")