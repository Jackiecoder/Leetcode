class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # save_area = []
        # length = len(height)
        # # print('length=',length)
        # for i in range(length):
        #     tempMaxArea = (length-1-i)*min(height[i],height[length-1])
        #     tempMaxHeight = length-1
        #     for j in range(length-2,i,-1):
        #         if height[j] > height[tempMaxHeight]:
        #             challengerArea =  (j-i)*min(height[i],height[j])
        #             challengerHeight = j
        #             if challengerArea>tempMaxArea:
        #                 tempMaxArea = challengerArea
        #                 tempMaxHeight = challengerHeight
        #     save_area.append(tempMaxArea)
        # #     print(tempMaxArea)
        # # print('Finished')
        # return max(save_area)
        
        
        l=len(height)
        ans=0
        
        p1=0
        p2=l-1
        
        while p1<p2:
            
            ans=max(ans,min(height[p1],height[p2])*(p2-p1))
            
            if height[p1]<height[p2]:
                p1+=1
            else:
                p2-=1
        
        return ans
        