# Project Setup - New Project
---
## Summary
Before starting the first technical lab, we will be walking through how to create your own project to get familiar with watsonx.ai and ensure you have access to your environment for the bootcamp. 

It is important we create a project in the right environment, or else it will cause issues down the line!

## Table of Contents

- [Project Setup - New Project](#project-setup---new-project)
  - [Summary](#summary)
  - [Table of Contents](#table-of-contents)
    - [1. Log into watsonx](#1-log-into-watsonx)
    - [2. Check that you are in the right instance](#2-check-that-you-are-in-the-right-instance)
    - [3. Create a new project](#3-create-a-new-project)
    - [Cloud Object Storage (COS)](#cloud-object-storage-cos)
    - [Click Create](#click-create)
    - [4. Associate the correct runtime instance](#4-associate-the-correct-runtime-instance)
  - [Steps to Access Project ID](#steps-to-access-project-id)

### 1. Log into watsonx<a name="log-in-to-watsonx"></a>
---
Next, follow this link to log into watsonx: https://dataplatform.cloud.ibm.com/wx/home?context=wx

Please accept the Terms & Conditions!

### 2. Check that you are in the right instance<a name="check-instance"></a>
---
You should now be taken to the watsonx home screen. Check at the top right that you are in the right instance. If it does not show the right name of the instance, you can select it in the drop-down. For the entirety of the bootcamp, you will be working in that same instance!

If you do not know your instance, go to your techzone reservations list https://techzone.ibm.com/my/reservations. Look for your recently created reservation and click on "Open this environment". Scroll down and look for a reservation name that looks similar to this:  ITZ-WATSONX-21. 

**Note:** The instance at the top right tends to change to your default personal account every time you switch/go back to a new page. Thus, it's always good to check the top right corner every time you switch to a new page.

![check-right-instance](assets/check-right-instance.png)

### 3. Create a new project<a name="new-project"></a>
---
Now, we can go ahead and create a new project. 

In the **Projects** section, click the "+" symbol to create a new project.
 
Or, use the link here to trigger a [New Project](https://dataplatform.cloud.ibm.com/projects/new-project?context=wx) creation.

![create-new-project](assets/create-new-project.png)

Enter a **unique name** for your project, include both your first and last name and any other information you would like.

![unique-name](assets/unique-name.png)

### Cloud Object Storage (COS)
It is likely there is also already a Cloud Object Storage instance selected for you, with a name that starts with "itzcos-..." If so, you don't have to do anything! 

Otherwise, you may be prompted to select from multiple instances. Please consult with your bootcamp lead which COS instance to select.

![select-instance](assets/select-instance.png)

### Click Create
Now, click Create. It may take a few seconds to officially be created.

### 4. Associate the correct runtime instance<a name="runtime-instance"></a>
---
With the project created, you should be directed to the project home page. Select the "Manage" tab.

Click on "Services and Integrations" in the left sidebar. Then, click on "Associate service."

![manage-tab](assets/manage-tab.png)

Select the service listed with "Type" = "watsonx.ai Runtime" and click **Associate**. 

![select-runtime-service](assets/select-runtime-service.png)

**Note:** If you can't find the service, remove all filters from the "Locations" dropdown. If you see 2+ Watson Machine Learning services, select the one where "Group" = the same *environment* name of the instance. The *environment* name can be found on https://techzone.ibm.com/my/reservations. 

6. Click on the **hamburger menu (☰)** in the top-left corner and select **"Access (IAM)"**.  

   ![Access IAM](/usecase-setup/environment-setup/assets/iam-access.png)  

7. In the left-hand menu, click on **"API Keys"**.  

   ![API Keys Menu](/usecase-setup/environment-setup/assets/click-api-key.png)  

8. Click **"Create"** to generate a new API key.  

   ![API Key Page](/usecase-setup/environment-setup/assets/create-api-key.png)  

9. Enter a name for your API key and click **"Create"**.  

   ![Create Api key](/usecase-setup/environment-setup/assets/api-key-details.png)  

10. **Copy your API key** and save it in a secure location. You will need it in later steps.  

    ![Api Key Show](/usecase-setup/environment-setup/assets/copy-api-key.png)  



## Steps to Access Project ID

1. Click on the hamburger menu (three horizontal lines) located at the top-left corner of the screen, You will see view all project options under Project section.
   
   ![Hamburger Menu](/usecase-setup/environment-setup/assets/hamburger_click.png) 

2. Now you will be redirected to list of Projects, find and click on the project you want to work with.

   ![Project Selection](/usecase-setup/environment-setup/assets/choose_project.png)  

3. Once inside the project view, click on the "Manage Options" button.

4. After clicking "Manage Options", the Project ID will be displayed copy Project ID for further use.

   ![Project ID](/usecase-setup/environment-setup/assets/click_manage_get_projectId.png) 

Now that we have created both the Project ID and the API Key, we will proceed with the creation of our agents.
