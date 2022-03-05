-- # -------------------------------- #
-- report ID를 입력하고 
-- 해당 detail를 반환
-- # -------------------------------- #

DROP PROCEDURE IF EXISTS SP_GET_REPORT_DETAIL;
DELIMITER $$
CREATE PROCEDURE SP_GET_REPORT_DETAIL(
    IN `in_report_id` INT
)
BEGIN

    SELECT 
    	report_report.`id`,
		report_report.`title`,
		report_report.`explanation`,
		report_report.`solved_title`,
		report_report.`solved_explanation`,
		report_report.`latitude`,
		report_report.`longitude`,
		report_report.`recommendation`,
		report_report.`solved`,
		report_report.`created_at`,
		report_report.`updated_at`,
		report_report.`solved_created_at`,
		report_report.`solved_updated_at`,
		report_report.`user_id`,
		user_user.`google_profile_image`,
		user_user.`app_name`,

		report_report.`solved_user`,
		report_report.`solved_google_profile_image`,
		report_report.`solved_app_name`,

		report_report.`category_id`
    FROM ( SELECT *
            FROM report_report
            WHERE report_report.`id` = `in_report_id` ) AS report_report
    
    INNER JOIN user_user
    ON user_user.`firebase_uid` = report_report.`user_id`;

END $$
DELIMITER ;

CALL SP_GET_REPORT_DETAIL(104);