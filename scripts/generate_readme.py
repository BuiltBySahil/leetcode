from pathlib import Path

README = Path("README.md")
SOLUTIONS = Path("solutions")

rows = []

for folder in sorted(SOLUTIONS.iterdir()):
    if not folder.is_dir():
        continue

    name = folder.name

    if "-" not in name:
        continue

    number, title = name.split("-", 1)

    title = title.replace("-", " ").title()

    row = f"| {number} | {title} | - | - | [Java]({folder.as_posix()}/Solution.java) |"

    rows.append(row)

table = "\n".join(rows)

readme = README.read_text(encoding="utf-8")

start = "<!-- START_TABLE -->"
end = "<!-- END_TABLE -->"

before = readme.split(start)[0]
after = readme.split(end)[1]

new_readme = (
    before
    + start
    + "\n\n"
    + "| # | Problem | Difficulty | Topic | Solution |\n"
    + "|---|---------|------------|-------|----------|\n"
    + table
    + "\n\n"
    + end
    + after
)

README.write_text(new_readme, encoding="utf-8")

print("README Updated Successfully!")
