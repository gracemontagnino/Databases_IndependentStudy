use new_surveys;
CREATE TABLE IF NOT EXISTS userIn
	(unameFirst VARCHAR(30),
	 unameLast VARCHAR(30),
     userID SMALLINT NOT NULL PRIMARY KEY);
CREATE TABLE IF NOT EXISTS survey
	(sname VARCHAR(20) NOT NULL PRIMARY KEY,
     created DATETIME NOT NULL);
CREATE TABLE IF NOT EXISTS question
	(label VARCHAR(30) NOT NULL PRIMARY KEY,
     ordinal SMALLINT NOT NULL,
     sname VARCHAR(20) NOT NULL,
     FOREIGN KEY (sname) REFERENCES survey (sname));
CREATE TABLE IF NOT EXISTS wasGiven
	(
    userID SMALLINT NOT NULL,
    sname VARCHAR(20) NOT NULL,
    completed DATETIME,
    PRIMARY KEY (userID, sname),
    FOREIGN KEY (userID) REFERENCES userIn (userID),
    FOREIGN KEY (sname) REFERENCES survey (sname)
    );
CREATE TABLE IF NOT EXISTS responded
	(
    userID SMALLINT NOT NULL,
    label VARCHAR(30) NOT NULL,
    scaleValUserIn SMALLINT NOT NULL,
    PRIMARY KEY (userID, label),
    FOREIGN KEY (userID) REFERENCES userIn (userID),
    FOREIGN KEY (label) REFERENCES question (label)
    );

