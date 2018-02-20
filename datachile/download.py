class Download(object):
    def __init__(self, data):
        self._data = data

    def xml(self, line_padding=""):
        result_list = list()

        json_obj_type = type(self._data)

        if json_obj_type is list:
            for sub_elem in json_obj:
                result_list.append(json2xml(sub_elem, line_padding))

            return "\n".join(result_list)

        if json_obj_type is dict:
            for tag_name in self._data:
                sub_obj = self._data[tag_name]
                result_list.append("%s<%s>" % (line_padding, tag_name))
                result_list.append(json2xml(sub_obj, "\t" + line_padding))
                result_list.append("%s</%s>" % (line_padding, tag_name))

            return "\n".join(result_list)

        return "%s%s" % (line_padding, self._data)

    def csv(self, data, delimiter=","):
        import json
        import csv

        #output = json.loads(data)
        output = data["data"]
        # open a file for writing
        employ_data = open('tmp.csv', 'w', encoding='utf8')

        # create the csv writer object
        csvwriter = csv.writer(employ_data, delimiter=delimiter)
        count = 0

        for emp in output:
            
            if count == 0:
                header = emp.keys()
                csvwriter.writerow(header)
                count += 1
            csvwriter.writerow(emp.values())
        employ_data.close()