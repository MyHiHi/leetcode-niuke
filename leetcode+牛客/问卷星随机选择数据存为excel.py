# -*- encoding: utf-8 -*-
'''
@File    :   问卷星随机选择数据存为excel.py
@Time    :   2020/03/09 16:47:23
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   问卷星随机选择数据存为excel.py
'''


def getData():
    data = {}
    from pyquery import PyQuery as pq
    html = pq('https://www.wjx.cn/m/59597032.aspx')
    for line in html('.field.ui-field-contain').items():
        q = line('.field-label')
        qu = q.text()
        ans = [t.text for t in line.find('.label')]
        data[qu] = ans
    return data


def writeExcel(data,num):
    import xlwt
    import random
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('调查', cell_overwrite_ok=True)
    le = len(data)
    keys = list(data.keys())
    for l in range(le):
        worksheet.write(0, l, keys[l])
    i = 1
    va = [list(v) for v in data.values()]
    # print(va, len(va))
    while i <= num:
        [random.shuffle(v) for v in va]
        myV = []
        myV += [va[c][0] for c in range(5)]
        rt = random.randint(1, 4)
        myV += [','.join(random.sample(va[5], rt))]
        myV += [va[c][0] for c in range(6, 9)]
        myV += [','.join(random.sample(va[9], rt))]
        myV += [va[c][0] for c in range(10, 19)]
        myV += [','.join(random.sample(va[19], rt))]
        myV += [va[c][0] for c in range(20, 33)]
        myV += [','.join(random.sample(va[t], rt)) for t in range(33, 35)]
        for l in range(le):
            worksheet.write(i, l, myV[l])
        i += 1
    workbook.save('D:\excel.xls')
    print('finished!')


data = getData()
# print(data)
writeExcel(data,2000)
