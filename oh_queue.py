#!/usr/bin/env python3

from os import path, makedirs, chmod
from re import compile
from shutil import rmtree
from sys import exit

from html import template


def main(form: str, sheet: str, html_path: str = "~/html/oh"):
    # validate urls:
    form_m = compile(
        r"^(https?:\/\/)?(forms.gle\/|docs.google.com\/forms\/d\/.*)")
    if not form_m.match(form):
        exit("form url is not valid")
    form_url = form_m.sub(r"https://\2", form)
    sheet_m = compile(r"^(https?:\/\/)?(docs.google.com\/spreadsheets\/d\/.*)")
    if not sheet_m.match(sheet):
        exit("sheet url is not valid")
    info = [form_url,
            compile(r"d/([a-zA-Z0-9_-]+)/edit").findall(sheet)[0],
            compile(r"gid=(\d+)").findall(sheet)[0]]
    print(info)
    html_path = path.expanduser(html_path)
    rmtree(html_path, ignore_errors=True)
    makedirs(html_path, exist_ok=True)
    with open(path.join(html_path, "index.html"), "w+") as index:
        index.write(template.format(info[0], info[1], info[2]))
    chmod(path.join(html_path, "index.html"), mode=0o644)
    chmod(path(html_path), mode=0o711)


if __name__ == "__main__":
    while True:
        form_val = input("Google Form URL: ")
        if form_val:
            break
    while True:
        sheet_val = input("Google Sheet URL: ")
        if sheet_val:
            break
    html_val = input("HTML path(optional): ")
    if not html_val:
        html_val = "~/html/oh"
    main(form_val, sheet_val, html_val)
