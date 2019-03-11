
def display_area():
    i = 0
    for data in climate_datas:
        print("{:>2}:{:<6}\t".format(i, data[0]), end="")
        i += 1
        if 0 == (i%5):
            print()
    print()

def display_temp(region_datas):
    print("顯示區域:", region_datas[0])
    print("-------------------")
    for i in range(1, 13):
        print("{:>2} 月均溫:{:>.1f}度".format(i, float(region_datas[i])))
    print("本地區年均溫為{}度".format(region_datas[13]))
    print("-------------------")


target_file = "climate.txt"
with open(target_file, 'r', encoding='utf-8') as file:
    raw_datas = file.readlines()
    climate_datas = []
    for data in raw_datas:
        climate_datas.append(data.rstrip('\n').split('\t'))

while True:
    display_area()
    area_index = int(input("請輸入你要查詢平均溫度的地區:(-1結束)"))
    if -1 == area_index:
        break
    display_temp(climate_datas[area_index])
    x = input("請按Enter鍵回主選單")