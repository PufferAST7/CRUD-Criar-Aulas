document.addEventListener('DOMContentLoaded', () => {

    // Referências dos modais
    const modalDetalhes = document.getElementById('modal-detalhes');
    const modalEditar = document.getElementById('modal-editar-aula');
    const modalNovaAula = document.getElementById('modal-nova-aula');

    // Evento de clique para cada botão "Detalhes"
    document.querySelectorAll('.btn-detalhes').forEach(botao => {
        botao.addEventListener('click', function () {

            // Captura os dados da aula vindos do dataset
            const titulo = this.dataset.titulo;
            const instrutor = this.dataset.instrutor;
            const data = this.dataset.data;
            const descricao = this.dataset.descricao;
            const sala = this.dataset.sala;
            const horario = this.dataset.horario;

            // Preenche o modal de detalhes com as informações
            document.getElementById('modal-titulo').innerText = titulo;
            document.getElementById('modal-instrutor').innerText = instrutor;
            document.getElementById('modal-data').innerText = data;
            document.getElementById('modal-descricao').innerText = descricao;
            document.getElementById('modal-sala').innerText = sala;
            document.getElementById('modal-horario').innerText = horario;

            // Prepara o valor do input oculto usado para excluir
            document.getElementById("excluir-titulo").value = titulo;

            // Configura o botão "Editar" com as informações da aula
            prepararEdicao(titulo, instrutor, data, descricao, sala, horario);

            // Exibe o modal de detalhes
            modalDetalhes.style.display = 'block';
        });
    });

    // Abre o modal de criar nova aula
    const btnNovaAula = document.getElementById("btn-nova-aula");
    btnNovaAula.onclick = () => modalNovaAula.style.display = "block";

    // Fecha qualquer modal ao clicar no botão X
    document.querySelectorAll(".close-button").forEach(btn => {
        btn.onclick = () => {
            btn.parentElement.parentElement.style.display = "none";
        };
    });

    // Função que prepara o modal de edição com os dados selecionados
    function prepararEdicao(titulo, instrutor, data, descricao, sala, horario) {
        const btnEditar = document.getElementById("btn-editar");

        btnEditar.onclick = () => {

            // Fecha o modal de detalhes e abre o modal de edição
            modalDetalhes.style.display = "none";
            modalEditar.style.display = "block";

            // Preenche os campos do modal de edição
            document.getElementById("editar-titulo-original").value = titulo;
            document.getElementById("editar-titulo").value = titulo;
            document.getElementById("editar-instrutor").value = instrutor;
            document.getElementById("editar-data").value = data;
            document.getElementById("editar-sala").value = sala;
            document.getElementById("editar-horario").value = horario;
            document.getElementById("editar-descricao").value = descricao;
        };
    }


    /* =============================
       ANIMAÇÃO DO TEXTO EXPANSÍVEL
       ============================= */

    // Botão que ativa a animação
    const toggleBtn = document.querySelector(".toggle-btn");

    // Caixa de texto que abre e fecha suavemente
    const textBox = document.querySelector(".text-box");

    // Só ativa se os elementos existirem na página
    if (toggleBtn && textBox) {
        toggleBtn.addEventListener("click", () => {

            // Alterna animação visual
            toggleBtn.classList.toggle("active");
            textBox.classList.toggle("visible");

            // Controla a altura animada
            if (textBox.classList.contains("visible")) {
                textBox.style.maxHeight = textBox.scrollHeight + "px";
            } else {
                textBox.style.maxHeight = "0px";
            }
        });
    }

});
