class ReportComment:
    """ 댓글 sql 생성

    """

    def __init__(self):
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

        self.incheon_user_id = "tiVRbcLxEKPcmsjhGZm0pRnA_100"
        self.busan_user_id = "tiVRbcLxEKPcmsjhGZm0pRnA_200"

    def make_sql(self, make_id, user_id):
        sql = (
                    "("
                    f"{make_id},"
                    f"'{title} 댓글',"
                    "'2022-02-17 20:41:12.000000',"
                    "'2022-02-17 20:41:12.000000',"
                    f"{id},"
                    f"'{user_id}'"
                    "),"
                )
        print(sql)
        return sql

if __name__ == '__main__':
    data = ReportComment()
    make_id = 1

    for id, title in data.report_list:
        for _ in range(10):  # 10 개씩 생성
            if id[0] == "1":  # 인천
                data.make_sql(make_id, data.incheon_user_id)
            if id[0] == "2":  # 부산
                data.make_sql(make_id, data.busan_user_id)
            make_id += 1