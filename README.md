<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Real-Time Feature Analysis</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
            h1, h2, h3, h4, h5 { color: #333; }
            ul { list-style-type: none; padding-left: 20px; }
            li { margin-bottom: 5px; }
            blockquote { background: #f9f9f9; border-left: 10px solid #ccc; padding: 10px; margin: 10px 0; }
            pre { background: #f4f4f4; padding: 10px; border-radius: 5px; font-family: monospace; }
            a { color: #007BFF; text-decoration: none; }
            u { text-decoration: underline; }
        </style>
</head>
<body>
    <h1>Real-Time Feature Analysis</h1>
    <h2>Table of Contents</h2>
    <ul>
        <li><strong>1. Overview</strong>
            <ul>
                <li>Terminology</li>
                <li>Organizational Structure</li>
                <li>Current state of the program</li>
                <li>General recommendations</li>
            </ul>
        </li>
        <li><strong>2. Downloading Required Packages</strong>
            <ul>
                <li>Installing Multiprocessing, Pandas, NumPy, Time, Socket, Neurokit 2, Python 3.12</li>
                <li>Important links to 3rd party software</li>
            </ul>
        </li>
        <li><strong>3. Available Functionality</strong>
            <ul>
                <li><a href="#EDA">EDA</a></li>
                <li>RSP</li>
            </ul>
        </li>
        <li><strong>4. Examples</strong>
            <ul>
                <li>Running the Main</li>
                <li>Using Device Emulator</li>
                <li>Understanding TCP</li>
                <li>Understanding Multiprocessing</li>
            </ul>
        </li>
        <li><strong>5. Future Development</strong>
            <ul>
                <li>Design & Theory</li>
                <li>GTL Lock & Limitations</li>
                <li>Making New Functions</li>
            </ul>
        </li>
    </ul>
    <h2>Overview</h2>
    <h4><u>Code Terminology:</u></h4>
    <ul>
        <li><strong>CPU:</strong> The brain of your computer, responsible for evaluating programs.</li>
        <li><strong>Multi-Processing:</strong> Running multiple calculations in parallel.</li>
        <li><strong>Multi-Threading:</strong> TBD</li>
        <li><strong>CPU Up Time:</strong> Measures active computing time, should be optimized.</li>
        <li><strong>Memory Management:</strong> Allocating and optimizing memory resources.</li>
        <li><strong>Sliding Window:</strong> Processing smaller data segments sequentially.</li>
        <li><strong>Stride:</strong> Step size for sliding window movement.</li>
    </ul>
    <p><strong>Resources:</strong> 
        <a href="https://www.geeksforgeeks.org/">GeeksforGeeks</a> | 
        <a href="https://www.ibm.com/docs/en">IBM Documentation</a>
    </p>
    <h2>Setting Up Real-Time</h2>
    <h3>Automatically: Anaconda Environment</h3>
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
