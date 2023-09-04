import re
def solution(myStr):return [s for s in re.split('[abc]', myStr) if s] or ["EMPTY"]