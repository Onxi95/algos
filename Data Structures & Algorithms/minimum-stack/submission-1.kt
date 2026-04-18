class MinStack() {
    private val stack = ArrayDeque<Int>()
    private val minStack = ArrayDeque<Int>()

    fun push(v: Int) {
        if (stack.isEmpty()) {
            stack.addLast(v)
            minStack.addLast(v)
        } else {
            val prevMin = minStack.last()
            minStack.addLast(minOf(prevMin, v))
            stack.addLast(v)
        }
    }

    fun pop() {
        stack.removeLast()
        minStack.removeLast()
    }

    fun top(): Int {
        return stack.last()
    }

    fun getMin(): Int {
        return minStack.last()
    }
}
