Given two names, the user votes on which one they like best.
The goal is to find the best-liked name with minimum voting.

---

## First Design: ##

Given the current set of votes, find the group of names with the least votes. Pit the best-liked name in the minimum
group against the best-liked name in the n+1 group.

### Simple database: ###
 * name
    * nameid
    * name
 * vote
    * greater_nameid
    * lesser_nameid
    * timestamp

### Simple client-server API: ###
 
 * GET /api/names/$N/
    * Get the next N names to be compared
 * POST /api/votes/    { 'lesser': $name1, 'greater': $name2 }
    * Send the results of a single vote.

### Simple client: ###

 1. fetch two names
 2. Display two big buttons with first two names
 3. When clicked, post the vote to the server.
 4. Repeat from 1.

### Testing: ###

Paul Irish says: Jasmine, Qunit or Mocha

Continuous integration! Travis?

Errorception.

