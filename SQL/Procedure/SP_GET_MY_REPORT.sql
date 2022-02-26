-- # -------------------------------- #
-- My UID를 입력하고
-- UID의 Report를 반환.
-- # -------------------------------- #

DROP PROCEDURE IF EXISTS SP_GET_MY_REPORT;
DELIMITER $$
CREATE PROCEDURE SP_GET_MY_REPORT(
    IN `in_uid` VARCHAR(28)
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
 		report_report.`updated_at`,
 		report_report.`category_id`
    FROM ( SELECT *
            FROM report_report
            WHERE report_report.`user_id` = `in_uid`) AS report_report
                
    LEFT JOIN user_user AS user_user
    ON report_report.`user_id` = user_user.`firebase_uid`

    LEFT JOIN report_category AS report_category
    ON report_report.`category_id` = report_category.`id`
	
	LEFT JOIN ( SELECT DISTINCT 
		report_reportimage.`report_id`,
		report_reportimage.`image`
	FROM report_reportimage ) AS report_reportimage
	ON report_reportimage.`report_id` = report_report.`id`;
	
END $$
DELIMITER ;

CALL SP_GET_MY_REPORT('tiVRbcLxEKPcmsjhGZm0pRnA_100');