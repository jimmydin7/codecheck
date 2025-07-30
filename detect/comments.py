# will load human & ai datasets from datasets/comments to make first detection
# then it will go through functions to detect em-dash patterns and more 
# point system -> final outcome

import re

def separate_comments_from_code(source, language):
    comment_syntax = {
        "python": {
            "single": [r"#"],
            "multi": [(r'"""', r'"""'), (r"'''", r"'''")]
        },
        "javascript": {
            "single": [r"//"],
            "multi": [(r"/\*", r"\*/")]
        },
        "java": {
            "single": [r"//"],
            "multi": [(r"/\*", r"\*/")]
        },
        "c": {
            "single": [r"//"],
            "multi": [(r"/\*", r"\*/")]
        },
        "cpp": {
            "single": [r"//"],
            "multi": [(r"/\*", r"\*/")]
        },
        "csharp": {
            "single": [r"//"],
            "multi": [(r"/\*", r"\*/")]
        },
        "php": {
            "single": [r"//", r"#"],
            "multi": [(r"/\*", r"\*/")]
        },
        "ruby": {
            "single": [r"#"],
            "multi": []
        },
        "bash": {
            "single": [r"#"],
            "multi": []
        },
        "haskell": {
            "single": [r"--"],
            "multi": [(r"\{-", r"-\}")]
        },
        "lua": {
            "single": [r"--"],
            "multi": [(r"--\[\[", r"\]\]")]
        },
        "html": {
            "single": [],
            "multi": [(r"<!--", r"-->")]
        },
        "sql": {
            "single": [r"--"],
            "multi": [(r"/\*", r"\*/")]
        },
    }

    syntax = comment_syntax.get(language.lower())
    if not syntax:
        raise ValueError(f"Language '{language}' not supported.")

    comments = []

    for start, end in syntax["multi"]:
        pattern = re.compile(f"{start}.*?{end}", re.DOTALL)
        comments.extend(pattern.findall(source))
        source = pattern.sub("", source)

    for single in syntax["single"]:
        pattern = re.compile(f"{single}.*?$", re.MULTILINE)
        comments.extend(pattern.findall(source))

    return [c.strip() for c in comments]
