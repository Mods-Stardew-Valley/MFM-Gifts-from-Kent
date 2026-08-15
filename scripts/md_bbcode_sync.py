#!/usr/bin/env python3
"""
md_bbcode_sync.py

Converte entre Markdown e BBCode nos dois sentidos.

Uso manual:
    python md_bbcode_sync.py to-bbcode README.md -o README.bbcode
    python md_bbcode_sync.py to-md README.bbcode -o README.md

Uso em CI (decide sozinho qual lado converter, comparando timestamps):
    python md_bbcode_sync.py sync README.md README.bbcode
"""

import argparse
import os
import re


# ---------- Markdown -> BBCode ----------

def convert_code_blocks_md2bb(text):
    def repl(match):
        return f"[code]{match.group(2)}[/code]"
    return re.sub(r"```(\w*)\n(.*?)```", repl, text, flags=re.DOTALL)


def convert_inline_code_md2bb(text):
    return re.sub(r"`([^`\n]+)`", r"[code]\1[/code]", text)


def convert_headers_md2bb(text):
    def repl(match):
        level = len(match.group(1))
        content = match.group(2).strip()
        sizes = {1: 20, 2: 17, 3: 15, 4: 12, 5: 11, 6: 10}
        return f"[size={sizes.get(level, 100)}][b]{content}[/b][/size]"
    return re.sub(r"^(#{1,6})\s+(.*)$", repl, text, flags=re.MULTILINE)


def convert_bold_italic_md2bb(text):
    text = re.sub(r"\*\*\*(.+?)\*\*\*", r"[b][i]\1[/i][/b]", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"[b]\1[/b]", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"[i]\1[/i]", text)
    text = re.sub(r"(?<!_)_(?!_)(.+?)(?<!_)_(?!_)", r"[i]\1[/i]", text)
    return text


def convert_strikethrough_md2bb(text):
    return re.sub(r"~~(.+?)~~", r"[s]\1[/s]", text)


def convert_images_md2bb(text):
    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r"[img]\2[/img]", text)


def convert_links_md2bb(text):
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"[url=\2]\1[/url]", text)


def convert_lists_md2bb(text):
    lines = text.split("\n")
    output = []
    in_list = False
    for line in lines:
        match = re.match(r"^(\s*)[-*]\s+(.*)$", line)
        if match:
            if not in_list:
                output.append("[list]")
                in_list = True
            output.append(f"[*]{match.group(2)}")
        else:
            if in_list:
                output.append("[/list]")
                in_list = False
            output.append(line)
    if in_list:
        output.append("[/list]")
    return "\n".join(output)


def convert_blockquotes_md2bb(text):
    return re.sub(r"^>\s?(.*)$", r"[quote]\1[/quote]", text, flags=re.MULTILINE)


def convert_hr_md2bb(text):
    return re.sub(r"^(-{3,}|\*{3,})$", "[hr]", text, flags=re.MULTILINE)


def markdown_to_bbcode(text):
    text = convert_code_blocks_md2bb(text)
    text = convert_hr_md2bb(text)
    text = convert_headers_md2bb(text)
    text = convert_images_md2bb(text)
    text = convert_links_md2bb(text)
    text = convert_bold_italic_md2bb(text)
    text = convert_strikethrough_md2bb(text)
    text = convert_inline_code_md2bb(text)
    text = convert_lists_md2bb(text)
    text = convert_blockquotes_md2bb(text)
    return text


# ---------- BBCode -> Markdown ----------

def convert_code_blocks_bb2md(text):
    return re.sub(
        r"\[code\](.*?)\[/code\]",
        lambda m: f"```\n{m.group(1)}\n```" if "\n" in m.group(1) else f"`{m.group(1)}`",
        text,
        flags=re.DOTALL,
    )


def convert_headers_bb2md(text):
    def repl(match):
        size = int(match.group(1))
        content = match.group(2)
        content = re.sub(r"\[/?b\]", "", content)
        level_map = [(200, 1), (175, 2), (150, 3), (125, 4), (110, 5), (100, 6)]
        level = next((lvl for sz, lvl in level_map if size >= sz), 6)
        return f"{'#' * level} {content.strip()}"
    return re.sub(r"\[size=(\d+)\]\[b\](.*?)\[/b\]\[/size\]", repl, text, flags=re.DOTALL)


def convert_bold_italic_bb2md(text):
    text = re.sub(r"\[b\]\[i\](.+?)\[/i\]\[/b\]", r"***\1***", text)
    text = re.sub(r"\[b\](.+?)\[/b\]", r"**\1**", text)
    text = re.sub(r"\[i\](.+?)\[/i\]", r"*\1*", text)
    return text


def convert_strikethrough_bb2md(text):
    return re.sub(r"\[s\](.+?)\[/s\]", r"~~\1~~", text)


def convert_images_bb2md(text):
    return re.sub(r"\[img\](.+?)\[/img\]", r"![](\1)", text)


def convert_links_bb2md(text):
    return re.sub(r"\[url=([^\]]+)\](.+?)\[/url\]", r"[\2](\1)", text)


def convert_lists_bb2md(text):
    text = re.sub(r"\[list\]\n?", "", text)
    text = re.sub(r"\[/list\]\n?", "", text)
    text = re.sub(r"\[\*\](.*)", r"- \1", text)
    return text


def convert_blockquotes_bb2md(text):
    return re.sub(r"\[quote\](.*?)\[/quote\]", r"> \1", text, flags=re.DOTALL)


def convert_hr_bb2md(text):
    return re.sub(r"^\[hr\]$", "---", text, flags=re.MULTILINE)


def bbcode_to_markdown(text):
    text = convert_code_blocks_bb2md(text)
    text = convert_hr_bb2md(text)
    text = convert_headers_bb2md(text)
    text = convert_images_bb2md(text)
    text = convert_links_bb2md(text)
    text = convert_bold_italic_bb2md(text)
    text = convert_strikethrough_bb2md(text)
    text = convert_lists_bb2md(text)
    text = convert_blockquotes_bb2md(text)
    return text


# ---------- CLI ----------

def do_to_bbcode(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()
    result = markdown_to_bbcode(content)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)
    print(f"Convertido: {input_path} -> {output_path}")


def do_to_md(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()
    result = bbcode_to_markdown(content)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)
    print(f"Convertido: {input_path} -> {output_path}")


def do_sync(md_path, bb_path):
    """Compara timestamps e converte do arquivo mais recente para o outro."""
    md_exists = os.path.exists(md_path)
    bb_exists = os.path.exists(bb_path)

    if md_exists and not bb_exists:
        do_to_bbcode(md_path, bb_path)
        return
    if bb_exists and not md_exists:
        do_to_md(bb_path, md_path)
        return
    if not md_exists and not bb_exists:
        raise SystemExit("Nenhum dos dois arquivos existe.")

    md_time = os.path.getmtime(md_path)
    bb_time = os.path.getmtime(bb_path)

    if md_time > bb_time:
        do_to_bbcode(md_path, bb_path)
    elif bb_time > md_time:
        do_to_md(bb_path, md_path)
    else:
        print("Arquivos com mesmo timestamp, nada a fazer.")


def main():
    parser = argparse.ArgumentParser(description="Sincroniza Markdown e BBCode nos dois sentidos.")
    sub = parser.add_subparsers(dest="command", required=True)

    p1 = sub.add_parser("to-bbcode", help="Converte Markdown -> BBCode")
    p1.add_argument("input")
    p1.add_argument("-o", "--output", required=True)

    p2 = sub.add_parser("to-md", help="Converte BBCode -> Markdown")
    p2.add_argument("input")
    p2.add_argument("-o", "--output", required=True)

    p3 = sub.add_parser("sync", help="Detecta qual mudou por ultimo e converte para o outro")
    p3.add_argument("md_path")
    p3.add_argument("bb_path")

    args = parser.parse_args()

    if args.command == "to-bbcode":
        do_to_bbcode(args.input, args.output)
    elif args.command == "to-md":
        do_to_md(args.input, args.output)
    elif args.command == "sync":
        do_sync(args.md_path, args.bb_path)


if __name__ == "__main__":
    main()