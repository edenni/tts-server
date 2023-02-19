from app import speakers
from pprint import pprint

with open("speaker_list.txt", "w") as f:
    for i, s in zip(range(len(speakers)), speakers):
        f.write(f"{i}: {s}\n")
