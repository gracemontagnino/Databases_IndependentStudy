CREATE TABLE userIn
	(unameFirst VARCHAR(30),
	 unameLast VARCHAR(30),
     userID SMALLINT NOT NULL PRIMARY KEY);
CREATE TABLE survey
	(sname VARCHAR(20) NOT NULL PRIMARY KEY,
     created DATETIME NOT NULL);
CREATE TABLE question
	(label VARCHAR(30) NOT NULL PRIMARY KEY,
     ordinal SMALLINT NOT NULL,
     FOREIGN KEY (sname) REFERENCES survey (sname));
CREATE TABLE wasGiven
	(
    uname VARCHAR(15) NOT NULL,
    sname VARCHAR(20) NOT NULL,
    completed DATETIME,
    PRIMARY KEY (uname, sname),
    FOREIGN KEY (uname) REFERENCES userIn (uname),
    FOREIGN KEY (sname) REFERENCES survey (sname)
    );
CREATE TABLE responded
	(
    uname VARCHAR(15) NOT NULL,
    label VARCHAR(30) NOT NULL,
    scaleValUserIn SMALLINT NOT NULL,
    PRIMARY KEY (uname, label),
    FOREIGN KEY (uname) REFERENCES userIn (uname),
    FOREIGN KEY (label) REFERENCES question (label)
    );