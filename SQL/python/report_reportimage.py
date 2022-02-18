class ReportImage:

    def __init__(self):
        self.image_file_name = "testImage.png"
        self.report_list = [
            ("101", "인천 모래내시장"),
            ("102", "인천 구월중학교"),
            ("103", "인천 터미널"),
            ("104", "인천 CSV"),
            ("105", "인천 올림픽국민생활관"),
            ("106", "인천 송도 센트럴파크"),
            ("107", "인천 대공원"),
            ("108", "인천 소래습지생태공원"),
            ("109", "인천 부평역"),
            ("110", "인천 부평공원"),
            ("111", "인천 주안역"),
            ("112", "인천 현대 프리미엄아울렛 송도점"),
            ("201", "부산 해운대"),
            ("202", "부산 광안리"),
            ("203", "부산 센텀시티 일반산업단지"),
            ("204", "부산 깡통시장"),
            ("205", "부산 보수동 헌책방 골목"),
            ("206", "부산 용두산 공원"),
            ("207", "부산 감천문화마을"),
            ("208", "부산 해동용궁사"),
            ("209", "부산 송정해수욕장")
        ]

    def make_sql(self, make_id, report_id):

        # 예시
        # "static/report/111/testImage.png"
        sql = (
                    "("
                    f"{make_id},"
                    f"'static/report/{report_id}/testImage.png',"
                    f"{report_id}"
                    "),"
                )
        print(sql)
        return sql

if __name__ == '__main__':
    R = ReportImage()
    make_id = 1
    for id, title in R.report_list:
        for _ in range(3):  # 3 개씩
            R.make_sql(make_id, id)
            make_id += 1