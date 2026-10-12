from mcp.server import MCPServer
from pathlib import Path

mcp = MCPServer("LocalNotes")

BASE_DIR = Path(__file__).resolve().parent

filename = BASE_DIR / "notes.txt"

@mcp.tool()
def add_note_to_file(content: str) -> str:
    """
    Appends the given content to the user's local notes.
    """
    

    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(content + "\n")

        return f"Content appended to {filename}."

    except Exception as e:
        return f"Error appending to file {filename}: {e}"


@mcp.tool()
def read_notes() -> str:
    """
    Reads and returns the contents of the user's local notes.
    """

    try:
        with open(filename, "r", encoding="utf-8") as f:
            notes = f.read()

        return notes if notes else "No notes found."

    except FileNotFoundError:
        return "No notes file found."

    except Exception as e:
        return f"Error reading file {filename}: {e}"


if __name__ == "__main__":
    mcp.run()