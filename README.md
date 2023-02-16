![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)



### Python Project

# Hub
### It is the first European platform entirely dedicated to the buying and selling of fine wines and spirits for individuals and traders.
![devises reponsive](/asset/images/iu.de.png)

* The file that contains my code is called `run.py`
* The spreadsheet to which you are linked is known as "usersdata."
* The Heroku link is https://wine-hub.herokuapp.com/.
* The application has two steps:
    - Enter your data.
    - Calculate the best membership (MBS) plan for you,
    which can be:
   - `Standard` for small businesses
   - `Advance` for medium-sized businesses
   - `Elite` for wine brokers and large businesses


# How it works..
 It requires some general data to start, such as your name, date of birth, your residence, the amount you spent on a week, a category of spirits or wines, and the grape varieties.

Once the user has inserted all the data, we will calculate the best MBS for the user.
MBS stands for membership plan.
The data that we are going to target is the weekly outcome, called "Amount" on the spreadsheet.

After the users insert the amount, it will be calculated in our MBS, and depending on the results, it will give the best plan for the users.

The MBS is divided into three slots.
- `Standard` to all users with an output of £/€ 0 to 350.
- `Advance` to all users with an outcome of 351 to £/€ 700.
- `Elite` to all users with a weekly output greater than £/€ 701.


# To the application.
This is the first section of the project where the steps are explained.

  -- ![devises reponsive](/asset/images/present.app.png)

The applicant can proceed with the application once it has been prepared.

--  ![devises reponsive](/asset/images/app.start.png)

Then, we will extract the amount used and calculate the MBS.
In this case, the customer has been elected for an Elite MBS.

-- ![devises reponsive](/asset/images/mbs.png)

## Future Features

* Allow users to compare various MBS.
* Allow users to insert only their name and surname to get to their data after being registered.
* Have more information about the MBS.
* Implement a bigger explanation for the MBS.

## Testing

I have manually tested this project by doing the following

- Passed the code through a PEP8 linter and confirmed there are no problems

- Once you have inserted the data, it will be sent to the spreadsheet.
Following the format assigned previously.

   ![devises reponsive](/asset/images/info.sheet.png)

- After the data has been collected, it will calculate the MBS and assign the slots: standard, advance, and elite.

   ![devises reponsive](/asset/images/mbs.sheets.png)

   - In this case, the user who has been elected has Standard MBS.

      ![devises reponsive](/asset/images/mbs.calc.png)


- Now let's go through the invalid data insert.
   ### The first section
   ![devises reponsive](/asset/images/testing.png)
   
  - If the user will not insert the surname, they will be 
    asked to try one more time.
  - If the user will not insert the date of birth following 
   the format that has been given,
   As shown in the previous screenshot, it will prompt you to try again.

  ### Second section

   ![devises reponsive](/asset/images/testing1.png)

    - If the user attempts to insert a word or series of words, an error message will be displayed.
    It will be prompted to enter a valid amount; this also applies if a negative number is provided, as shown in the screenshot.




### Third part
  - As a business perspective, I left some data easy to skip, such as residence, category, and favorite style, because since we are collecting data for a future membership plan, we can already remove users who will not be interested or try to waste our time.
  
  ![devises reponsive](/asset/images/testing2.png)    



- My local terminal and the Code Institute Heroku terminal were both tested.

## Bugs

  Solved Bugs

- I had some problems with the Python format when I first started the project, adding too much space through the function and loop, which I fixed by removing the extra spaces.


- My validations for the function calculate_mbs_usr_amount were incorrect because I was unable to extrac the required data.

    
       The way I resolved my issue was just by adding the
        `(data[0], data[3])`
        to the terminal, and it worked.

 ### Remaining Bugs
  * There are no bugs left.       


## Validator Testing
  - PEP8
      -  No errors were returned from PEPSonline.com.


      ![devises reponsive](asset/images/pep8c.png)


## Deployment

This project was deployed using the Code Institute's mock terminal for Heroku.

* Steps for deployment:
  - Fork or clone this repository
  - Create a new Heroku app
  - Set buildbacks to `Python` and `NodeJS` in that order.
  - Config Var use `CREDS` as port and the `creds.jason` file as key.
  - Add a new key called `PORT` and a new key `8000`.
  - Connect the Heroku app to your GitHub.
  - Once connected, choose the repository that you would like to use to connect.
  - Link the Heroku app to the repository
  - Click on choose Manual Deploy


  # Credits
   * Code Institute for the deployment terminal