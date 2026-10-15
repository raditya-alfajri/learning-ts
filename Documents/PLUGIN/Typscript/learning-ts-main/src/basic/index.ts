let nama: string = "John Doe";
let umur: number = 30;
let isStudent: boolean = true;

console.log(`Nama: ${nama}`);
console.log(`Umur: ${umur}`);
console.log(`Apakah mahasiswa: ${isStudent}`);

let hobi: string[] = ["Membaca", "Bersepeda", "Memasak"]; 
console.log(`nama: ${nama} memiliki hobi: ${hobi[0]}`);

if (umur <= 18){ 
    console.log(`${nama} dibawah umur`);
} else {
    console.log(`${nama} sudah dewasa`);
}

let hari: string = "Sabtu";

switch (hari) {
    case "Senin":
        console.log("weekday");
        break;
    case "Selasa":
        console.log("weekday");
        break;
    case "Rabu":
        console.log("weekday");
        break;
    case "Kamis":
        console.log("weekday");
        break;
    case "Jumat":
        console.log("before weekend");
        break;
    default:
        console.log("weekend");
}

for (let i = 0; i < hobi.length; i++) {
    console.log(`Hobi ke-${i + 1}: ${hobi[i]}`);
} 

function tambah(a: number, b: number): number {
    return a + b;
}

let hasil = tambah(5, 10);
console.log(`Hasil penjumlahan: ${hasil}`);