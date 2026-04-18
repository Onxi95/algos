class Solution {
    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        val map: MutableMap<String, MutableList<String>> = mutableMapOf()
        strs.forEach { str -> 
            val key = str.toList().sorted().joinToString("")
            map.getOrPut(key) { mutableListOf<String>() }.add(str)
        }
        return map.values.toList()
    }
}
