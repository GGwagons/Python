<h1>guess_num.py</h1>

<h2>Overview</h2>
<p>The <code>guess_num.py</code> script is a number guessing game. The script generates a random number within a specified range, and the user has up to 7 attempts to guess the correct number. The range is dynamically generated, ensuring that there is always a difference of at least 5 and no more than 25 between the lower and upper bounds of the range.</p>

<h2>Dependencies</h2>
<ul>
    <li>Python 3.x</li>
    <li>Standard library modules:
        <ul>
            <li><code>random</code></li>
            <li><code>sys</code></li>
        </ul>
    </li>
</ul>

<h2>Script Details</h2>

<h3>Functions</h3>

<h4><code>between()</code></h4>
<p>Generates a random range <code>[lower, higher]</code> such that the difference between <code>higher</code> and <code>lower</code> is between 5 and 25 (inclusive).</p>

<p><strong>Returns:</strong></p>
<ul>
    <li><code>tuple</code>: A tuple containing two integers <code>(lower, higher)</code> where <code>0 &lt;= lower &lt; higher &lt;= 100</code>.</li>
</ul>

<p><strong>Example Usage:</strong></p>
<pre><code>lower, higher = between()</code></pre>

<h4><code>generate_random_int(lower, higher)</code></h4>
<p>Generates a random integer within the specified range <code>[lower, higher]</code>.</p>

<p><strong>Parameters:</strong></p>
<ul>
    <li><code>lower (int)</code>: The lower bound of the range.</li>
    <li><code>higher (int)</code>: The upper bound of the range.</li>
</ul>

<p><strong>Returns:</strong></p>
<ul>
    <li><code>int</code>: A random integer within the range <code>[lower, higher]</code>.</li>
</ul>

<p><strong>Example Usage:</strong></p>
<pre><code>x = generate_random_int(lower, higher)</code></pre>

<h3>Main Script</h3>

<ol>
    <li><strong>Generate the range:</strong> The script first calls <code>between()</code> to get a random range <code>(lower, higher)</code>.</li>
    <li><strong>Generate the target number:</strong> It then calls <code>generate_random_int(lower, higher)</code> to get the target number <code>x</code> that the user has to guess.</li>
    <li><strong>User interaction:</strong> The user is prompted to guess the number within the specified range. They have up to 7 attempts to guess correctly.
        <ul>
            <li>For each guess, the script checks if the user's guess is correct.</li>
            <li>If the guess is correct, the script congratulates the user and displays the number of attempts taken.</li>
            <li>If the guess is incorrect and there are remaining attempts, the script informs the user and indicates the remaining attempts.</li>
            <li>If all attempts are used without a correct guess, the script reveals the correct number and ends the game.</li>
        </ul>
    </li>
</ol>

<p><strong>Example Run:</strong></p>
<pre class="example"><code>Choose Between: 10 &lt;-&gt; 30
Guess The Number: 20
Ops! You Missed
You Still Have 6 Tries

Choose Between: 10 &lt;-&gt; 30
Guess The Number: 25
Congratulations You Did It In 2 Tries
THE WINNING NUMBER WAS: 25
</code></pre>
