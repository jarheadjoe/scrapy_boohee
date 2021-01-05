import codecs
import csv
from collections import defaultdict

from flask import json


class DataTransfer:
    def __init__(self):
        pass



    @staticmethod
    def trans_json_to_csv():
        food_details = get_food_details()
        group_map = get_grouped_food_details(food_details)
        food_names = get_all_food_names(food_details)
        for group_name, group_content in group_map.items():
            print('================', group_name, '================')
            with open('./csv/' + group_name + '.csv', mode='w',newline='') as data_file:
                # data_file.write(codecs.BOM_UTF8)
                csv_writer = csv.writer(data_file)
                csv_writer.writerow(['id', '来源', '名称', '分类', '红绿灯地址', '大图片地址', '小图片地址', '热量', '碳水化合物', '脂肪',
                                     '蛋白质', '纤维素', '维生素A', '维生素C', '维生素E', '胡萝卜素',
                                     '硫胺素', '核黄素', '烟酸', '胆固醇', '镁', '钙', '铁', '锌', '铜', '锰', '钾', '磷', '钠', '硒',
                                     '度量单位'])
                for food_obj in group_content:
                    print(food_obj['basic_info']['food_name'], food_obj['href'])
                    nutrition_dict = {}
                    for nutrition_obj in food_obj['nutrition_info']:
                        nutrition_dict[list(nutrition_obj.keys())[0]] = list(nutrition_obj.values())[0]
                    if '用户上传' in food_obj['source']:
                        source = '用户上传'
                    else:
                        source = '薄荷'
                    col_array = [
                        food_obj['href'].split('/')[-1],
                        source,
                        food_obj['basic_info']['food_name'],
                        food_obj['basic_info']['food_group_name'],
                        food_obj['basic_info']['traffic_light_img_href'],
                        food_obj['basic_info']['img_big_href'] ,
                        food_obj['basic_info']['img_small_href'],
                        food_obj['basic_info']['calories_value'],
                        nutrition_dict[u'碳水化合物(克)'] if u'碳水化合物(克)' in nutrition_dict else '',
                        nutrition_dict[u'脂肪(克)'] if u'脂肪(克)' in nutrition_dict else '',
                        nutrition_dict[u'蛋白质(克)'] if u'蛋白质(克)' in nutrition_dict else '',
                        nutrition_dict[u'纤维素(克)'] if u'纤维素(克)' in nutrition_dict else '',
                        nutrition_dict[u'维生素A(微克)'] if u'维生素A(微克)' in nutrition_dict else '',
                        nutrition_dict[u'维生素C(毫克)'] if u'维生素C(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'维生素E(毫克)'] if u'维生素E(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'胡萝卜素(微克)'] if u'胡萝卜素(微克)' in nutrition_dict else '',
                        nutrition_dict[u'硫胺素(毫克)'] if u'硫胺素(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'核黄素(毫克)'] if u'核黄素(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'烟酸(毫克)'] if u'烟酸(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'胆固醇(毫克)'] if u'胆固醇(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'镁(毫克)'] if u'镁(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'钙(毫克)'] if u'钙(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'铁(毫克)'] if u'铁(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'锌(毫克)'] if u'锌(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'铜(毫克)'] if u'铜(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'锰(毫克)'] if u'锰(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'钾(毫克)'] if u'钾(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'磷(毫克)'] if u'磷(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'钠(毫克)'] if u'钠(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'硒(微克)'] if u'硒(微克)' in nutrition_dict else '',
                        ",".join([k + v for item in food_obj['widget_unit_info'] for k, v in item.items()])
                    ]
                    csv_writer.writerow(col_array)
    @staticmethod
    def trans_json_to_csv_all():
        food_details = get_food_details()
        group_map = get_grouped_food_details(food_details)
        food_names = get_all_food_names(food_details)
        with open('./all.csv', mode='w', newline='') as data_file:
            # data_file.write(codecs.BOM_UTF8)
            csv_writer = csv.writer(data_file)
            csv_writer.writerow(['id', '来源', '名称', '分类', '红绿灯地址', '大图片地址', '小图片地址', '热量', '碳水化合物', '脂肪',
                                 '蛋白质', '纤维素', '维生素A', '维生素C', '维生素E', '胡萝卜素',
                                 '硫胺素', '核黄素', '烟酸', '胆固醇', '镁', '钙', '铁', '锌', '铜', '锰', '钾', '磷', '钠', '硒',
                                 '度量单位'])
            for group_name, group_content in group_map.items():
                print('================', group_name, '================')

                for food_obj in group_content:
                    print(food_obj['basic_info']['food_name'], food_obj['href'])
                    nutrition_dict = {}
                    for nutrition_obj in food_obj['nutrition_info']:
                        nutrition_dict[list(nutrition_obj.keys())[0]] = list(nutrition_obj.values())[0]
                    if '用户上传' in food_obj['source']:
                        source = '用户上传'
                    else:
                        source = '薄荷'
                    col_array = [
                        food_obj['href'].split('/')[-1],
                        source,
                        food_obj['basic_info']['food_name'],
                        food_obj['basic_info']['food_group_name'],
                        food_obj['basic_info']['traffic_light_img_href'],
                        food_obj['basic_info']['img_big_href'],
                        food_obj['basic_info']['img_small_href'],
                        food_obj['basic_info']['calories_value'],
                        nutrition_dict[u'碳水化合物(克)'] if u'碳水化合物(克)' in nutrition_dict else '',
                        nutrition_dict[u'脂肪(克)'] if u'脂肪(克)' in nutrition_dict else '',
                        nutrition_dict[u'蛋白质(克)'] if u'蛋白质(克)' in nutrition_dict else '',
                        nutrition_dict[u'纤维素(克)'] if u'纤维素(克)' in nutrition_dict else '',
                        nutrition_dict[u'维生素A(微克)'] if u'维生素A(微克)' in nutrition_dict else '',
                        nutrition_dict[u'维生素C(毫克)'] if u'维生素C(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'维生素E(毫克)'] if u'维生素E(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'胡萝卜素(微克)'] if u'胡萝卜素(微克)' in nutrition_dict else '',
                        nutrition_dict[u'硫胺素(毫克)'] if u'硫胺素(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'核黄素(毫克)'] if u'核黄素(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'烟酸(毫克)'] if u'烟酸(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'胆固醇(毫克)'] if u'胆固醇(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'镁(毫克)'] if u'镁(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'钙(毫克)'] if u'钙(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'铁(毫克)'] if u'铁(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'锌(毫克)'] if u'锌(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'铜(毫克)'] if u'铜(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'锰(毫克)'] if u'锰(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'钾(毫克)'] if u'钾(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'磷(毫克)'] if u'磷(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'钠(毫克)'] if u'钠(毫克)' in nutrition_dict else '',
                        nutrition_dict[u'硒(微克)'] if u'硒(微克)' in nutrition_dict else '',
                        ",".join([k + v for item in food_obj['widget_unit_info'] for k, v in item.items()])
                    ]
                    csv_writer.writerow(col_array)


def get_all_food_names(food_details):
    food_names = set()
    for food in get_food_details():
        food_names.add(food['basic_info']['food_name'].encode('utf-8'))
    return food_names


def get_grouped_food_details(food_details):
    group_map = defaultdict(list)
    for food_detail in food_details:
        food_group_name = food_detail['basic_info']['food_group_name']
        group_map[food_group_name].append(food_detail)
    return group_map


def get_food_details():
    return json.loads(open('./food_detail_backup.json').read())





if __name__ == '__main__':
    # DataTransfer.trans_json_to_csv()
    DataTransfer.trans_json_to_csv_all()
