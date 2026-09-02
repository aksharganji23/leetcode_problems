char* longestCommonPrefix(char** strs, int strsSize) {
    if (strsSize == 0) return "";

    // Take the first string as reference
    char* first = strs[0];

    // Compare char by char
    for (int i = 0; first[i] != '\0'; i++) {
        char c = first[i];

        // Check if this character matches in all strings
        for (int j = 1; j < strsSize; j++) {
            // If mismatch or string ended
            if (strs[j][i] != c) {
                // Allocate result prefix
                char* ans = (char*)malloc(i + 1);
                strncpy(ans, first, i);
                ans[i] = '\0';
                return ans;
            }
        }
    }

    // If the whole first string is the prefix
    char* ans = (char*)malloc(strlen(first) + 1);
    strcpy(ans, first);
    return ans;
}
