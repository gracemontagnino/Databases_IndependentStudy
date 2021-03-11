CREATE TABLE USER_IN
	(UNAME VARCHAR(15) NOT NULL PRIMARY KEY);
CREATE TABLE SURVEY
	(SNAME VARCHAR(20) NOT NULL PRIMARY KEY);
CREATE TABLE QUESTION
	(LABEL VARCHAR(30) NOT NULL PRIMARY KEY);
CREATE TABLE WASGIVEN
	(
    UNAME VARCHAR(15) NOT NULL,
    SNAME VARCHAR(20) NOT NULL,
    COMPLETED BOOL NOT NULL,
    PRIMARY KEY (UNAME, SNAME),
    FOREIGN KEY (UNAME) REFERENCES USER_IN (UNAME),
    FOREIGN KEY (SNAME) REFERENCES SURVEY (SNAME)
    );
CREATE TABLE HASQUESTION
	(
    SNAME VARCHAR(20) NOT NULL,
    LABEL VARCHAR(30) NOT NULL,
    PRIMARY KEY (LABEL, SNAME),
    FOREIGN KEY (LABEL) REFERENCES QUESTION (LABEL),
    FOREIGN KEY (SNAME) REFERENCES SURVEY (SNAME)
    );
CREATE TABLE RESPONDED
	(
    UNAME VARCHAR(15) NOT NULL,
    LABEL VARCHAR(30) NOT NULL,
    SCALE_VAL_USER_IN SMALLINT NOT NULL,
    PRIMARY KEY (UNAME, LABEL),
    FOREIGN KEY (UNAME) REFERENCES USER_IN (UNAME),
    FOREIGN KEY (LABEL) REFERENCES QUESTION (LABEL)
    );