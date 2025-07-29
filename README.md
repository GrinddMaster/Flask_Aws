# Flask_Aws

## Goals
-Build two versions one that is vulnerable that can be exploited.
-Build a version that is more secure. 
-Finally to be deployed onto AWS cloud.

### Description
Flask framework was used to create and deploy a containarized project onto the cloud using docker.

#### Unsecure version provides:
- A login page where it verifies the user
- A lookup page where it searches for existing users
- A signup page to add new users

#### Secure version provides:
- Hashes the password stored in the database.
- Prevents path traversal exploit from the URL.
- Prevents path traversal of server files.

**MYSql** is the database for this project.

### This project is made by Ali Hussein & Yahya El Adawy @AASTMT
