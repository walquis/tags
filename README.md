# Tags - A silly little Python webapp for CodePlatoon git classes

The tags webapp lists tags and stores more tags.

It displays an image based on info in a config file.

It knows about development, uat, and production environments.

It uses a SQLite database.

It uses a primitive (and rather obsolete) ORM called [Flask-Orator](https://github.com/sdispater/flask-orator).

This app is so barebones and unfinished that it begs for changes.  Using git, you will collaborate with your team to make it better.

## Environment assumptions

- You have a Python3 installed that is recent enough to have the "-m" option for configuring virtual environments.

- You have a [GitHub](https://github.com) account.

## Set up and run the webapp

Fork the Tags repo from https://github.com/walquis/tags.

Run these commands in a Terminal session:
```bash
$ cd # Start from your home directory
$ mkdir src; cd src  # Or cd to wherever you keep code projects
$ git clone https://github.com/<yourlogin>/tags # Clone your fork
# Or use ssh protocol...  $ git clone git@github.com:<yourlogin>/tags
$ cd tags
$ mkdir ../shared  # In case you want to share config across releases
$ cp config.yml.sample ../shared/config.yml
$ python3 -m venv venv  # Make a virtual env in the "venv" directory
$ source venv/bin/activate  # Enter your virtual env
$ pip install -r requirements.txt  # Populate current virtual env with packages
$ python bin/load_schema.py   # Init your DB structure. Assumes FLASK_ENV=development
$ python bin/seed.py   # Add data to your DB.  Assumes FLASK_ENV=development
$ bin/run-flask-webserver.sh  # Assumes FLASK_ENV=development
```
Now visit http://localhost:5555 in your browser.

## A Simulated Project for Collaborating

*Goal*: Your team will exercise your new-found knowledge of git by making changes to this code base.  Below are some suggested tasks, solutions, hints for viewing diffs, and a typical task workflow.  As your team begins to deliver completed tasks, you will experience the typical challenges associated with working in parallel on a code base--and practice using git to solve them.  To help keep things simple, feel free to use the sample solutions (see below), rather than coming up with an original implementation; the goal is not primarily to learn new code, but to gain experience using git for team collaboration.

The ```master``` branch has a working version of the app, runnable as described above.

*Objective*: Keep the app working as you deliver each change to ```master```. &nbsp;&nbsp;Don't "break the build"!

### Hints for viewing changes with diff'ing commands:
1. For each task below, a sample solution lives on a corresponding branch.  Feel free to look at the solution branch (or just use it) for accomplishing the task.  For instance, you can view the "Add a config parameter ..." solution by git-diff'ing its ```more_config``` solution branch against master:
```
$ git checkout more_config
$ git diff master
```
2. Because (a) all the sample solutions branch from the same point on master, and (b) master will be moving as changes come in, you may want to create a branch to use as a label purely for diff'ing purposes:
```
$ git checkout master
$ git branch master-mark
$ git checkout view_template
$ git diff master-mark
```
3. For some branch comparisons, you may desire to exclude one or more files from the ```git diff``` output. For instance, no need to see the entire jquery file when looking at ```better_delete_route```...)
```
$ git checkout better_delete_route
$ git diff master -- . ':(exclude)*jquery*.js'
```
4. Consider using ```git show``` if you just want to see a single commit's worth of diffs.  You can do that from any branch in any state--no need to (for instance) get your workspace to a clean state, checkout a particular branch locally and git diff.
```
$ git show origin/view_template
```
Note that ```git show``` only shows diffs for the commit you specify--not for the whole branch.

Both *Round One* and *Round Two* solutions are branched from the initial ```master``` branch.  However, you may want to tackle the more-complex *Round Two* tasks after you've completed *Round One*.

Making changes:  You can view the solutions as described above and then make the changes to your workspace "manually" by typing or copy-pasting, or you may find it simpler to merge the solution branch over to the branch you're on.


### Getting Started on the Project

1. *Someone on your team* - Fork this repo and grant read/write access to the rest of the team, who will each clone to their local machine.  NOTE: Just to keep things simple and focused on git (as opposed to github), we will not be using any Github workflow operations apart from the one fork operation.
1. *Whole Team* - Take a look at the Round One tasks below, and decide who will tackle each task.  It will be useful to ```git diff``` the branches with sample solutions, as demonstrated above.
1. *Each Member* - Begin implementing your assigned task.  You may want to work on a non-master branch.
1. *Each Member* - As you finish a task, merge it to ```master``` and ```git push```.  (NOTE: Before merging to master, it's a good idea to Do a ```git pull``` of ```master``` first, just in case changes have been delivered since you last branched from ```master```. In that case, you will need to merge before delivering!)  Oh, and after delivering to ```master```, and before pushing to the shared team repo, don't forget to make sure the website still works.

### Round One Tasks
- ```view_template``` - Move the HTML into a Jinja2 template
- ```stylesheet``` - Move CSS into a stylesheet
- ```tag_input_first``` - Move the tag input above the tag list
- ```more_config``` - Add a config parameter to set title to 'Hello Sol!'
- ```delete_route``` - Add a delete route, to where clicking on a tag deletes it
- ```about_page_with_nav``` - Add an "about" page, with navigation menu

### Round Two Tasks
- ```layout``` - Add a Jinja layout
- ```better_delete_route``` - Use a DELETE method (and some Javascript/jQuery) to delete tags
- ```peewee``` - Switch the ORM from Flask-Orator to Peewee (if you really want to bite off a big chunk!)

### A Possible Workflow
1. ```git checkout master``` - The branch where your team will rendezvous with changes.
1. ```git pull origin master``` - Catch your local master up with latest changes from your team.
1. ```git checkout -b mytask``` - Create and go to a new task branch from master.
1. ```git merge origin/stylesheet``` - Merge a solution (e.g. stylesheet) over to ```mytask``` (resolving any conflicts).
1. ```git checkout master``` - Go to master in prep for bringing your stuff in.
1. ```git pull origin master``` (in case more changes have been pushed by teammates).
1. (If there *are* more changes, go back to mytask and merge 'em in.  Then tell your team to hold off now, it's your turn!).
1. ```git merge mytask``` - Assuming you're back on master at this point.
1. ```git push origin master``` - Share your scintillating creativity with your team.
