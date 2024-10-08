# Arcanum

A tool for downloading articles from [adt.arcanum.com](https://adt.arcanum.com) in PDF format.

## Installation

1. Clone the repository
2. Install the required packages with `pip install -r requirements.txt`
3. Create a `.env` file with the following variables:
    * `ARCANUM_USERNAME`: your username for adt.arcanum.com
    * `ARCANUM_PASSWORD`: your password for adt.arcanum.com

## Usage

1. Run `python main.py <magazine_name> <block_numbers><year_numbers>`

    * `<magazine_name>`: the name of the magazine you want to download articles from
    * `<block_numbers>`: the numbers of the blocks you want to download articles from
        + e.g. `range(10)` will download articles from all blocks between 1 and 9
    * `<year_numbers>`: the numbers of the blocks you want to download articles from
        + e.g. `range(10)` will download articles from all years between 1 and 9

    Example: `python main.py NemzetiSport 1 3 5 7 9`

## Notes

* The script will create a folder in the current directory with the name of the magazine, and save the downloaded articles in that folder.
* If an article is already downloaded, the script will not re-download it.
* The script will not download articles that are not available in PDF format.
* The script may not work if the website changes its structure or if the magazine is not available in the specified block numbers.
