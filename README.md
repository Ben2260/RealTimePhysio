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
