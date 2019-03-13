# simple-data-diff
Simple project to help verify data in collumns

This is a incomplete project.

The idea is that you pass filenames as input, they should be CSV or something like that. Because the idea is that you can pass as argument the delimiter and the columns that should be used as keys for comparing elements. Also it should be passed the argument for selecting the operation 'diff', 'intersection', etc.

The output is the number of instances according to operation and the elements of the operation slected.

This project is basicaly a wrapper around set operatins in order to do simple dataset comparisons, without having to use tools like pandas. And focusing on specific types of files.