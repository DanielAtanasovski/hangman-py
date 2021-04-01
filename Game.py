class game:
    def __init__(self) -> None:
        self.word_list = self.setup_file_word_list()
        self.word = "none"

        pass

    def get_random_word() -> str:
        pass

    def setup_file_word_list() -> list:
        file_words = []
        # Get the word list and convert to array
        with open("wordlist.txt") as file:
            for line in file:
                file_words.append(line.strip())
        return file_words
