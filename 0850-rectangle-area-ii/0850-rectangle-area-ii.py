class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7
        # collect all y's for coordinate compression
        ys = set()
        for x1, y1, x2, y2 in rectangles:
            ys.add(y1); ys.add(y2)
        ys = sorted(ys)
        y_id = {v: i for i, v in enumerate(ys)}
        
        # events: (x, y1, y2, type)  type=1 add, -1 remove
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, y1, y2, 1))
            events.append((x2, y1, y2, -1))
        events.sort()
        
        n = len(ys) - 1   # number of intervals between y's
        cover = [0] * (4 * n)
        length = [0] * (4 * n)
        
        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                cover[node] += val
            else:
                mid = (l + r) // 2
                if ql <= mid:
                    update(node*2, l, mid, ql, qr, val)
                if qr > mid:
                    update(node*2+1, mid+1, r, ql, qr, val)
            if cover[node] > 0:
                length[node] = ys[r+1] - ys[l]
            else:
                length[node] = length[node*2] + length[node*2+1] if l != r else 0
        
        ans = 0
        prev_x = events[0][0]
        i = 0
        while i < len(events):
            x = events[i][0]
            ans = (ans + length[1] * (x - prev_x)) % MOD
            while i < len(events) and events[i][0] == x:
                _, y1, y2, typ = events[i]
                update(1, 0, n-1, y_id[y1], y_id[y2]-1, typ)
                i += 1
            prev_x = x
        return ans