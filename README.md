# Cleanup Obsidian Markdown to Hugo Markdown

The Obsidian Markdown Cleanup is a Python script that removes Obsidian-style link brackets from a text file, while preserving any link text that was present.

I made this, because I use Obsidian as my main markdown editor, and want to use its strong links. The problem was, that Hugo rendered the link brackets as well, and this script removed the need to manually remove all the brackets.

# Usage

To use the script, simply run it with a single argument specifying the name of the file to process. For example:

`python cleanup/cleanup.py my_text_file.md`

This will remove any link brackets from `my_text_file.md` and save the modified content back to the same file.

These are some possible cleanups: - `This is an [[Obsidian Link]]` turns into `This is an Obsidian Link` - `This is an [[Link|Obsidian Link]]` turns into `This is an Obsidian Link`

# Testing

The Obsidian Link Remover includes a set of automated tests to ensure that the script works correctly. To run the tests, navigate to the tests directory and run the following command:

python -m unittest

This will run all the tests and report any errors or failures.

# Contributing

If you'd like to contribute to the Obsidian Link Remover, please feel free to submit a pull request on GitHub. Any contributions are welcome!
