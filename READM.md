<img align="right" src="https://user-images.githubusercontent.com/47650058/188333432-c3aeb596-5090-4b74-9a5e-f5957bfb6acf.png" alt="DiscordDB" height="200" width="200">

# TDPlanner
> TDPlanner is a To Do List application which uses mathematical calculations to plan the order of your day.

TDPlanner uses basic mathematics to sort the order of which the tasks listed should be done. It even provides a visual representation of the graph using the `matplotlib` package in Python.

---

![image](https://user-images.githubusercontent.com/47650058/188777357-a02f5d56-0516-48e7-b759-b87cd0034592.png)

## Usage
Using the application is as easy as using any other TO DO List Application.
- Add Task: Add a task to the to do list.
- Mark As Complete: Mark a task in the to do list as complete (remove the task from the to do list)
- Reset Tasks: Deletes all concurrent tasks in the to do list and starts a fresh to do list.

*Tasks will not reset if you close the tab because they are locally stored in a cache database. Multiple tasks can have duplicate names without an issue because there is a task ID system set in place.*

## Settings
I have included weightage settings just in case for people who prefer doing urgent tasks more than important tasks and vice versa. The settings will be reset to equal weightage every time the application is opened.

## Calculations and Visualizations
TDPlanner uses `matplotlib` to display the graph and show the user which tasks are being chosen to be first and why. <br>
On a grid (x axis being urgency values and y axis being importance values of the tasks), we can lay out each of the tasks as a point on the grid. Based on the importance weightage and urgence weightage, we can determine the slope of a line that we are going to use to sweep through until we reach the origin picking the tasks we have to do in order. <br>
Here is an example displayed in desmos (graphing calculator) to help you visualize:
![mathrepresentation](https://user-images.githubusercontent.com/47650058/188779468-553bb0f6-6f30-42c2-a84f-d0e1e8480b9b.gif)
In the example above, the slope of the line was -1 because the weightage of the 2 were the same. But, if the weightages were to be altered, the sweep would work the same except the slope of the line would have been the only change. In the scenario where multiple points hit the sweeping line at the same time, we put the most urgent tasks first.

According to the example above with equal weightage, the tasks we are supposed to be doing follow the order of: {(9,9), (6,7), (5,8), (8,2)}. <br>
But let's say you gave more weightage to urgency instead of importance; if you decrease the importance weightage and increase the urgency weightage enough, (8,2) will come further ahead in the order of the to do list.

With all the visualization, I came to a simple conclusion that each task could be sorted by a singular value which is the sum of the values multiplied by the weights, or in other terms, `importance_weight*importance_value + urgence_weight*urgence_value`. Using this to calculate the value a task holds, functions the same as sweeping through the graph and I only used the graph sweeping to create a better visualization of what happens behind the scenes.

## BUGS
- [ ] Matplotlib is using agg which is a non-GUI backend which doesn't allow the application to show the figures.
- [ ] Matplotlib takes a long time to build the font cache
- [ ] Icon and application name doesn't show

## TODO
- [ ] Add the lines to the Matplotlib figures that explain the mathematics.
- [ ] Add installation instructions and desktop file configuration.
- [ ] Create wiki, project and INSTALL txt file.

---

TDPlanner (To Do Planner) is written in Python 3.9 and uses TKinter GUI to function. TDPlanner uses this TKinter [dark theme](https://github.com/formazione/tkinter_dark_theme) script from [Formazione](https://github.com/formazione) for the GUI.
