import { motor } from "./motor";

const matic = new motor("honda vario", "merah", 160);
const matic2 = new motor("yamaha fazio", "hitam", 125);

matic.nyalakanMesin();
matic.cekMesin();

console.log("============================")

matic2.nyalakanMesin();
matic2.cekMesin();
