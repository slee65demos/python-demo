class Calculator:
    # calculate specific state's avg tuition rise between 2004-2016
    @staticmethod
    def state_avg_rise(data):
        num1 = data[1] - data[0]
        num2 = data[2] - data[1]
        num3 = data[3] - data[2]
        num4 = data[4] - data[3]
        num5 = data[5] - data[4]
        num6 = data[6] - data[5]
        num7 = data[7] - data[6]
        num8 = data[8] - data[7]
        num9 = data[9] - data[8]
        num10 = data[10] - data[9]
        num11 = data[11] - data[10]
        # round the output
        return round((num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11) / 11, 3)
    
    # calculate national average rise
    @staticmethod
    def national_avg_rise(data):
        num1 = sum(row[1] for row in data) - sum(row[0] for row in data)
        num2 = sum(row[2] for row in data) - sum(row[1] for row in data)
        num3 = sum(row[3] for row in data) - sum(row[2] for row in data)
        num4 = sum(row[4] for row in data) - sum(row[3] for row in data)
        num5 = sum(row[5] for row in data) - sum(row[4] for row in data)
        num6 = sum(row[6] for row in data) - sum(row[5] for row in data)
        num7 = sum(row[7] for row in data) - sum(row[6] for row in data)
        num8 = sum(row[8] for row in data) - sum(row[7] for row in data)
        num9 = sum(row[9] for row in data) - sum(row[8] for row in data)
        num10 = sum(row[10] for row in data) - sum(row[9] for row in data)
        num11 = sum(row[11] for row in data) - sum(row[10] for row in data)
        return round((num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11) / 11, 3)

    # calculate national rise each year
    @staticmethod
    def rise_each_year(data):
        num1 = sum(row[1] for row in data) - sum(row[0] for row in data)
        num2 = sum(row[2] for row in data) - sum(row[1] for row in data)
        num3 = sum(row[3] for row in data) - sum(row[2] for row in data)
        num4 = sum(row[4] for row in data) - sum(row[3] for row in data)
        num5 = sum(row[5] for row in data) - sum(row[4] for row in data)
        num6 = sum(row[6] for row in data) - sum(row[5] for row in data)
        num7 = sum(row[7] for row in data) - sum(row[6] for row in data)
        num8 = sum(row[8] for row in data) - sum(row[7] for row in data)
        num9 = sum(row[9] for row in data) - sum(row[8] for row in data)
        num10 = sum(row[10] for row in data) - sum(row[9] for row in data)
        num11 = sum(row[11] for row in data) - sum(row[10] for row in data)
        print("Tuition rise for 2004-05 - 2005-06: $" + str(num1))
        print("Tuition rise for 2005-06 - 2006-07: $" + str(num2))
        print("Tuition rise for 2006-07 - 2007-08: $" + str(num3))
        print("Tuition rise for 2007-08 - 2008-09: $" + str(num4))
        print("Tuition rise for 2008-09 - 2009-10: $" + str(num5))
        print("Tuition rise for 2009-10 - 2010-11: $" + str(num6))
        print("Tuition rise for 2010-11 - 2011-12: $" + str(num7))
        print("Tuition rise for 2011-12 - 2012-13: $" + str(num8))
        print("Tuition rise for 2012-13 - 2013-14: $" + str(num9))
        print("Tuition rise for 2013-14 - 2014-15: $" + str(num10))
        print("Tuition rise for 2014-15 - 2015-16: $" + str(num11))
