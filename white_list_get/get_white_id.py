import os


class get_whitelist_id:
    def __init__(self, msg):
        print()
        self.id = msg
        self.T_or_F, self.W_list, self.id_path = self.whitelist()

    def whitelist(self):

        whitelist = []
        id_path = os.path.dirname(os.path.abspath(__file__)) + '/id.csv'
        with open(id_path, 'r', encoding='utf-8-sig') as idc:
            for i in idc:
                try:
                    ids = i.split(',')
                    whitelist.append(ids[2].replace('\n', ''))
                except IndexError as e:
                    print('格式错误 %s,可能是id.csv中间有空白,请将空白列清除' % e)
                    continue
                except:
                    print('white error')

        if str(self.id) in whitelist:
            return True, whitelist, id_path
        else:
            return False, whitelist, id_path
