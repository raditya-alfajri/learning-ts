export class motor {
    public merk: string;
    public warna: string;
    private ccMesin: number;

    constructor(merk: string, warna: string, ccMesin: number){
        this.merk = merk;
        this.warna = warna;
        this.ccMesin = ccMesin;
    }

    public nyalakanMesin(): void {
        console.log(`mesin : ${this.merk} warna ${this.warna}`)
    }

    public cekMesin(): void {
        console.log(`Mesin motor ini berkapasitas ${this.ccMesin}`)
    }
}
