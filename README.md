<!DOCTYPE html>
<html lang="en">
<body>
<h1>Real-Time Feature Analysis</h1>
<h2>Table of Contents</h2>
<ul>
    <li><strong>1. Overview</strong>
        <ul>
            <li><a href="#Terminology">Terminology</a></li>
            <li><a href="#Organizational_Structure">Organizational Structure</a></li>
            <li><a href="#Current_State">Current state of the program</a></li>
            <li><a href="#General_Recommendations">General recommendations</a></li>
        </ul>
    </li>
    <li><strong>2. Downloading Required Packages</strong>
        <ul>
            <li><a href="#Installing_Packages">Installing Multiprocessing, Pandas, NumPy, Time, Socket, Neurokit 2, Python 3.12</a></li>
            <li><a href="#Third_Party_Links">Important links to 3rd party software</a></li>
        </ul>
    </li>
    <li><strong>3. Available Functionality</strong>
        <ul>
            <li><a href="#EDA">EDA</a></li>
            <li><a href="#RSP">RSP</a></li>
        </ul>
    </li>
    <li><strong>4. Examples</strong>
        <ul>
            <li><a href="#Running_Main">Running the Main</a></li>
            <li><a href="#Device_Emulator">Using Device Emulator</a></li>
            <li><a href="#Understanding_TCP">Understanding TCP</a></li>
            <li><a href="#Multiprocessing">Understanding Multiprocessing</a></li>
        </ul>
    </li>
    <li><strong>5. Future Development</strong>
        <ul>
            <li><a href="#Design_Theory">Design & Theory</a></li>
            <li><a href="#GTL_Lock_Limitations">GTL Lock & Limitations</a></li>
            <li><a href="#New_Functions">Making New Functions</a></li>
        </ul>
    </li>
</ul>
<h2>Overview</h2>
<h4><u>Code Terminology:</u></h4>
<ul>
    <li><strong>CPU:</strong> The brain of your computer, responsible for evaluating programs and processes.</li>
    <li><strong>Multi-Processing:</strong> A method that enables multiple mathematical operations to be performed simultaneously.</li>
    <li><strong>Multi-Threading:</strong> TBD</li>
    <li><strong>CPU Up Time:</strong> The percentage of time the CPU is actively computing within a given period.</li>
    <li><strong>Memory Management:</strong> The process of allocating and optimizing memory resources efficiently.</li>
    <li><strong>Memory Blocks:</strong> Temporary storage areas used to transfer data between locations or devices.</li>
    <li><strong>Sliding Window:</strong> A technique for processing smaller segments of a dataset sequentially.</li>
    <li><strong>Stride:</strong> The step size at which a sliding window moves across a dataset.</li>
</ul>
<h4>Resources</h4>
<p>Still confused? Here are some resources for learning more about these concepts:</p>
<ul>
    <li><a href="https://www.geeksforgeeks.org/">GeeksforGeeks</a></li>
    <li><a href="https://www.ibm.com/docs/en">IBM Documentation</a></li>
</ul>
<h4><u>Organizational Structure</u></h4>
<p>The naming structure of my file system consists of three sections:</p>
<h5>1. Stage</h5>
<ul>
    <li><strong>[M]:</strong> <u>Main File</u> – tested, debugged, and ready for use.</li>
    <li><strong>[T]:</strong> <u>Test File</u> – undergoing debugging and lacks comments.</li>
    <li><strong>[uE]:</strong> <u>User Example File</u> – aids users in creating new functions.</li>
    <li><strong>[V]:</strong> <u>Variable File</u> – contains old code used for reference.</li>
    <li><strong>Example:</strong> A common file type you should familiarize yourself with are the feature extraction files. These serve as examples and existing implementations of current feature extraction methods that can either be built upon or used directly. The example we will be using below is the basic Respiration feature extraction method; since this method is complete, it is in stage [M].</li>
    <div style="display: flex; justify-content: center;">
        <img src="https://github.com/Ben2260/RealTimePhysio/raw/main/Project%201%3A%20Real%20Time/Prefix%20name%20file%20Example.png" 
             alt="Prefix Name File Example" 
             style="width: 50%; height: auto;">
    </div>
</ul>
<h5>2. Core Purpose</h5>
<ul>
    <li><strong>[3rd]:</strong> <u>Third-Party</u> file – external or purchased library.</li>
    <li><strong>[Feat]:</strong> <u>Feature</u> file – functional and available for user use.</li>
    <li><strong>[main]:</strong> <u>Leader</u> file – core file; meant to be executed directly.</li>
    <li><strong>[Com]:</strong> <u>Communication</u> file – handles data collection and routing.</li>
    <li><strong>[zOld]:</strong> <u>Original</u> file – deprecated but may be useful for development.</li>
    <li><strong>Example:</strong> A common file type you should familiarize yourself with are the feature extraction files. These serve as examples and existing implementations of current feature extraction methods that can either be built upon or used directly. The example we will be using below is the basic Respiration feature extraction method; since this method is complete, it is in stage [M].</li>
    <div style="display: flex; justify-content: center;">
        <img src="https://github.com/Ben2260/RealTimePhysio/blob/main/Project%201%3A%20Real%20Time/Core%20name%20file%20Example.png" 
             alt="Prefix Name File Example" 
             style="width: 50%; height: auto;">
    </div>
</ul>
<h5>3. General</h5>
<p>The remaining portion of the filename describes the file itself, allowing multiple versions of similar files to exist.</p>
        <li><strong>Example:</strong> A common file type you should familiarize yourself with are the feature extraction files. These serve as examples and existing implementations of current feature extraction methods that can either be built upon or used directly. The example we will be using below is the basic Respiration feature extraction method; since this method is complete, it is in stage [M].</li>
    <div style="display: flex; justify-content: center;">
        <img src="https://github.com/Ben2260/RealTimePhysio/blob/main/Project%201%3A%20Real%20Time/Generic%20name%20file%20Example.png" 
             alt="Prefix Name File Example" 
             style="width: 50%; height: auto;">
    </div>
<h4><u>Current State of the Program:</u></h4>
<ul>
    <li><strong>Description:</strong> TBD</li>
    <li><strong>System Ability:</strong> TBD</li>
    <li><strong>Available Features:</strong> TBD</li>
</ul>
<h4><u>General Recommendations:</u></h4>
<p>To be filled out upon project completion.</p>
<h3>Setting Up Real-Time</h3>
<h4>Automatically: Anaconda Environment</h4>
<h2 id="Overview">Download & Set Up</h2>
    <h3>Easy: Anaconda Environment</h3>
    <p><strong>Downloading and Setting Up Anaconda:</strong></p>
    <ol>
        <li>Visit <a href="https://www.anaconda.com/">Anaconda Website</a> and download the latest version.</li>
        <li>Run the installer and follow setup instructions.</li>
        <li>Verify installation:
            <pre>conda --version</pre>
        </li>
        <li>Create a new environment:
            <pre>conda create --name RealTime python=3.9</pre>
        </li>
        <li>Activate the environment:
            <pre>conda activate RealTime</pre>
        </li>
        <li>Install required libraries:
            <pre>conda install numpy pandas neurokit2 sockets multiprocessing</pre>
        </li>
        <li>Verify installation:
            <pre>conda list</pre>
        </li>
    </ol>
    <h3>Manually: Downloading Required Packages</h3>
    <p><strong>Installing Libraries:</strong></p>
    <ul>
        <li><a href="https://numpy.org/">NumPy</a></li>
        <li><a href="https://pandas.pydata.org/">Pandas</a></li>
        <li><a href="https://neuropsychology.github.io/NeuroKit/">Neurokit 2</a></li>
        <li><a href="https://docs.python.org/3/library/socket.html">Sockets</a></li>
        <li><a href="https://docs.python.org/3/library/multiprocessing.html">Multiprocessing</a></li>
    </ul>
    <ol>
        <li>Open your Terminal.</li>
        <li>Run:
            <pre>pip install numpy pandas neurokit2 sockets multiprocessing</pre>
        </li>
        <li>Verify installation:
            <pre>pip show numpy pandas neurokit2 sockets multiprocessing</pre>
        </li>
    </ol>

</body>
</html>
