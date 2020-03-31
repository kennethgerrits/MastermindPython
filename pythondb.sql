
-- -----------------------------------------------------
-- Table `Player`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Player` ;

CREATE TABLE IF NOT EXISTS `Player` (
  `id` INT PRIMARY KEY NOT NULL,
  `username` VARCHAR(45) NOT NULL UNIQUE
);

-- -----------------------------------------------------
-- Table `mydb`.`Game`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Game` ;

CREATE TABLE IF NOT EXISTS `Game` (
  `id` INT PRIMARY KEY NOT NULL,
  `Player_id` INT NOT NULL,
  `guess_amount` INT NOT NULL,
  `has_cheated` TINYINT NOT NULL,
  `start_time` DATETIME NOT NULL,
    FOREIGN KEY (`Player_id`)
    REFERENCES `Player` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

