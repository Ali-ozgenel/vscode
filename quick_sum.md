doc:different points of quick sort kinds
🧩 1️⃣ Lomuto Partition (En basit ama verimsiz olan)
📘 Mantık:
Pivot her zaman dizinin son elemanı (pivot = arr[ub])
Tek bir “gezen” değişken (i) kullanır.
Dizi baştan sona tek yönde taranır.
💻 Tipik yapı:
int Partition(int arr[], int lb, int ub) {
    int pivot = arr[ub];
    int i = lb - 1;

    for (int j = lb; j < ub; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i+1], &arr[ub]);
    return i+1;
}
🔹 Özellikler:
Döngü tek yönlü (sol → sağ).
Sade ama fazla swap yapar.
Küçük diziler için kolay, ama pratikte daha yavaştır.
Pivot’un son eleman olması gereklidir.
🧩 2️⃣ Hoare Partition (Klasik ve hızlı olan)
📘 Mantık:
Pivot genelde ilk eleman (pivot = arr[lb])
İki uçtan (start, end) ortada buluşma prensibi.
Döngü iki yönde işler.
💻 Tipik yapı:
int Partition(int arr[], int lb, int ub) {
    int pivot = arr[lb];
    int start = lb;
    int end = ub;

    while (start < end) {
        while (arr[start] <= pivot) start++;
        while (arr[end] > pivot) end--;
        if (start < end)
            swap(&arr[start], &arr[end]);
    }
    swap(&arr[lb], &arr[end]);
    return end;
}
🔹 Özellikler:
İki yönlü çalışır (soldan-sağa ve sağdan-sola).
Swap sayısı azdır.
Pivot ilk elemandır.
while(start < end) kullanılır çünkü pivot döngü dışında swap’lanır.
🧩 3️⃣ Middle Pivot (Hoare benzeri, ama pivot ortada)
📘 Mantık:
Pivot ortadaki eleman (pivot = arr[(left+right)/2])
İki uçtan (i, j) hareket eder ama pivot sabittir.
<= kullanılır çünkü pivot da işlenir.
💻 Tipik yapı:
void quicksort(int D[], int left, int right) {
    int i = left, j = right;
    int pivot = D[(left + right) / 2];
    int temp;

    do {
        while (D[i] < pivot) i++;
        while (D[j] > pivot) j--;
        if (i <= j) {
            temp = D[i];
            D[i] = D[j];
            D[j] = temp;
            i++; j--;
        }
    } while (i <= j);

    if (left < j)
        quicksort(D, left, j);
    if (i < right)
        quicksort(D, i, right);
}
🔹 Özellikler:
Hoare’a çok benzer ama pivot ortadadır.
Pivot işlem sırasında dizinin içinde kalır (taşınmaz).
<= kullanılır çünkü pivot’un kendisi de kontrol edilir.
Swap sayısı azdır, pratikte çok etkilidir.