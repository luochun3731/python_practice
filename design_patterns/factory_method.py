'''
Factory Method: 不通过类而是通过工厂函数来创建对象.
'''

import xml.etree.ElementTree as etree
import json


class JSONConnector:
    def __init__(self, file_path):
        self.data = dict()
        with open(file_path, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    # @Properyty将成员函数的调用变成属性赋值（负责把一个方法变成属性调用）
    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, file_path):
        self.tree = etree.parse(file_path)

    # @Properyty将成员函数的调用变成属性赋值（负责把一个方法变成属性调用）
    @property
    def parsed_data(self):
        return self.tree


def connection_factory(file_path):
    if file_path.endswith('json'):
        connector = JSONConnector
    elif file_path.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(file_path))
    return connector(file_path)


def connect_to(file_path):
    factory = None
    try:
        factory = connection_factory(file_path)
    except ValueError as err:
        print(err)
    return factory


def main():
    sqlite_factory = connect_to('data/person.sq3')

    xml_factory = connect_to('data/person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar'))
    print('#################### xml data ####################')
    print('found: {} persons'.format(len(liars)))
    for liar in liars:
        print('first name: {}'.format(liar.find('firstName').text))
        print('last name: {}'.format(liar.find('lastName').text))
        [print('phone number: ({})'.format(p.attrib['type']), p.text) for p in liar.find('phoneNumbers')]
    print()

    json_factory = connect_to('data/donut.json')
    json_data = json_factory.parsed_data
    print('#################### json data ####################')
    for donut in json_data:
        print('name: {}'.format(donut['name']))
        print('price: {}'.format(donut['ppu']))
        [print('toppint: {} {}'.format(t['id'], t['type'])) for t in donut['topping']]
        print('\n')


if __name__ == '__main__':
    main()
