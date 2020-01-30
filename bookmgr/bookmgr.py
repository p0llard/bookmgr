import os

from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def create_categories(categories):
    for category in categories:
        path = os.path.abspath(category)

        if not os.path.isdir(path) and os.path.exists(path):
            print("Category is a file")

        else:
            os.makedirs(path, exist_ok=True)


def build_name(title, author):
    return "{} — {}".format(author, title)


def build_links(name, path, categories):
    for category in categories:
        cat_path = os.path.abspath(category)
        link_path = os.path.join(cat_path, name)

        try:
            os.symlink(path, link_path)
        except FileExistsError:
            print("Link already present")


def deploy_book(path):
    try:
        index = os.path.join(path, ".index.yaml")
        with open(index, "r") as f:
            card = load(f, Loader=Loader)

            title = card["title"]
            author = card["author"]
            categories = card["categories"]
            name = build_name(title, author)

            create_categories(categories)
            build_links(name, path, categories)

    except TypeError as error:
        print("Failed to parse index card for book")

    except IOError as error:
        print("Failed to find index card for book")
