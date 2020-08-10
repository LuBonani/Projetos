//classe abstrata
export class Conta{
    constructor(saldoInicial, cliente, agencia){
        if(this.constructor == Conta){
            throw new Error ("Você não deveria instanciar um objeto do tipo Conta");
        }

        this._saldo = saldoInicial;
        this._cliente = cliente;
        this._agencia = agencia;
    }

    set cliente(novoValor){
        if(novoValor instanceof Cliente){
            this._cliente = novoValor;
        }
    }

    get cliente(){
        return this._cliente;
    }
    
    get saldo(){
        return this._saldo;
    }

    //Método abstrato
    sacar(valor){
        throw new Error ("O método sacar da Conta é abstrato")
    }
    
    _sacar(valor, taxa){
        valor = taxa * valor;
        if(this._saldo >= valor){
            this._saldo -= valor;
            return valor;
        }
        return 0;
    }

    depositar(valor){
        if(valor <= 0){
            return;
        }
        this._saldo += valor;
    }

    transferir(valor, conta){
        this.sacar(valor);
        conta.depositar(valor);
    }
}