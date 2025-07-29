import os

class FileData:
    def __init__(self, file_path):
        self.full_path = file_path
        self.name = os.path.basename(file_path)
        self.extension = os.path.splitext(file_path)[1]
        self.size = os.path.getsize(file_path) if os.path.exists(file_path) else 0
        self.source_code = self._read_source_code()
    
    def _read_source_code(self):
        try:
            if os.path.exists(self.full_path) and os.path.isfile(self.full_path):
                with open(self.full_path, 'r', encoding='utf-8') as file:
                    return file.read()
            else:
                return ""
        except (UnicodeDecodeError, PermissionError, IOError):
            return ""
