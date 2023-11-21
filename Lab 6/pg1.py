from collections import deque

def ladder_length(startWord, endWord, wordList):
    if endWord not in wordList or not startWord or not endWord or not wordList:
        return 0

    word_len = len(startWord)
    wordList = set(wordList)

    queue = deque([(startWord, 1)])

    while queue:
        current_word, level = queue.popleft()

        for i in range(word_len):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + char + current_word[i + 1:]

                if next_word == endWord:
                    return level + 1

                if next_word in wordList:
                    wordList.remove(next_word)
                    queue.append((next_word, level + 1))

    return 0

# Example usage:
startWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

result = ladder_length(startWord, endWord, wordList)
print("Length of the shortest transformation sequence:", result)
