/**
 * @param {string[]} strs
 * @return {string[][]}
 */
function groupAnagrams(strs) {
    const map = {};

    for (let i = 0; i < strs.length; i += 1) {
        const word = strs[i];
        const sortedWord = Array.from(word).sort().join();
        if (map[sortedWord]) {
            map[sortedWord].push(word)
        } else { map[sortedWord] = [word] };
    }

    const result = [];
    Object.values(map).map((valArray) => {
        result.push(valArray);
    })

    return result;
}
