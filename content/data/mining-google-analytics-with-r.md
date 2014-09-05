Title: Mining Google Analytics with R
Date: 
Author: gmwils
Summary: 
status: draft

Download from https://code.google.com/p/r-google-analytics/ the .tar.gz file.

Run the following from the command line:

```shell
R CMD INSTALL RGoogleAnalytics_1.4.tar.gz
```

Then you can run the library:

```
# Loading the RGoogleAnalytics library
require("RGoogleAnalytics")

# Step 1. Authorize your account and paste the accesstoken 
query <- QueryBuilder()
access_token <- query$authorize()
```
