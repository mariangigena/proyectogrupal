alter table tip rename column business_id to gmap_id; 

CREATE TABLE lg_business (gmap_id VARCHAR(75), name_business varchar(50), laction text (6), luser VARCHAR(100), ddate datetime);
CREATE TABLE bussiness_records (id int AUTO_INCREMENT, tot_records int, luser VARCHAR())

CREATE TRIGGER log_business BEFORE INSERT ON business 
	FOR EACH ROW
    INSERT INTO lg_bussines (gmap_id, name_business, laction, luser, DDATE)
		VALUES (NEW.gmap_id, NEW.name_business, 'INSERT', USER(), NOW());

CREATE TABLE lg_categories (id_category MEDIUMINT, name_category varchar(50), laction text (6), luser VARCHAR(100), ddate datetime);
CREATE TRIGGER log_categories BEFORE INSERT ON categories 
	FOR EACH ROW
    INSERT INTO lg_categories (id_category, name_category, laction, luser, DDATE)
		VALUES (NEW.id_category, NEW.name_category,'INSERT', USER(), NOW());

CREATE TABLE lg_business_category (gmap_id VARCHAR(75), id_category MEDIUMINT, laction text (6), luser VARCHAR(100), ddate datetime);
CREATE TRIGGER log_business_category BEFORE INSERT ON bussiness_category 
	FOR EACH ROW
    INSERT INTO lg_categories_category (gmap_id, id_category, laction, luser, DDATE)
		VALUES (NEW.gmap_id, NEW.id_category, 'INSERT', USER(), NOW());

CREATE TABLE lg_misc (id_misc MEDIUMINT,misc_name varchar(75), id_servicio TINYINT, laction text (6), luser VARCHAR(100), ddate datetime);
CREATE TRIGGER log_misc BEFORE INSERT ON misc 
	FOR EACH ROW
    INSERT INTO lg_misc (id_misc, misc_name, id_servicio, laction, luser, DDATE)
		VALUES (NEW.id_misc, NEW.misc_name, NEW.id_servicio, 'INSERT', USER(), NOW());


CREATE TABLE lg_misc_bussin (id_misc MEDIUMINT, gmap_id VARCHAR(75), id_servicio TINYINT, laction text (6), luser VARCHAR(100), ddate datetime);
CREATE TRIGGER log_misc BEFORE INSERT ON misc 
	FOR EACH ROW
    INSERT INTO lg_misc (id_misc, misc_name, id_servicio, laction, luser, DDATE)
		VALUES (NEW.id_misc, NEW.misc_name, NEW.id_servicio, 'INSERT', USER(), NOW()); 


CREATE TABLE lg_reviews_google (id_state TINYINT, gmap_id VARCHAR(75), user_id varchar(25), laction text (6), luser VARCHAR(100), ddate datetime);
CREATE TRIGGER log_reviews_google BEFORE INSERT ON reviews_google
	FOR EACH ROW
    INSERT INTO lg_reviews_google (id_state, gmap_id, user_id, laction, luser, DDATE)
		VALUES (NEW.id_state, NEW.gmap_id, NEW.user_id, 'INSERT', USER(), NOW()); 


CREATE TABLE lg_servicio (id_servicio TINYINT, name_servicio VARCHAR(75), laction text (6), luser VARCHAR(100), ddate datetime);
CREATE TRIGGER log_servicio BEFORE INSERT ON servicio
	FOR EACH ROW
    INSERT INTO lg_servicio (id_servicio, name_servicio, laction, luser, DDATE)
		VALUES (NEW.id_servicio, NEW.name_servicio, 'INSERT', USER(), NOW()); 


CREATE TABLE lg_tip (user_id VARCHAR(50), gmap_id VARCHAR(75), date TIMESTAMP, laction text (6), luser VARCHAR(100), ddate datetime);
CREATE TRIGGER log_tip BEFORE INSERT ON tip
	FOR EACH ROW
    INSERT INTO lg_tip (user_id, gmap_id, laction, luser, DDATE)
		VALUES (NEW.user_id, NEW.gmap_id, 'INSERT', USER(), NOW()); 


alter TABLE tip rename column business_id to gmap_id;
alter TABLE tip modify column gmap_id VARCHAR(75);

ALTER TABLE Persons
MODIFY COLUMN DateOfBirth year;