"""
Author  => v1siuol
Date    => 2017.03.18

201 / 201 test cases passed.
Status: Accepted
Runtime: 44 ms
"""
class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        r = color[1:3]
        g = color[3:5]
        b = color[5:7]

        return '#'+self.hi(r)+self.hi(g)+self.hi(b)

    def hi(self, twochar):
        lm_color_dict = {'0': 0, '1':16, '2':32, '3':48, '4': 64, '5':80, '6':96, 
        '7':112, '8':128, '9':144, 'a':160, 'b':176, 'c':192, 'd':208, 'e':224, 'f':240}

        rm_color_dict = {'0': 0, '1':1, '2':2, '3':3, '4': 4, '5':5, '6':6, 
        '7':7, '8':8, '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}

        back_color_dict = {0: '0', 1:'1', 2:'2', 3:'3', 4: '4', 5:'5', 6:'6', 
        7:'7', 8:'8', 9:'9', 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}

        tong = lm_color_dict[twochar[0]] + rm_color_dict[twochar[0]]
        mytong = twochar[0]+twochar[0]
        
        if twochar[0] != '0':
            zuo = lm_color_dict[twochar[0]]-16 + rm_color_dict[twochar[0]]-1
            myzuo = back_color_dict[rm_color_dict[twochar[0]]-1]+back_color_dict[rm_color_dict[twochar[0]]-1]
        else:
            zuo = lm_color_dict[twochar[0]] + rm_color_dict[twochar[0]]
            myzuo = twochar[0]+twochar[0]

        if twochar[0] != 'f':
            you = lm_color_dict[twochar[0]]+16 + rm_color_dict[twochar[0]]+1
            
            myyou = back_color_dict[rm_color_dict[twochar[0]]+1]+back_color_dict[rm_color_dict[twochar[0]]+1]
        else:
            you = lm_color_dict[twochar[0]] + rm_color_dict[twochar[0]]
            myyou = twochar[0]+twochar[0]
            
        # print(mytong, myzuo, myyou)

        ori = lm_color_dict[twochar[0]] + rm_color_dict[twochar[1]]

        mymin = self.dist(ori, tong)
        
        mychar = mytong
        # print(mymin)
        # print(mychar)

        if (self.dist(ori, zuo) < mymin):
            mymin = self.dist(ori, zuo)
            mychar = myzuo
            # print(mymin)
            # print(mychar)
        if (self.dist(ori, you) < mymin):
            mymin = self.dist(ori, you)
            mychar = myyou
            # print(mymin)
            # print(mychar)

        return mychar


    def dist(self, ori, b):
        # print(ori, b, (ori - b)^2)
        return (ori - b)**2