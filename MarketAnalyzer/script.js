const apiKey = 'CG-y2RdvEzEZ6z57m8FoE5KCJzz';
const apiUrl = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=7&interval=daily';

const requestOptions = {
    method: 'GET',
    headers: {
        'Authorization': `Bearer ${apiKey}`,
    },
};

fetch(apiUrl, requestOptions)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const priceHistory = data.prices.map(item => item[1]);
        updateDashboard(priceHistory);
    })
    .catch(error => {
        console.error('Error:', error);
    });

function updateDashboard(priceHistory) {
    const currentPrice = priceHistory.at(-1);
    const firstPrice = priceHistory[0];
    

    document.getElementById("currentPrice").innerHTML = currentPrice.toFixed(2);

    const totalReturn = ((currentPrice - firstPrice) / firstPrice) * 100;
    document.getElementById("totalReturn").innerHTML = totalReturn.toPrecision(4) + "%";

    let dailyReturns = [];
    for (let i = 1; i < priceHistory.length; i++) 
        {
        let change = (priceHistory[i] / priceHistory[i - 1]) - 1;
        dailyReturns.push(change);
    }
    console.log("Daily Returns:", dailyReturns);
    var tag = document.getElementById("dailyReturns");
    var ulHTML = "<ul>";

    for(let i = 0;i < dailyReturns.length;i++){
        ulHTML += `<li>${dailyReturns[i].toFixed(2)}</li>`;
    }

    ulHTML += "</ul>";
    tag.innerHTML = ulHTML;

    let meanReturn = dailyReturns.reduce((a, b) => a + b) / dailyReturns.length;
    let variance = dailyReturns.reduce((a, b) => a + Math.pow(b - meanReturn, 2), 0) / dailyReturns.length;
    let volatility = Math.sqrt(variance);
    console.log("Volatility (Standard Deviation):", volatility.toFixed(4));
    var tag = document.getElementById("volatility");
    tag.innerHTML += `${volatility.toPrecision(4)}`;

    let peak = 0;
    let maxDrawdown = 0;
    priceHistory.forEach(price => {
        if (price > peak) {
            peak = price; // Update the highest point reached 
        }
        let drawdown = (price - peak) / peak;
        if (drawdown < maxDrawdown) {
            maxDrawdown = drawdown; // Track the largest drop
        }
    });
    console.log("Maximum Drawdown (%):", (maxDrawdown * 100).toFixed(2));
    var tag = document.getElementById("maxDrawdown");
    tag.innerHTML += `${maxDrawdown.toPrecision(4)}`;

    console.log("Updated with live data:", priceHistory);
}

// // let priceHistory = [99, 105, 98, 110, 120, 115, 125];
// var tag = document.getElementById("priceHistory");
// var ulHTML = "<ul>";

// for(let i = 0;i < priceHistory.length;i++){
//     ulHTML += `<li>${priceHistory[i]}</li>`;
// }

// ulHTML += "</ul>";
// tag.innerHTML = ulHTML;

// // const currentPrice = priceHistory[priceHistory.length - 1];
// const currentPrice = priceHistory.at(-1)
// console.log("Current Price:", currentPrice);
// var tag = document.getElementById("currentPrice");
// tag.innerHTML += `${currentPrice}`;

// // var tag = document.getElementById("output");
// // tag.innerHTML = "<h2>hello</h2>"

// //Calculation: Total Return
// const firstPrice = priceHistory[0];
// const totalReturn = ((currentPrice - firstPrice) / firstPrice) * 100;
// // console.log("Total Return (%):", totalReturn.toFixed(2));
// console.log("Total Return (%):", totalReturn);
// var tag = document.getElementById("totalReturn");
// tag.innerHTML += `${totalReturn.toPrecision(4)}`;
