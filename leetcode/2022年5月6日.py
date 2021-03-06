"""
写一个 RecentCounter 类来计算特定时间范围内最近的请求。

请你实现 RecentCounter 类：

RecentCounter() 初始化计数器，请求数为 0 。
int ping(int t) 在时间 t 添加一个新请求，其中 t 表示以毫秒为单位的某个时间，并返回过去 3000 毫秒内发生的所有请求数（包括新请求）。确切地说，返回在 [t-3000, t] 内发生的请求数。
保证 每次对 ping 的调用都使用比之前更大的 t 值。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-recent-calls
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
# class RecentCounter:
#
#     def __init__(self):
#         self.quee = []
#
#
#     def ping(self, t: int) -> int:
#         while self.quee[0] < t - 3000:
#             self.quee.pop([o])
#         return len(quee)
#
t = 3001
in__ = [[], [1], [100], [3001], [3002]]
real =  in__[1:]
print(real[0][0])
while real[0][0]< t - 3000:
    print(real.pop([0]))
print(len(real))



"""
class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)





class RecentCounter:

    def __init__(self):
        self.req = []  # 用于存放请求

    def ping(self, t: int) -> int:
        self.req.append(t)  # 先将请求添加的列表
        while t-self.req[0] > 3000:  # 循环判断是否有超出3000ms的请求
            del self.req[0]  # 删除超出的请求
        return len(self.req)  # 返回3000ms以内的请求
"""




