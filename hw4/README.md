<h1>This file details the layout of this program.<h1>
<p>The code beings with looping through the tsv files and seperating the
 domains from the rest of the files. There is then a function defined that makes plot graphs and checks for already made pngs within the png_folders directory. If there is no copy of the png, it is then saved into the directory, otherwise, it skips over the files and goes to the next. <p>

 <p>The for loop then traverses each domain and obtains the forward DNS, checks if the DNS returned succesful and then repeats a similar task for the reverse DNS. It then creates nodes that are attached to edges,this part of the code was contributed by Zach Chatman. It then calls the make plot function to create graphs of DNS. <p>