def solution(n):
    def fib(n):
        _curr, _next = 0, 1
        for _ in range(n):
            _curr, _next = _next, _curr + _next
        return _curr
    
    
    return fib(n)%1234567