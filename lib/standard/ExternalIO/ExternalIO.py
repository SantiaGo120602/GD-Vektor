from typing import ByteString

class ExternalIOBuilder:
    def __init__(self):
        self.name = 1

    def readText(self, path: str) -> str:
        with open(path, 'r') as f:
            texto = f.read().replace("\n","") 
            return texto

    def writeText(self, path: str, content: str) -> None:
        with open(path, 'w') as f:
            f.write(content)

    def readBinary(self, path: str) -> ByteString:
        with open(path, 'rb') as f:
            return f.read()

    def writeBinary(self, path: str, content: str) -> None:
        content = bytes(content, 'utf-8')
        with open(path, "wb") as f:
            f.write(content.encode())

ExternalIO = ExternalIOBuilder()