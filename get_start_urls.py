    def get_start_urls(self, data=None):
        '''
        部分网页频道页比较规律且数量较多，在此处直接抓取链接返回给parse函数
        '''
        channel_urls = set()
        url = {'url': '', 'meta': {'keep_status_code': True}}
        response = self.download(url)
        try:
            M = str(re.findall("F='(.*?)'", response.content)[0])
            t = re.findall("C='(\d+)'", response.content)[0]
            Y = re.findall("Y='([a-f0-9]+)'", response.content)[0]
        except:
            return []
        num = 0
        for i in M:
            num += ord(i)
        num_finall = num * int(t) + 111111
        key_str = 'WZWS_CONFIRM_PREFIX_LABEL{}'.format(num_finall)
        key_str_base64 = base64.b64encode(key_str)
        Y_str = '''{"hostname":"www.xcjw.gov.cn","scheme":"http","verify":"%s"}''' % (Y)
        Y_str_base_64 = base64.b64encode(Y_str)
        seconde_jump_url = '/WZWSRELw==?wzwschallenge={}&wzwsinfos={}'.format(
            key_str_base64, Y_str_base_64)
        resp = self.download({'url': seconde_jump_url, 'meta': {'keep_status_code': True}})
        return self.start_urls
