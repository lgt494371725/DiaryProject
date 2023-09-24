CREATE TABLE IF NOT EXISTS t_pre_career(
`id` INT(32) PRIMARY KEY AUTO_INCREMENT COMMENT "入社前経験id",
 role VARCHAR(64) NOT NULL COMMENT "ロール",
 start_date DATE NOT NULL COMMENT "開始日",
 end_date DATE NOT NULL COMMENT "終了日",
 exp_detail TEXT(512) NOT NULL COMMENT "経験詳細",
 FOREIGN KEY(eid) REFERENCES t_employee(id)
)ENGINE=InnoDB DEFAULT CHARSET=UTF8; 

CREATE TABLE IF NOT EXISTS t_assign_exp(
`id` INT(32) PRIMARY KEY AUTO_INCREMENT COMMENT "アサイン経験id",
 role VARCHAR(64) NOT NULL COMMENT "ロール",
 start_date DATE NOT NULL COMMENT "開始日",
 end_date DATE NOT NULL COMMENT "終了日",
 FOREIGN KEY(eid) REFERENCES t_employee(id),
 FOREIGN KEY(project_id ) REFERENCES t_project(id) COMMENT "プロジェクトid"
)ENGINE=InnoDB DEFAULT CHARSET=UTF8; 
---