def write_txt_file(file_path: str, content: str):
    """
    Write a string into a .txt file (overwrites if exists).
    Args:
        file_path (str): Destination path.
        content (str): Text to write.
    Returns:
        str: Path to the written file.
    """
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return file_path
tool_schema={
    "type": "function",
    "function": {
        "name": "write_txt_file",
        "description": "Write text content to a .txt file. Overwrites if file already exists.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Full path for the .txt file (e.g. 'notes.txt' or '/tmp/info.txt')."
                },
                "content": {
                    "type": "string",
                    "description": "The text content to write into the file."
                }
            },
            "required": ["file_path", "content"]
        }
    }
}