
-- -----------------------------------------------------
-- Table `mydb`.`Game`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Game` ;

CREATE TABLE IF NOT EXISTS `Game` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `username` VARCHAR(45) NOT NULL,
  `guess_amount` INTEGER NOT NULL,
  `has_cheated` TINYINT NOT NULL,
  `start_time` DATETIME NOT NULL
);

