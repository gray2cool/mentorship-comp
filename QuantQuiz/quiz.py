import random 
 
def main(): 
    msgs = ["1. A systematic quant manager relies primarily on intuition and real-time news sentiment to adjust portfolio weights during a market session. (T/F)", 
    "2. Harry Markowitz’s development of Modern Portfolio Theory in the 1950s is considered a foundational milestone in quantitative finance. (T/F)", 
    "3. A Quant Developer's primary \"ship\" or output is usually a research paper or a mathematical signal, rather than the execution infrastructure. (T/F)", 
    "4. Geometric Brownian Motion is a common stochastic process used to model stock prices because it prevents prices from becoming negative. (T/F)", 
    "5. In the context of time-series modeling, a GARCH model is primarily used to forecast the mean return of an asset over time. (T/F)", 
    "6. Survivorship bias occurs when a backtest includes only the companies that currently exist, ignoring those that went bankrupt or were delisted. (T/F)", 
    "7. The Sharpe Ratio is a risk-adjusted performance metric that penalizes only \"bad\" volatility (downside) while ignoring \"good\" volatility (upside). (T/F)", 
    "8. \"Look-ahead bias\" in backtesting involves using information in a simulation that would not have been available to the trader at that specific time. (T/F)", 
    "9. Statistical Arbitrage (Stat-Arb) typically relies on the mean-reverting behavior of a pair or group of related financial instruments. (T/F)", 
    "10. Python is preferred over C++ for low-latency execution systems due to its superior memory management and execution speed. (T/F)"]
    
    answerKey = ["f", "t", "f", "t", "f", "t", "f", "t", "t", "f"] 
     
    welcomeStatement() 
    responses = navigate(msgs, answerKey) 
    score = calculateScore(responses, answerKey, msgs) 
    print(f"Total correct: {score} out of {len(msgs)}") 
    print("No money here!") 
 
def welcomeStatement(): 
    x = input("Are you ready to answer the Quant Quiz? If you pass you may/may not get $1,000,000 (yes/no): ").lower()
    if x in ["no", "nah"]: 
        quit() 
    else: 
        print("Answer all questions carefully, ethier (T)rue or (F)alse!") 
 
def navigate(mL, key): 
    responses = [''] * len(mL) 
    a = 0 
    b = 0 
    index = 0 
    cont = True 
    while cont == True: 
        responce = input("What do you want to do? (N)ext, (P)revious, (G)oto, (R)andom, (S)hake, or (Q)uit?").lower() 
        if responce == "q" or responce == "quit": 
            return submitResponses(responses, mL, key) 
        elif responce == "n" or responce == "next": 
            if a >= 1: 
                index = (index + 1) % len(mL) 
            else: 
                index = 0 
            a = a + 1 
        elif responce == "p" or responce == "previous": 
            if a >= 1: 
                if index == 0: 
                    index = len(mL) 
                index = index - 1 
            else: 
                index = 0 
            a = a + 1 
        elif responce == "g" or responce == "goto": 
            ans = eval(input("Which #? (1-" + str(len(mL)) + ")Message: ")) 
            if ans < 1 or ans > len(mL): 
                print("invalid number") 
            index = ans - 1 
            a = a + 1 
        elif responce == "r" or responce == "random": 
            index = random.randint(0,len(mL)-1) 
            a = a + 1 
        elif responce == "s" or responce == "shake": 
            x = list(zip(mL, key, responses)) 
            random.shuffle(x) 
            mL[:], key[:], responses[:] = zip(*x) 
            responses = list(responses) 
            index = 0 
            a = a + 1 
            print("Messages, answer key, and responses shuffled!") 
            continue 
        else: 
            print("Invalid Entry - Try Again") 
            continue 
         
        print(mL[index], responses[index]) 
        responses[index] = input("Response: ").lower 
 
        print(key) 
        print(responses) 
        print(mL) 
 
        if all(responses) and b<1: 
            return completedResponses(responses, mL, key) 
            b = b + 1 
 
        completion = sum(1 for r in responses if r) 
        print(f"You have answered {completion} out of {len(mL)} questions.") 
 
def completedResponses(responses, mL, key): 
    completion = sum(1 for r in responses if r) 
 
    while True: 
        confirm = input(f"You're Done! You have answered {completion} out of {len(responses)} questions. Are you finished? (yes/no): ").lower() 
        if confirm in ["yes", "y"]: 
            return responses 
        elif confirm in ["no", "n"]: 
            print("Continue answering questions.") 
            return navigate(mL, key) 
        else: 
            print("Invalid input. Please type 'yes' or 'no'.") 
 
def submitResponses(responses, mL, key): 
    completion = sum(1 for r in responses if r) 
 
    while True: 
        confirm = input(f"You have answered {completion} out of {len(responses)} questions. Are you sure you're finished? (yes/no): ").lower() 
        if confirm in ["yes", "y"]: 
            return responses 
        elif confirm in ["no", "n"]: 
            print("Continue answering questions.") 
            return navigate(mL, key)
        else: 
            print("Invalid input. Please type 'yes' or 'no'.") 
 
def calculateScore(responses, key, mL): 
    score = 0
    for i in range(len(responses)):
        if responses[i] == key[i]:
            score = score + 1 
    return score 
 
main()