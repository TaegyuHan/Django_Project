-- # -------------------------------- #
-- 현위치의 주변의
-- report 리스트를 가져 오는 프로시져
-- # -------------------------------- #

DROP PROCEDURE IF EXISTS SP_GET_REPORT_LIST;
DELIMITER $$
CREATE PROCEDURE SP_GET_REPORT_LIST(
    IN `in_bot_latitude` INT,
    IN `in_top_latitude` INT,
    IN `in_bot_longitude` INT,
    IN `in_top_longitude` INT
)
BEGIN

    SELECT 
        report_report.`id`,
        report_report.`title`,
        report_report.`explanation`,
        report_report.`category_id`,
        report_category.`content`,
        report_reportimage.`image`,
        report_report.`user_id`,
        report_report.`latitude`,
        report_report.`longitude`,
        report_report.`recommendation`,
        report_report.`solved`,
        user_user.`app_name`,
        user_user.`google_profile_image`,
        report_report.`created_at`,
        report_report.`updated_at`
    FROM ( SELECT *
            FROM report_report
            WHERE (report_report.`latitude` >= `in_bot_latitude`
                AND report_report.`latitude` <= `in_top_latitude`
                AND report_report.`longitude` >= `in_bot_longitude`
                AND report_report.`longitude` <= `in_top_longitude`
                AND report_report.`solved` = 0)) AS report_report
                
    LEFT JOIN user_user AS user_user
    ON report_report.`user_id` = user_user.`firebase_uid`

    LEFT JOIN report_category AS report_category
    ON report_report.`category_id` = report_category.`id`

    LEFT JOIN ( SELECT 
                    report_reportimage.`image`,
                    report_reportimage.`report_id`
                FROM report_reportimage
                GROUP BY report_reportimage.`report_id` ) AS report_reportimage
    ON report_reportimage.`report_id` = report_report.`id`;


END $$
DELIMITER ;

CALL SP_GET_REPORT_LIST(37.2239727, 37.6239727, 125.8543867, 127.4543867);