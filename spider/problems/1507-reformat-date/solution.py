class Solution:
    def reformatDate(self, date: str) -> str:
        y = date[-4:]
        dic= {"Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05', "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}
        month = dic[date[-8:-5]]
        day = ''
        if date[:2].isdigit():
            day = date[:2]
        elif date[0].isdigit():
            day = '0{}'.format(date[0])
        return '{}-{}-{}'.format(y,month,day)