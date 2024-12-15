/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
function isAnagram(s, t) {
    if (s.length !== t.length) return false;

    const map = {};

    // Build frequency map for string `s`
    for (const letter of s) {
        map[letter] = (map[letter] || 0) + 1;
    }

    // Reduce frequency based on string `t`
    for (const letter of t) {
        if (!map[letter]) {
            return false; // Letter not found or already depleted
        }
        map[letter] -= 1;
    }

    // Check for remaining non-zero values
    for (const count of Object.values(map)) {
        if (count !== 0) {
            return false; // Some letters are unbalanced
        }
    }

    return true;
}
