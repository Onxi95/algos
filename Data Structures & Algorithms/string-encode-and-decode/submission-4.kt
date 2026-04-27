class Solution {
    fun encode(strs: List<String>): String {
        return strs.joinToString("") { "${it.length}#$it" }
    }

    fun decode(str: String): List<String> {
        val result = mutableListOf<String>()
        
        var i = 0

        while(i < str.length) {
            val hashIndex = str.indexOf('#', i)
            val length = str.substring(i, hashIndex).toInt()

            val start = hashIndex + 1
            val end = start + length

            result.add(str.substring(start, end))
            i = end
        }

        return result
    }
}
