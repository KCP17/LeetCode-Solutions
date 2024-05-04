class Solution():
    def maxWidthOfVerticalArea(self, points):
        x_cors = []
        for point in points:
            x_cors.append(point[0])

        sorted_x_cors = self.quicksort(x_cors)

        max_width = 0
        for i in range(len(sorted_x_cors)-1):
            distance = sorted_x_cors[i+1] - sorted_x_cors[i]
            if distance > max_width:
                max_width = distance

        return max_width
    
    def quicksort(self, x_cors):
        if len(x_cors) <= 1: return x_cors
        pivot = x_cors[0]
        less_than_pivot = []
        greater_than_pivot = []

        for x_cor in x_cors[1:]:
            if x_cor < pivot:
                less_than_pivot.append(x_cor)
            else:
                greater_than_pivot.append(x_cor)
        
        return self.quicksort(less_than_pivot) + [pivot] + self.quicksort(greater_than_pivot)
