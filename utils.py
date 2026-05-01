def format_header(text, indent_before=False):
    msg = f"-----## {text} ##-----"

    if indent_before:
        msg = f"\n{msg}"

    return msg

