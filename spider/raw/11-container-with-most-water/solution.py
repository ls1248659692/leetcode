class Solution:
    def maxArea(self, height: List[int]) -> int:
        def mxa_v0(height):
            ww = len(height) - 1
            all_h_sort = sorted(list(set(height)),reverse=True)
            height_dict = {hh:set() for hh in all_h_sort}
            for ii in range(len(height)):
                height_dict[height[ii]].add(ii)
            
            water = (max(height_dict[all_h_sort[0]]) - min(height_dict[all_h_sort[0]])) * all_h_sort[0]
            wall_pool=height_dict[all_h_sort[0]]
            for hh in all_h_sort[1:]:
                if hh * ww < water: break
                wall_pool = height_dict[hh].union({min(wall_pool), max(wall_pool)})
                new_water = (max(wall_pool) - min(wall_pool)) * hh
                water = new_water if new_water > water else water
            return water

        def mxa_v1(height):
            all_h_sort = sorted(list(set(height)),reverse=True)
            height_dict = {hh:[] for hh in all_h_sort}
            for ii in range(len(height)):
                height_dict[height[ii]].append(ii)
            
            water,widthi_pool = 0,[]
            # åè®¾ hh æ¯ ä¸¤èè¾ä½çbar, æ»¡è¶³è¯¥æ¡ä»¶ä¸ç æè¿iè·ç¦»ï¼è¿­ä»£æè¿iè·ç¦»
            for hh in all_h_sort[0:]:
                widthi_pool = height_dict[hh]+([min(widthi_pool), max(widthi_pool)] if widthi_pool else [])
                new_water = (max(widthi_pool) - min(widthi_pool)) * hh
                water = new_water if new_water > water else water
            return water    
        return mxa_v1(height)        