class Solution {
    fun encode(strs: List<String>): String {
        return strs.map { "${it.length}#$it" }.joinToString("")
    }

    fun decode(str: String): List<String> {
        var i = 0

        val result = mutableListOf<String>()

        while (i < str.length) {
            var j = i
            var num = StringBuilder()
            while (str[j] != '#') {
                num.append(str[j])
                j++
            }
            val length = num.toString().toInt()
            val start = j + 1
            val end = start + length

            result.add(str.substring(start, end))
            i = end
        }

        return result
    }
}
