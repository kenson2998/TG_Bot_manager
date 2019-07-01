from selenium import webdriver

'''
func1 :
放IP 与 网域查询功能
'''


def func1(**kwargs):
    from chrome_space import chrome_setting
    try:
        results = ''
        print(kwargs)
        if kwargs['function'] == 'IP查询' and kwargs['content'] != '':
            html_url = 'http://ip138.com/ips138.asp?ip=' + kwargs['content']
            # d = webdriver.Chrome(options=chrome_setting.options)
            d = webdriver.Chrome(chrome_setting.chromedriver_dir, options=chrome_setting.options)
            d.get(html_url)
            data_table = d.find_elements_by_xpath('/html/body/table/tbody/tr[3]/td/ul')
            for i in data_table:
                results += i.text
        if kwargs['function'] == 'DNS查询' and kwargs['content'] != '':
            html_url = 'http://ip.tool.chinaz.com/' + kwargs['content']
            d = chrome_setting.webdriver.Chrome(chrome_setting.chromedriver_dir, options=chrome_setting.options)
            d.get(html_url)
            data_list = d.find_elements_by_css_selector('p.WhwtdWrap:nth-child(1)')
            data_table = d.find_elements_by_css_selector('p.WhwtdWrap:nth-child(2)')
            data_table1 = d.find_elements_by_css_selector('p.WhwtdWrap:nth-child(3)')
            results3 = [{}, {}]
            for i in data_list:
                list_1 = (i.text).split('\n')

            for i in data_table:
                results1 = i.text.split('\n')
                for ii in range(len(list_1)):
                    results3[0][list_1[ii]] = results1[ii]
            for k, v in results3[0].items():
                results += '%s : %s \n' % (k, v)

            if data_table1 != []:
                for i in data_table1:
                    results2 = i.text.split('\n')
                    for ii in range(len(list_1)):
                        results3[1][list_1[ii]] = results2[ii]
                for k, v in results3[1].items():
                    results += '%s : %s \n' % (k, v)
        d.close()
    except:
        results = '查詢失敗'
    if kwargs['content'] == '':
        results = '查詢失敗'
    return results
