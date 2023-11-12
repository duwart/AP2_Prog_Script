document.getElementById("calculateButton").addEventListener("click", async function () {
    const numberInput = document.getElementById("numberInput");
    const errorElement = document.getElementById("error");

    const number = parseFloat(numberInput.value);

    const response = await fetch("/result/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ number: number })
        });
    
    if (!isNaN(number) && response.ok) {
        const data = await response.json();
        numberInput.value = data.result;
        errorElement.textContent = "";
    } else {
        errorElement.textContent = "Erro ao calcular. Insira um número válido!";
    }
});