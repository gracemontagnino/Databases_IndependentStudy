#1a

USE new_surveys;
SELECT userID, COUNT(completed) FROM wasGiven
WHERE userID = 1001;
#GROUP BY userID;
SELECT userID, COUNT(sname) FROM wasGiven
GROUP BY userID;

#1c
SELECT userIn.unameFirst, responded.scaleValUserIn FROM userIn INNER JOIN responded
ON userIn.userID=responded.userID
WHERE unameFirst = "Olivia" 
GROUP BY (label);


SELECT AVG(responded.scaleValUserIn), userIn.userID FROM userIn INNER JOIN responded
ON userIn.userID=responded.userID
INNER JOIN question ON responded.label=question.label
WHERE unameFirst = "Kayla" AND sname = "test survey"
GROUP BY (userID);


  
#1d
SELECT u.unameFirst, COUNT(r.scaleValUserIn), r.scaleValUserIn
FROM userIn as u  
INNER JOIN responded as r ON u.userID=r.userID
INNER JOIN question as q ON r.label=q.label
WHERE unameFirst = "Kayla" AND sname = "test survey"
GROUP BY unameFirst, scaleValUserIn ;


#1e
SELECT DATEDIFF(w.completed, s.created) AS DAYS
FROM survey as s  
LEFT JOIN wasGiven as w ON s.sname=w.sname;


#2a
SELECT q.sname, r.label, AVG(r.scaleValUserIn) FROM responded as r
INNER JOIN question as q on r.label=q.label
GROUP BY label;
#2b
SELECT q.sname, q.ordinal, r.label, COUNT(r.scaleValUserIn), r.scaleValUserIn FROM responded as r
INNER JOIN question as q on r.label=q.label
GROUP BY sname, label, ordinal, scaleValUserIn;
#2c
SELECT q.sname, r.label, COUNT(r.scaleValUserIn), AVG(r.scaleValUserIn) FROM responded AS r
INNER JOIN question as q ON r.label=q.label
GROUP BY sname, label;