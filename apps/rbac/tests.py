from django.test import TestCase

# Create your tests here.
permissions_menu = [{'id': 10, 'title': '用户管理', 'parent': 5}, {'id': 9, 'title': '组织结构', 'parent': 5},
                    {'id': 8, 'title': '公司单位', 'parent': 5}, {'id': 7, 'title': '系统工具', 'parent': 1},
                    {'id': 6, 'title': '权限管理', 'parent': 1}, {'id': 5, 'title': '基础设置', 'parent': 1},
                    {'id': 4, 'title': '流程', 'parent': None}, {'id': 3, 'title': '人力资源', 'parent': None},
                    {'id': 2, 'title': '行政管理', 'parent': None}, {'id': 1, 'title': '系统', 'parent': None}]


all_menu_dict = {}
for item in permissions_menu:
    item['children'] = []
    all_menu_dict[item['id']] = item

def get_menu_data(all_menu_dict):
    menu_data = []
    for i in all_menu_dict:
        if all_menu_dict[i]['parent']:
            pid = all_menu_dict[i]['parent']
            parent_menu = all_menu_dict[pid]
            parent_menu['children'].append(all_menu_dict[i])
        else:
            menu_data.append(all_menu_dict[i])

    return menu_data














