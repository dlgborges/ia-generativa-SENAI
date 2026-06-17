function analisar() {
    const ticker = document.getElementById('tickerInput').value.toUpperCase();
    const resDiv = document.getElementById('resultado');
    const status = document.getElementById('status');
    const expl = document.getElementById('explicacao');
    const alt = document.getElementById('alternativas');

    resDiv.classList.remove('hidden');

    // Lógica de simulação (Substituir por chamada de API real no futuro)
    if (ticker === "EXEMPLO") {
        status.innerText = "Investimento cauteloso";
        status.className = "alerta";
        expl.innerText = "A empresa apresenta alta volatilidade no curto prazo e uma dívida líquida elevada em relação ao patrimônio líquido.";
        alt.innerHTML = "<strong>Sugestão:</strong> Considere empresas de 'Utilidade Pública' ou 'Dividendos', que possuem fluxo de caixa mais previsível.";
    } else {
        status.innerText = "Análise neutra/positiva";
        status.className = "sucesso";
        expl.innerText = "Com base em indicadores fundamentais, a empresa demonstra saúde financeira estável.";
        alt.innerHTML = "";
    }
}