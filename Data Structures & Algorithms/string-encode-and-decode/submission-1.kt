class Solution {

    fun encode(strs: List<String>): String {
        if (strs.isEmpty()) {
            return ""
        }
        val lengths = strs.map { it.length }
        return "${lengths.joinToString(",")}#${strs.joinToString("")}"
    }

    fun decode(str: String): List<String> {
        if (str.isEmpty()) {
            return listOf()
        }
        val (encodedLengths, strs) = str.split("#", limit = 2)
        if (encodedLengths.isEmpty()) {
            return listOf()
        }
        val lengths = encodedLengths.split(",").map { it.toInt() }
        val result = mutableListOf<String>()
        var offset = 0
        for (len in lengths) {
            result.add(strs.substring(offset, offset + len))
            offset += len
        }
        return result
    }
}
