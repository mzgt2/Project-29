# Project-29

## 🃏 Spanish Flash Cards

A desktop flashcard app built with Python and Tkinter to help you learn Spanish vocabulary.

## Features

- 🔀 **Random** Spanish words pulled from a word list
- ⏱️ **Auto-flips** card to English translation after 3 seconds
- ✅ **Mark known words** to remove them from the deck
- 💾 **Progress saved** — words you know won't appear again
- 🔄 **Resumes where you left off** on next launch

## Requirements

```bash
pip install pandas
```

> `tkinter` is included in Python's standard library.

## Setup

1. Clone or download the project
2. Install dependencies:
```bash
pip install pandas
```
3. Ensure your file structure matches below
4. Run the app:
```bash
python main.py
```

## File Structure

```
flash-cards/
├── main.py
├── data/
│   ├── spanish_words.csv     # Full word list (required)
│   └── words_to_learn.csv    # Auto-created, tracks remaining words
└── images/
    ├── card_front.png
    ├── card_back.png
    ├── right.png
    └── wrong.png
```

## How It Works

| Action | Button | Result |
|--------|--------|--------|
| **Known** | ✅ Right | Removes word from deck, saves progress |
| **Unknown** | ❌ Wrong | Keeps word in deck, shows next card |

- Card shows **Spanish** word on front
- After **3 seconds** it flips to the **English** translation
- Click ✅ or ❌ before or after the flip

## Notes

- Delete `words_to_learn.csv` to reset progress and start from the full word list
- `spanish_words.csv` must contain `Spanish` and `English` columns

## License

Free to use for personal and educational purposes.
