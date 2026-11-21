class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        // given an array of strs, group all anagrams together into sublists.
        // you may return the output in any order.

        // an anagram is a string that contains the exact same characters as another string
        // but the orders of the characters can be different
        
        // Example:
        // Input: strs = ["act","pots","tops","cat","stop","hat"]
        // Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        // APPROACH 1 Brute force
        // Create a map of key-value pairs representing {map:word}
        // where map represents each character and its frequency. For example
        // {{"c":1,"a":1,"t":1:"cat"} O(n)
        // Then, have a running array made up of tuples [ (map, [words]) ]
        // and iteratively compare each map to each map in the running array, 
        // appending if one doesn't exist and incrementing one with the respective word if it does.
        // Worst case : O(n^2)

        // APPROACH 2 : Convert Map to Strings. 
        // Create a map of key-value pairs representing {charFreqs:word}
        // where string represents each character and its frequency. For example
        // {{"a1b0c1..t1..z0":"cat"} O(n)
        // Then, create an array of strings to words [(str, [words])]
        // Since key lookups for strings are in constant time, this loop will also be O(n)


        const firstLetterInd = "a".charCodeAt(0);
        const ourMap = new Map() // str:wrd

        for (const str of strs) {
            let count = new Array(26).fill(0)
            for (const c of str) {
                count[c.charCodeAt(0) - firstLetterInd] += 1;
            }
            const freqStr = count.join(",");
            if (!ourMap.has(freqStr)) {
                ourMap.set(freqStr,[str]);
            } 
            else {
                ourMap.get(freqStr).push(str);
            }
        }

        return Array.from(ourMap.values());

    }
}
