class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (!(s.length === t.length)) {
            return false;
        }
        const charMaps = new Map();
        const charMapt = new Map();

        for (let i = 0; i < s.length; i++) {
            charMaps.set(s[i], (charMaps.get(s[i]) ?? 0) + 1);
            charMapt.set(t[i], (charMapt.get(t[i]) ?? 0) + 1);
        }

        for (const [key,val] of charMaps) {
            if (!((charMapt.has(key)) && (charMapt.get(key) === val))) {
                return false;
            }
        }
        return true;

    }
}
