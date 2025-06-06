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
            <li><a href="#Resources">Additional Resources</a></li>
        </ul>
    </li>
    <li><strong>2. Setting Up Real-Time</strong>
        <ul>
            <li><a href="#Easy_Anaconda_Environment">Easy: Anaconda Environment</a></li>
            <li><a href="#Third_Party_Links">Manual: Downloading Required Packages</a></li>
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
<h3 id="Terminology"><u>Code Terminology:</u></h3>
<ul>
    <li><strong>CPU:</strong> The brain of your computer, responsible for evaluating programs and processes.</li>
    <li><strong>Multi-Processing:</strong> A method that enables multiple mathematical operations to be performed simultaneously.</li>
    <li><strong>Multi-Threading:</strong> A technique that allows a CPU to execute multiple threads concurrently, improving efficiency and responsiveness by enabling tasks to run in parallel.</li>    
    <li><strong>CPU Up Time:</strong> The percentage of time the CPU is actively computing within a given period.</li>
    <li><strong>Memory Management:</strong> The process of allocating and optimizing memory resources efficiently.</li>
    <li><strong>Memory Blocks:</strong> Temporary storage areas used to transfer data between locations or devices.</li>
    <li><strong>Sliding Window:</strong> A technique for processing smaller segments of a dataset sequentially.</li>
    <li><strong>Stride:</strong> The step size at which a sliding window moves across a dataset.</li>
</ul>
    
<h3 id="Organizational_Structure"><u>Organizational Structure:</u></h3>
    <p>The naming structure of my file system consists of three sections:</p>
    <h4>1. Prefix</h4>
    <ul>
        <li><strong>[M]:</strong> <u>Main File</u> – tested, debugged, and ready for use.</li>
        <li><strong>[T]:</strong> <u>Test File</u> – undergoing debugging and lacks comments.</li>
        <li><strong>[uE]:</strong> <u>User Example File</u> – aids users in creating new functions.</li>
        <li><strong>[V]:</strong> <u>Variable File</u> – contains old code used for reference.</li>
        <br>
        <li><strong>Example:</strong> A common file type you should familiarize yourself with are the feature extraction files. These serve as examples and existing implementations of current feature extraction methods that can either be built upon or used directly. The example we will be using below is the basic Respiration feature extraction method; since this method is complete, it is in stage [M] and is displayed bellow.</li>
        <div style="display: flex; justify-content: center;">
            <img src="https://github.com/Ben2260/RealTimePhysio/raw/main/Project%201%3A%20Real%20Time/Prefix%20name%20file%20Example.png" 
                 alt="Prefix Name File Example" 
                 style="width: 50%; height: auto;">
        </div>
    </ul>
    <h4>2. Core Purpose</h4>
    <ul>
        <li><strong>[3rd]:</strong> <u>Third-Party</u> file – external or purchased library.</li>
        <li><strong>[Feat]:</strong> <u>Feature</u> file – functional and available for user use.</li>
        <li><strong>[main]:</strong> <u>Leader</u> file – core file; meant to be executed directly.</li>
        <li><strong>[Com]:</strong> <u>Communication</u> file – handles data collection and routing.</li>
        <li><strong>[zOld]:</strong> <u>Original</u> file – deprecated but may be useful for development.</li>
        <br>
        <li><strong>Example:</strong> Basic Respiration feature extraction method; since this file is a feature exstraction method, it has core purpose [Feat] and is displayed bellow.</li>
        <div style="display: flex; justify-content: center;">
            <img src="https://github.com/Ben2260/RealTimePhysio/blob/main/Project%201%3A%20Real%20Time/Core%20name%20file%20Example.png" 
                 alt="Prefix Name File Example" 
                 style="width: 50%; height: auto;">
        </div>
        </ul>
    <h4>3. General</h4>
    <ul>
    <p>The remaining portion of the filename describes the file itself, allowing multiple versions of similar files to exist.</p>
            <br>
            <li><strong>Example:</strong> Basic Respiration feature extraction method; Since this method is representative of a basic respiration feature exstraction methodology it is described as seen bellow.</li>
        <div style="display: flex; justify-content: center;">
            <img src="https://github.com/Ben2260/RealTimePhysio/blob/main/Project%201%3A%20Real%20Time/Generic%20name%20file%20Example.png" 
                 alt="Prefix Name File Example" 
                 style="width: 50%; height: auto;">
        </div>
</ul>
<h3 id="Current_State"><u>Current State of the Program:</u></h3>
<ul>
    <li><strong>Description:</strong> This program is designed to provide researchers with a methodology for real-time collection and analysis of physiological features from one or more participants. By utilizing multiprocessing, the system efficiently extracts, distributes, examines, and displays predefined physiological features from incoming data streams. This allows researchers to process multiple sources of biometric data simultaneously without significant delays or bottlenecks. A key component of this system is its use of TCP (Transmission Control Protocol) and buffer memory spaces to manage the movement of data between processes and objects. These mechanisms ensure smooth data transmission and prevent loss of critical information, even when handling multiple concurrent streams. While the system is structurally sound and provides a strong foundation for future development, its functionality remains limited due to the number of tested and approved feature extraction methods. As of May 5, 2025, only the Respiration (RSP) feature extraction using Neurokit 2 has undergone full validation and testing. Work has begun on Electrodermal Activity (EDA), but it remains unfinished. However, because of the modular nature of this framework, completing EDA—and integrating additional features—is relatively straightforward. Included in this documentation is a detailed guide on how users can develop and implement their own feature extraction methods, making it possible to tailor the system to specific research needs and expand its overall capabilities.</li>
<br>
    <li><strong>System Ability:</strong>  For Data Collection The system supports multiple incoming physiological data streams from various sources. Using multiprocessing, the system distributes the raw data to predefined feature extraction modules, which analyze specific physiological signals supported by the use of TCP for real-time data transfer, ensuring seamless communication between different computational processes. Buffers store transient data to prevent loss and improve efficiency. Extracted features are examined and displayed according to researcher-defined parameters, allowing immediate insights into physiological responses.</li>
<br>
    <li><strong>Looking Ahead:</strong> While the framework is operational, expanding the system's capabilities by developing additional feature extraction methods is essential for broader applications. Neurokit currently serves as both an analytical tool and a reference point for designing new functionalities, demonstrating how other feature extraction techniques can be structured within this ecosystem. By following the documentation, users can harness the full potential of this program, whether by utilizing its existing methods or by contributing new physiological feature analyses that enhance its scope and accuracy.</li>
<br>
</ul>
<h3 id="General_Recommendations"><u>General Recommendations:</u></h3>
<li>Before running a custom feature exstraction script on an important deveice run it on a personal one to ensure that it is built correctly and doesnt damage the computerer</li>
<li>Use all avaliable development toos labeled with the prefix [T] as it will make development much smoother and help rule out the system itself having a bug</li>
<li>An annoying but common b ug found in development is when a process is run only once due to a terminator like "sys.exit" or a function like "sleep" being used as these both have a computer wide affect forcing all elements to be halted.</li>
<li>Familiarize yourself with Pyqt6, TCP, and Multi threading</li>
<h3 id="Resources"><u>Additional Resources:</u></h3>
<p>Still confused? Here are some resources for learning more about these concepts:</p>
<ul>
    <li><a href="https://www.geeksforgeeks.org/">GeeksforGeeks</a></li>
    <li><a href="https://www.ibm.com/docs/en">IBM Documentation</a></li>
</ul>
<h2>Setting Up Real-Time</h2>
    <h3 id ="Easy_Anaconda_Environment">Easy: Anaconda Environment</h3>
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
    <h3 id="Third_Party_Links">Manual: Downloading Required Packages</h3>
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
