import {Cliente} from "./Cliente.js"
import { Gerente } from "./Funcionario/Gerente.js"
import { Diretor } from "./Funcionario/Diretor.js"
import { SistemaAutenticacao } from "./SistemaAutenticacao.js";

const diretor = new Diretor("Rodrigo", 10000, 12348765);
diretor.cadastrarSenha("123456");
const gerente = new Gerente("Joaquim",  5000, 12345678);
gerente.cadastrarSenha("123");

const cliente = new Cliente("Lais", 789432, "456");
const gerenteEstaLogado = SistemaAutenticacao.login(gerente, "123");
const diretorEstaLogado = SistemaAutenticacao.login(diretor, "123456");

const clienteEstaLogado = SistemaAutenticacao.login(cliente, "456");

console.log(clienteEstaLogado);
console.log(diretorEstaLogado, gerenteEstaLogado);