import streamlit as st

# Configure Streamlit page for a wide, beautiful layout
st.set_page_config(
    page_title="Professional Scientific Calculator",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit's default headers and footers for a clean, professional look
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        body {
            background-color: #121212;
        }
    </style>
""", unsafe_allow_html=True)

# Embed the complete premium iOS-style responsive scientific calculator
calculator_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sleek Scientific Calculator</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@400;700&family=SF+Pro+Display:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        * {
            box-sizing: border-box;
            user-select: none;
            -webkit-user-select: none;
        }
        body {
            background-color: #121212;
            font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 10px;
        }
        .calculator-frame {
            background: linear-gradient(145deg, #232526, #111111);
            border-radius: 28px;
            padding: 24px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7), 
                        inset 0 2px 3px rgba(255, 255, 255, 0.15);
            width: 100%;
            max-width: 900px;
            border: 2px solid #333;
        }
        
        /* LCD Screen Design matching image 17844381991772111704529177274507_6d3fba.jpg */
        .screen {
            background: linear-gradient(to bottom, #d2dec4, #b4c2a3);
            border-radius: 14px;
            padding: 18px 24px;
            margin-bottom: 24px;
            box-shadow: inset 0 4px 10px rgba(0, 0, 0, 0.3), 
                        0 2px 4px rgba(255, 255, 255, 0.05);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: flex-end;
            height: 120px;
            border: 3px solid #222;
            position: relative;
            overflow: hidden;
        }
        /* Realistic Screen Glare Effect */
        .screen::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 50%;
            background: linear-gradient(rgba(255,255,255,0.15), rgba(255,255,255,0));
            pointer-events: none;
        }
        .screen-top-indicator {
            width: 100%;
            display: flex;
            justify-content: space-between;
            font-size: 14px;
            font-weight: 700;
            color: #3b4234;
            letter-spacing: 1px;
            text-transform: uppercase;
        }
        .display-value {
            font-size: 48px;
            color: #1c2117;
            font-weight: 600;
            text-align: right;
            word-break: break-all;
            max-width: 100%;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            letter-spacing: 0.5px;
            font-family: monospace;
        }
        
        /* Layout Grid */
        .grid-container {
            display: grid;
            grid-template-columns: repeat(8, 1fr);
            gap: 12px;
            position: relative;
        }
        
        /* Button Styles */
        button {
            border: none;
            outline: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 52px;
            transition: transform 0.05s, filter 0.08s;
            position: relative;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.4), 
                        inset 0 1px 1px rgba(255, 255, 255, 0.1);
        }
        button:active {
            transform: scale(0.95);
            filter: brightness(0.85);
        }
        
        /* Color Palettes matching scientific calculators */
        /* Columns 1-4: Scientific keys */
        .btn-scientific {
            background: linear-gradient(to bottom, #3a3d40, #242528);
            color: #e5e5e5;
            font-size: 15px;
            font-weight: 500;
            border: 1px solid #1a1b1d;
        }
        /* Row 1 standard keys & +/- / C */
        .btn-utility {
            background: linear-gradient(to bottom, #595c5f, #3b3d40);
            color: #ffffff;
            font-size: 17px;
            border: 1px solid #2a2b2d;
        }
        /* Numeric pad keys */
        .btn-number {
            background: linear-gradient(to bottom, #2b2c2e, #141516);
            color: #ffffff;
            font-size: 21px;
            font-weight: 600;
            border: 1px solid #0d0e0f;
        }
        /* Basic operations on right & equal */
        .btn-orange {
            background: linear-gradient(to bottom, #f2a154, #d47a22);
            color: #ffffff;
            font-size: 20px;
            font-weight: 700;
            border: 1px solid #945110;
        }
        .btn-orange:active {
            background: #d47a22;
        }
        
        /* Double height equal button */
        .double-height-equal {
            grid-row: span 2;
            height: calc(104px + 12px); /* Spans 2 rows precisely */
            background: linear-gradient(to bottom, #f59e0b, #d97706);
        }
        
        /* 2nd Function active state */
        .active-2nd {
            background: linear-gradient(to bottom, #f59e0b, #d97706) !important;
            color: white !important;
            box-shadow: 0 0 10px rgba(245, 158, 11, 0.5) !important;
        }
        
        /* Small styling adjustments */
        sup {
            font-size: 10px;
            margin-left: 1px;
        }
        .memory-indicator {
            font-size: 12px;
            color: #d45d00;
            font-weight: bold;
            opacity: 0;
            transition: opacity 0.2s;
        }
        .memory-indicator.active {
            opacity: 1;
        }
    </style>
</head>
<body>

    <div class="calculator-frame">
        <!-- Display Screen -->
        <div class="screen">
            <div class="screen-top-indicator">
                <span id="angle-mode-display">Rad</span>
                <span id="memory-flag" class="memory-indicator">M</span>
            </div>
            <div class="display-value" id="calc-display">0</div>
        </div>
        
        <!-- Button Grid (8 Columns x 6 Rows) -->
        <div class="grid-container">
            
            <!-- ROW 1 -->
            <button class="btn-scientific" onclick="handleBtn('2nd')" id="btn-2nd">2nd</button>
            <button class="btn-scientific" onclick="handleBtn('(')">(</button>
            <button class="btn-scientific" onclick="handleBtn(')')">)</button>
            <button class="btn-scientific" onclick="handleBtn('%')">%</button>
            <button class="btn-utility" onclick="handleBtn('mc')">mc</button>
            <button class="btn-utility" onclick="handleBtn('m+')">m+</button>
            <button class="btn-utility" onclick="handleBtn('m-')">m-</button>
            <button class="btn-utility" onclick="handleBtn('mr')">mr</button>
            
            <!-- ROW 2 -->
            <button class="btn-scientific" onclick="handleBtn('1/x')">1/x</button>
            <button class="btn-scientific" onclick="handleBtn('x²')">x²</button>
            <button class="btn-scientific" onclick="handleBtn('x³')">x³</button>
            <button class="btn-scientific" onclick="handleBtn('yˣ')">y<sup>x</sup></button>
            <button class="btn-utility" onclick="handleBtn('C')">C</button>
            <button class="btn-utility" onclick="handleBtn('+/-')">+/-</button>
            <button class="btn-orange" onclick="handleBtn('÷')">÷</button>
            <button class="btn-orange" onclick="handleBtn('×')">×</button>
            
            <!-- ROW 3 -->
            <button class="btn-scientific" onclick="handleBtn('x!')">x!</button>
            <button class="btn-scientific" onclick="handleBtn('√')">√</button>
            <button class="btn-scientific" onclick="handleBtn('³√y')" id="btn-cube-root">³√y</button>
            <button class="btn-scientific" onclick="handleBtn('log')">log</button>
            <button class="btn-number" onclick="handleBtn('7')">7</button>
            <button class="btn-number" onclick="handleBtn('8')">8</button>
            <button class="btn-number" onclick="handleBtn('9')">9</button>
            <button class="btn-orange" onclick="handleBtn('-')">-</button>
            
            <!-- ROW 4 -->
            <button class="btn-scientific" onclick="handleBtn('sin')" id="btn-sin">sin</button>
            <button class="btn-scientific" onclick="handleBtn('cos')" id="btn-cos">cos</button>
            <button class="btn-scientific" onclick="handleBtn('tan')" id="btn-tan">tan</button>
            <button class="btn-scientific" onclick="handleBtn('log₂')">log<sub>2</sub></button>
            <button class="btn-number" onclick="handleBtn('4')">4</button>
            <button class="btn-number" onclick="handleBtn('5')">5</button>
            <button class="btn-number" onclick="handleBtn('6')">6</button>
            <button class="btn-orange" onclick="handleBtn('+')">+</button>
            
            <!-- ROW 5 -->
            <button class="btn-scientific" onclick="handleBtn('sinh')" id="btn-sinh">sinh</button>
            <button class="btn-scientific" onclick="handleBtn('cosh')" id="btn-cosh">cosh</button>
            <button class="btn-scientific" onclick="handleBtn('tanh')" id="btn-tanh">tanh</button>
            <button class="btn-scientific" onclick="handleBtn('2ˣ')">2<sup>x</sup></button>
            <button class="btn-number" onclick="handleBtn('1')">1</button>
            <button class="btn-number" onclick="handleBtn('2')">2</button>
            <button class="btn-number" onclick="handleBtn('3')">3</button>
            <!-- Equal button spanning Row 5 and 6 -->
            <button class="btn-orange double-height-equal" onclick="handleBtn('=')">=</button>
            
            <!-- ROW 6 -->
            <button class="btn-scientific" onclick="handleBtn('angle-toggle')" id="btn-deg-rad">Deg</button>
            <button class="btn-scientific" onclick="handleBtn('π')">π</button>
            <button class="btn-scientific" onclick="handleBtn('EE')">EE</button>
            <button class="btn-scientific" onclick="handleBtn('Rand')">Rand</button>
            <!-- Zero spans 1 column matching Col 5 -->
            <button class="btn-number" onclick="handleBtn('0')">0</button>
            <button class="btn-number" onclick="handleBtn('.')">.</button>
            <button class="btn-utility" onclick="handleBtn('Del')">Del</button>
        </div>
    </div>

    <script>
        // Physical tactile clicking sound generation via Web Audio API
        function playClick() {
            try {
                let ctx = new (window.AudioContext || window.webkitAudioContext)();
                let osc = ctx.createOscillator();
                let gain = ctx.createGain();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(600, ctx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(10, ctx.currentTime + 0.04);
                gain.gain.setValueAtTime(0.04, ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.04);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start();
                osc.stop(ctx.currentTime + 0.04);
            } catch(e) {}
        }

        // Calculator states
        let display = document.getElementById('calc-display');
        let currentVal = "0";
        let previousVal = "";
        let pendingOp = "";
        let is2ndActive = false;
        let angleMode = "Rad"; // Default Mode
        let memoryValue = 0;
        let resetDisplayOnNextInput = false;

        function updateDisplay() {
            // Beautify large numbers with clean spaces/commas separation
            let formatted = currentVal;
            if (!isNaN(formatted) && formatted !== "" && !formatted.includes('e')) {
                let parts = formatted.split('.');
                parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, " ");
                formatted = parts.join('.');
            }
            display.innerText = formatted;
        }

        function handleBtn(key) {
            playClick();
            
            if (!isNaN(key) || key === '.') {
                if (currentVal === "0" && key !== '.') {
                    currentVal = key;
                } else {
                    if (resetDisplayOnNextInput) {
                        currentVal = key;
                        resetDisplayOnNextInput = false;
                    } else {
                        if (key === '.' && currentVal.includes('.')) return;
                        currentVal += key;
                    }
                }
                updateDisplay();
                return;
            }

            switch(key) {
                case 'C':
                    currentVal = "0";
                    previousVal = "";
                    pendingOp = "";
                    resetDisplayOnNextInput = false;
                    updateDisplay();
                    break;

                case 'Del':
                    if (currentVal.length > 1){
                        currentVal = currentVal.slice(0, -1);
                    } else {
                        currentVal = "0";
                    }
                    updateDisplay();
                    break;    
                    
                case '+/-':
                    currentVal = (parseFloat(currentVal) * -1).toString();
                    updateDisplay();
                    break;
                    
                case '%':
                    currentVal = (parseFloat(currentVal) / 100).toString();
                    updateDisplay();
                    break;
                    
                case 'π':
                    currentVal = Math.PI.toString();
                    updateDisplay();
                    break;
                    
                case 'Rand':
                    currentVal = Math.random().toString();
                    updateDisplay();
                    break;
                    
                case '1/x':
                    let num = parseFloat(currentVal);
                    currentVal = num !== 0 ? (1 / num).toString() : "Error";
                    updateDisplay();
                    break;
                    
                case 'x²':
                    currentVal = Math.pow(parseFloat(currentVal), 2).toString();
                    updateDisplay();
                    break;
                    
                case 'x³':
                    currentVal = Math.pow(parseFloat(currentVal), 3).toString();
                    updateDisplay();
                    break;
                    
                case '2ˣ':
                    currentVal = Math.pow(2, parseFloat(currentVal)).toString();
                    updateDisplay();
                    break;
                    
                case 'x!':
                    currentVal = factorial(parseFloat(currentVal)).toString();
                    updateDisplay();
                    break;
                    
                case '√':
                    currentVal = Math.sqrt(parseFloat(currentVal)).toString();
                    updateDisplay();
                    break;
                    
                case '³√y':
                    currentVal = Math.cbrt(parseFloat(currentVal)).toString();
                    updateDisplay();
                    break;
                    
                case 'EE':
                    currentVal += "e+";
                    updateDisplay();
                    break;
                    
                // Memory operations
                case 'mc':
                    memoryValue = 0;
                    document.getElementById('memory-flag').classList.remove('active');
                    break;
                case 'm+':
                    memoryValue += parseFloat(currentVal);
                    document.getElementById('memory-flag').classList.add('active');
                    break;
                case 'm-':
                    memoryValue -= parseFloat(currentVal);
                    document.getElementById('memory-flag').classList.add('active');
                    break;
                case 'mr':
                    currentVal = memoryValue.toString();
                    updateDisplay();
                    break;
                    
                // Degree/Rad Toggle
                case 'angle-toggle':
                    if (angleMode === "Rad") {
                        angleMode = "Deg";
                        document.getElementById('btn-deg-rad').innerText = "Rad";
                    } else {
                        angleMode = "Rad";
                        document.getElementById('btn-deg-rad').innerText = "Deg";
                    }
                    document.getElementById('angle-mode-display').innerText = angleMode;
                    break;
                    
                // 2nd button layout toggle
                case '2nd':
                    is2ndActive = !is2ndActive;
                    document.getElementById('btn-2nd').classList.toggle('active-2nd', is2ndActive);
                    
                    // Toggle values dynamically
                    document.getElementById('btn-sin').innerHTML = is2ndActive ? "sin⁻¹" : "sin";
                    document.getElementById('btn-cos').innerHTML = is2ndActive ? "cos⁻¹" : "cos";
                    document.getElementById('btn-tan').innerHTML = is2ndActive ? "tan⁻¹" : "tan";
                    document.getElementById('btn-sinh').innerHTML = is2ndActive ? "sinh⁻¹" : "sinh";
                    document.getElementById('btn-cosh').innerHTML = is2ndActive ? "cosh⁻¹" : "cosh";
                    document.getElementById('btn-tanh').innerHTML = is2ndActive ? "tanh⁻¹" : "tanh";
                    break;
                    
                // Math functions (Angles taken into account)
                case 'sin':
                case 'cos':
                case 'tan':
                case 'sinh':
                case 'cosh':
                case 'tanh':
                    let angle = parseFloat(currentVal);
                    if (angleMode === "Deg" && !key.startsWith('sinh') && !key.startsWith('cosh') && !key.startsWith('tanh')) {
                        angle = angle * (Math.PI / 180);
                    }
                    
                    if (!is2ndActive) {
                        if (key === 'sin') currentVal = Math.sin(angle).toString();
                        if (key === 'cos') currentVal = Math.cos(angle).toString();
                        if (key === 'tan') currentVal = Math.tan(angle).toString();
                        if (key === 'sinh') currentVal = Math.sinh(angle).toString();
                        if (key === 'cosh') currentVal = Math.cosh(angle).toString();
                        if (key === 'tanh') currentVal = Math.tanh(angle).toString();
                    } else {
                        // Inverse functions
                        if (key === 'sin') currentVal = (angleMode === "Deg" ? Math.asin(parseFloat(currentVal)) * (180 / Math.PI) : Math.asin(parseFloat(currentVal))).toString();
                        if (key === 'cos') currentVal = (angleMode === "Deg" ? Math.acos(parseFloat(currentVal)) * (180 / Math.PI) : Math.acos(parseFloat(currentVal))).toString();
                        if (key === 'tan') currentVal = (angleMode === "Deg" ? Math.atan(parseFloat(currentVal)) * (180 / Math.PI) : Math.atan(parseFloat(currentVal))).toString();
                        if (key === 'sinh') currentVal = Math.asinh(parseFloat(currentVal)).toString();
                        if (key === 'cosh') currentVal = Math.acosh(parseFloat(currentVal)).toString();
                        if (key === 'tanh') currentVal = Math.atanh(parseFloat(currentVal)).toString();
                    }
                    updateDisplay();
                    break;
                    
                case 'log':
                    currentVal = Math.log10(parseFloat(currentVal)).toString();
                    updateDisplay();
                    break;
                    
                case 'log₂':
                    currentVal = Math.log2(parseFloat(currentVal)).toString();
                    updateDisplay();
                    break;

                // Basic Binary operations
                case '+':
                case '-':
                case '×':
                case '÷':
                case 'yˣ':
                    previousVal = currentVal;
                    pendingOp = key;
                    resetDisplayOnNextInput = true;
                    break;
                    
                case '=':
                    if (previousVal !== "" && pendingOp !== "") {
                        let a = parseFloat(previousVal);
                        let b = parseFloat(currentVal);
                        let res = 0;
                        if (pendingOp === '+') res = a + b;
                        if (pendingOp === '-') res = a - b;
                        if (pendingOp === '×') res = a * b;
                        if (pendingOp === '÷') res = b !== 0 ? a / b : "Error";
                        if (pendingOp === 'yˣ') res = Math.pow(a, b);
                        
                        currentVal = res.toString();
                        previousVal = "";
                        pendingOp = "";
                        updateDisplay();
                    }
                    break;
            }
        }

        function factorial(n) {
            if (n < 0) return "Error";
            if (n === 0 || n === 1) return 1;
            let result = 1;
            for (let i = 2; i <= Math.floor(n); i++) result *= i;
            return result;
        }

        // Support physical keyboard inputs for standard calculations
        document.addEventListener('keydown', (event) => {
            let key = event.key;
            if (!isNaN(key)) handleBtn(key);
            if (key === '.') handleBtn('.');
            if (key === '+') handleBtn('+');
            if (key === '-') handleBtn('-');
            if (key === '*') handleBtn('×');
            if (key === '/') handleBtn('÷');
            if (key === 'Enter' || key === '=') handleBtn('=');
            if (key === 'Escape' || key === 'c' || key === 'C') handleBtn('C');
        });
    </script>
</body>
</html>
"""

# Render the custom designed scientific calculator
st.components.v1.html(calculator_html, height=720, scrolling=False)
