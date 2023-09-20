# MODEL_dan_Deployment_Hacktiv8-FinalProject3-Classification-Ensemble-Model
Halo! Selamat datang di repository ku. Ini adalah model klasifikasi gagal jantung yang mempunyai akurasi sebesar 89% dengan algoritma Bagging! -Final Project H8

![image](https://github.com/Mazcho/MODEL_dan_Deployment_Hacktiv8-FinalProject3-Classification-Ensemble-Model/assets/77985996/7650caee-f8f0-40c1-885d-0dac47eb6221)

Model ini adalah hasil eksperiman model ensambel, yang dimana model ini diterapkan beberapa algoritma ensambel dan dipilih model yang terbaik. Setelah itu model terbaik akan dilakukan Tuning. Untuk algoritma terbaik ada pada Extratreeclasifire
ExtraTreesClassifier) adalah salah satu jenis model ensambel dalam machine learning. Model ini termasuk dalam kategori ensambel pohon keputusan, yang berarti itu berdasarkan pada konsep penggabungan sejumlah besar pohon keputusan untuk meningkatkan kinerja prediksi.
ExtraTreesClassifier memiliki karakteristik khusus yang membedakannya dari model pohon keputusan lainnya, seperti Random Forests. Dalam ExtraTreesClassifier:
Pemilihan Fitur Acak: Ketika membangun setiap pohon dalam ensambel, ExtraTreesClassifier secara acak memilih subset fitur untuk digunakan dalam proses pemilihan split. Hal ini dapat membantu mengurangi overfitting dan meningkatkan keragaman dalam model.
Pemisahan Node yang Paling Kuat: ExtraTreesClassifier cenderung memilih split yang paling kuat, bahkan jika perbedaan dalam pemilihan tersebut kecil. Ini dapat membuat model lebih tahan terhadap noise dalam data.
Bootstrapping: Seperti pada Random Forests, ExtraTreesClassifier juga menggunakan teknik bootstrapping, yang melibatkan pengambilan sampel acak dengan pengembalian dari data pelatihan untuk setiap pohon.
Dengan kombinasi dari ketiga fitur ini, ExtraTreesClassifier dapat menjadi pilihan yang baik ketika Anda ingin membangun ensambel pohon keputusan yang sangat kuat dan tahan terhadap overfitting. Namun, perlu dicatat bahwa seperti halnya dengan banyak algoritma machine learning, hasilnya dapat bervariasi tergantung pada dataset dan pengaturan yang digunakan.

Hasil sebelum tuning

![image](https://github.com/Mazcho/MODEL_dan_Deployment_Hacktiv8-FinalProject3-Classification-Ensemble-Model/assets/77985996/21f36352-089a-4a36-8ef5-71dd2a4264d7)


Hasil setelah tuning

![image](https://github.com/Mazcho/MODEL_dan_Deployment_Hacktiv8-FinalProject3-Classification-Ensemble-Model/assets/77985996/6d864a47-3c9e-44bf-b25f-2fc1616539f4)



Kalian bisa coba website nya disini : https://hacktiv8finalproject3potensiserangagagaljantung.streamlit.app/
