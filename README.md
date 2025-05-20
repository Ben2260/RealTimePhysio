# Real-Time Feature Analysis:
### Table of Contents:
>  **1. Overview**
>> - Terminology
>> - Organizational Structure
>> - Current state of the program
>> - General recomendations
>
> **2. Downloading required packages**
>> - Installing {Multiprocesingpandas} {numpy} {time} {socket} {Neurokit 2} {Python 3.12}
>> - Important links to 3rd party softwares
>
> **3. Avaliable Functionality**
>> - [EDA](#EDA)
>> - RSP
>
> **4. Examples**
>> - Running the Main
>> - Using Device emulator
>> - Understanding TCP
>> - Understanding multi procesing
>
> **5. Future development**
>> - Design & Theory
>> - GTL Lock & limitations
>> - Making new functions
### Overview:

> ##### <u>*Code Terminology:*</u>
>> - **CPU**: This is shorthand for the Central Processing Unit; you can think of it as the brain of your computer. It is responsible for evaluating every program, subprocess, and YouTube video. However, its primary goal is the evaluation of a program, it's best to think of the CPU as a speedy calculator; it will do the calculation really fast, but it's up to something else to decide how the returned value is used. 
>> - **Multi-Procesing:** Multiprocesing is, as the name implies, a way for programers to preform multiple mathmatical operations at the same time. Where a program normally executes code line by line, a program utilizing multiprocesing is able to distribute a single process to each core, allowing for 2 lines of code to be executed at the same time.
>> - **Multi-Threading:** TBD
>> - **CPU up time:** The time spent activley computing by the CPU over a given time period, this is usually measured in percent. This metric is usefull because we want to make this as high as possible without reaching % > 90% where we usually beguin to see the CPU bottel neck the program
>> - **Memory management:** The process of controlling and coordinating computer memory, including assigning memory blocks to various programs, tracking memory usage, and reclaiming memory when it is no longer needed to ensure efficient and optimal use of memory resources.
>> - **Memory blocks:** A temporary storage area in memory used to hold data while it is being transferred between two locations or devices. Buffers help in smoothing out the differences in the processing speeds of different components.
>> - **Sliding window:** A technique used in algorithms where a window of a fixed size moves over a dataset to process or analyze smaller segments of the data sequentially. This is useful in tasks such as signal processing and time-series analysis.
>> - **Stride:** The step size or interval at which the sliding window moves across the dataset. A smaller stride leads to more overlap between windows, providing higher resolution but increased computational load, while a larger stride results in less overlap and reduced computational load.
>> Still confused? Here are some resources for learning more about these concepts:
>>
>> [![Click Me](https://media.geeksforgeeks.org/gfg-gg-logo.svg)](https://www.geeksforgeeks.org/)  
<table style="border: 3px solid black; border-collapse: collapse;">
  <tr>
    <th style="border: 3px solid black;">Link</th>
    <th style="border: 3px solid black;">Description</th>
  </tr>
  <tr>
    <td style="border: 3px solid black;">
      <img src="https://vectorseek.com/wp-content/uploads/2021/02/IBM-Logo-Vector.jpg" width="100">
    </td>
    <td style="border: 3px solid black;">IBM Logo</td>
  </tr>
</table>


> ##### <u>*Organizational Structure*</u>
>> The naming structure of my file system is made up of 3 sections and well be using the example above as we go through it:
>> 1. <u>*Stage*</u>: The first set of square brakets represents the stage of the script.
>>> - In our example this would be:
>>>> **[M]**[Anlys]
>>>> 
>>>> **[M]**...
>>>> 
>>> - *[M]*: Denotes a <u>MAIN</u> file; This file has been tested and debuged, it has comments and is ready for use.
>>> - *[T]*: Denotes a <u>TEST</u> file; This file is in the process of being debuged and is in need of comments.
>>> - *[uE]*: Denotes a User <u>EXAMPLE</u> file; This file is supposed to show and aid the user in building their functions that can attach to the system. As well as highligh the core ideas and theorys used in the origional development of the system.
>>> - *[V]*: Denotes a <u>VARIABLE</u> file; This file includes old code I used for reference when developing the system.
>>>
>>
>> 2. <u>*Core Purpose*</u>: The second set of square brakets represents the core purpose of the script.
>>> - In our example this would be:
>>>> [M]**[Anlys]**
>>>>
>>>> ...**[Anlys]**...
>>> - *[3rd]*: Denotes a <u>3rd PARTY</u> file; Required but not native to any library, or was purchased by the lab.
>>> - *[Feat]*: Denotes a <u>FEATURE</u> file; A feature exstraction function, it can be changed but currently works and is avaliable for user use.
>>> - *[main]*: Dentotes a <u>LEADER</u> file; The Main or Core file, if nothing has changed you should be able to just run this file and use the project as intended
>>> - *[Com]*: Denotes a <u>COMMUNICATION</u> file; Focuses on connecting with some other program inorder to collect data and re-rout it to the system
>>> - *[zOld]*: Denoted an <u>ORIGIONAL</u> file; Old file that isnt used but if you are trying to developsomething new it might be usesfull to see other things that I've tried and failed but in the future might work as updates to libraries are implimented.
>> 3. <u>*General*</u>: The remaining portion of the file name is used to describe the file itself, this allows us to have multiple of any one file name as it might exists in many diffrent forms. Since this is just additional info there arent any specific identefires to adhear too.
> 
> ##### <u>*Current state of the program:*</u>
>>> - Description: TBD
>>> - System ability: TBD
>>> - Avalable Fetures: TBD
> 
> ##### <u>*General recomendations:*</u>
>> To be filled out at a later date, as project reaches completion.
## Setting Up real time
#### Automatically: Anaconda Environment

> ##### *Downloading and Setting Up Anaconda:*
>> 1. Visit the [Anaconda official website](https://www.anaconda.com/) and download the latest version for your operating system.
>> 2. Run the installer and follow the setup instructions, ensuring you add Anaconda to your system's PATH.
>> 3. Open the Anaconda Navigator or use the terminal to verify the installation:
    ```bash
    conda --version
    ```
>> 4. Create a new environment for real-time processing:
    ```bash
    conda create --name RealTime python=3.9```
>> 5. Activate the environment:
    ```bash
    conda activate RealTime
    ```
>> 6. Install the required libraries:
    *** ''' bash
    conda install numpy pandas neurokit2 sockets multiprocessing
    
>> 7. Verify the installation:
    ```bash
    conda list
    ```
>> Congrats! Your Anaconda environment is now set up.


#### Manually: Downloading required packages

> ##### *Installing libraries:*
>> There are only 5 required Python libraries to run this program:
>> - [Numpy](https://numpy.org/)
>> - [Pandas](https://pandas.pydata.org/)
>> - [Neurokit 2](https://neuropsychology.github.io/NeuroKit/)
>> - [Sockets](https://docs.python.org/3/library/socket.html)
>> - [Multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
>>
>> Links for which are attached above. Additionally, as a reminder, to download these files:
>> 1. Open your computer's Terminal by typing "Terminal" in the search bar.
>> 2. Type the following command:
    ```bash
    pip install numpy pandas neurokit2 sockets multiprocessing
    ```
>> 3. Verify that the packages have been downloaded:
    ```bash
    pip show numpy pandas neurokit2 sockets multiprocessing
    ```
>> Congrats! You can now run the rest of the code discussed below!!
> >
>
>
>
> ##### *Usefullant links to 3rd party softwares:*
>> - Numpy:  

### Avaliable Functionality:

> ##### *EDA:*
> TBD
> ##### *RSP|*
> TBD
### Examples:

> ##### *Running the Main:*
> TBD
> ##### *Using Device emulator*
> TBD
> ##### *Using TCP*
> TBD
> ##### *Using multi-procesing*
> TBD
### Examples:

> ##### *Design & Theory*
> TBD
> ##### *GTL Lock & limitations*
> TBD
> ##### *Making new functions*
> TBD
