# AWS-Boto3
Amazon Web Services (AWS) offers a service known as Identity and Access Management (IAM) that lets AWS Administrators provision and manage users and permissions in AWS cloud.  AWS IAM can prove very useful for System Administrators looking to centrally manage users, permissions and credentials; in order to authorize user access on AWS services like EC2, S3, CloudWatch etc.

AWS SDK for Python, also known as the Boto-3 library, makes user management very simple by letting user, developers and sysadmins write Python scripts to create and manage IAM users in AWS infrastructure. Before starting writing Python programs to automate IAM, it is a prerequisite to configure AWS credentials in a Shell environment. These credentials must have full  access admin rights to manage the AWS IAM service, and  here is my article to setup the environment on a local computer.

Here we'll take a look at how Python can be used by System Administrators to automate the management of Amazon Web Services (AWS) Elastic Compute Cloud (EC2) infrastructure. You'll learn how to set up the Python scripting environment for first use, and how to enable ourself as a user to create Python scripts to launch virtual machine instances in AWS EC2 as per specific requirements. 

# Install AWS CLI and Python Boto3 Library :-

Before we can get started, we need to install Boto3 library in Python and the AWS Command Line Interface (CLI) tool using 'pip' which is a package management system written in Python used to install and manage packages that can contain code libraries and dependent files.

Boto3 is the AWS SDK for Python, which provides Object-based APIs and low-level direct access to AWS services like EC2. AWS CLI is a command line tool written in Python that introduces efficient use cases to manage AWS services with a set of very simple commands. 

Using 'pip' run the following command to install the AWS CLI and Python's Boto3 library on your machine: 
  
 # "pip install awscli boto3"

# Create a User and get AWS Access ID and Secret Key

Now that we've installed the AWS CLI and Boto3, its time to create your user credentials on the AWS console, so that AWS services can be access programmatically. Follow these steps to create your user credentials:

1. Launch the Identity and Access Management console (IAM) in AWS. 

2. Click Users on the navigation menu on the left of the screen. 

3. In the popup window, click on Add User. 

In the new window, provide a user name and choose the 'Programmatic Access' access type, then click next. 

To set the permissions, choose 'Attach Existing Policies Directly' and in the Policy Filter type 'AmazonEC2FullAccess', you can choose any permission level, but in this example I'll click on the checkbox next to 'AmazonEC2FullAccess' and then click the 'next' button.

Finally, review the user and permission levels, and click on the 'Create User' button. 

 The next page will show your keys, as shown below. These are only available once, so it its a good idea to download and save then safely in a secure location. 
