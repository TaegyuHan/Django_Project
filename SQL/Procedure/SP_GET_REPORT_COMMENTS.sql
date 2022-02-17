-- # -------------------------------- #
-- report ID를 입력하고 
-- 해당 ID의 댓글을 가져오는 프로시져
-- # -------------------------------- #

DROP PROCEDURE IF EXISTS SP_GET_REPORT_COMMENTS;
DELIMITER $$
CREATE PROCEDURE SP_GET_REPORT_COMMENTS(
    IN `in_report_id` INT
)
BEGIN

      SELECT report_comment.id,
            report_comment.content,
            report_comment.created_at,
            report_comment.updated_at,
            user_user.firebase_uid,
            user_user.google_profile_image,
            user_user.app_name
        FROM ( SELECT *
            FROM report_comment
            WHERE report_comment.report_id=`in_report_id`
        ) AS report_comment
        LEFT JOIN user_user AS user_user
        ON report_comment.user_id = user_user.firebase_uid
		  ORDER BY report_comment.created_at ASC;

END $$
DELIMITER ;

CALL SP_GET_REPORT_COMMENTS(12);