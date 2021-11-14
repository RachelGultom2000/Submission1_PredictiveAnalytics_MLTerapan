![](img/stroke_logo.jpeg)

# Submission1_PredictiveAnalytics_MLTerapan
Submission 1 - ML Terapan

### Metode : 
- Logistic Regression
- Random Forest

---

## Problem Domain

![](img/statistik_stroke.png)

**Penyakit Stroke menjadi salah satu penyebab banyakknya angka kematian di banyak negara termasuk Indonesia.**

Berdasarkan hasil pemeriksaan yang dilakukan oleh dokter di Indonesia, rasio penderita penyakit stroke merupakan yang paling tinggi grafiknya pada tahun 2014.Stroke atau cedera cerebrovaskuler adalah kehilangan fungsi otak yang diakibatkan oleh berhentinya suplai darah ke bagian otak.Atau lebih mudahnya kondisi yang terjadi ketika pasokan darah ke otak berkurang akibat penyumbatan (stroke iskemik) atau pecahnya pembuluh darah (stroke hemoragik).

Menurut WHO stroke adalah adanya tanda-tanda klinik yang berkembang cepat akibat gangguan fungsi otak fokal (atau global) dengan
gejala-gejala yang berlangsung selama 24 jam atau lebih yang menyebabkan kematian tanpa adanya penyebab lain yang jelas selain
vaskuler.

**Berdasarkan permasalahan diatas,maka penulis membuat sebuah penelitian dengan menciptakan aplikasi 
yang dapat memprediksi kemungkinan sesorang mengidap penyakit stroke dengan mempertimbangkan banyak faktor
seperti jenis kelamin,usia,beban pekerjaan,keaktifan merokok,berat badan dan lain lain**

Maka dari itu,judul untuk penelitian ini adalah "Prediksi Penyakit Stroke dengan Menggunakan Metode Logistic Regression",sehingga diharapkan hasil penelitian ini dapat memberikan edukasi dini terhadap masyarakat mengenai pentingnya menerapkan hidup sehat agar tidak terjadi lagi kematian akibat penyakit stroke di Indonesia.


---

## Business Understanding

### Problem Statement
- Bagaimana cara melakukan prediksi terhadap si penderita apakah beresiko terkena penyakit stroke atau tidak dalam setidaknya 10 tahun kedepan dari statistik kesehatannya?

### Goals
- Melakukan prediksi atau klasifikasi apakah seseorang beresiko menderita penyakit stroke atau tidak setidaknya dalam 10 tahun kedepan dari statistik kesehatannya.

### Solution Statement
- **Solusi Pertama** adalah dengan metode **Logistic Regression**, dimana metode ini merupakan metode yang cukup efektif dalam melakukan klasifikasi yang outputnya hanya 1 dan 0 atau True/False.
- **Solusi Kedua** adalah dengan metode **Random Forest**,dimana sesuai namanya yang berarti 'hutan acak', metode ini bekerja dengan mengambil banyaknya subpohon atau estimators(decision) dan kemudian membentuk 1 pohon utuh untuk klasifikasinya. 
- Adapun **Dua Metrik** yang digunakan adalah : 
    - **Akurasi** = merupakan acuan terhadap hasil prediksi,berasal dari sklearn dengan formula Accuracy/score.
    - **Mean Squared Error** (MSE) = merupakan acuan terhadap pengurangan nilai aktual ,berasal dari sklearn dengan nama MSE.
 
## Data Understanding
Data yang digunakan berasal dari Kaggle dengan nama **Stroke Prediction Dataset** 
atau dapat didownload [disini](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset)

- Overview Dataset (Pendekatan Statistik) : 
  - Dataset terdiri dari 5111 baris/record data dan setiap record memiliki 12 kolom data atau berdimensi 5111 rows x 12 columns.
    
    ![](img/pre_pro.PNG)
    
  - Dataset juga mengandung missing value atau nilai NaN di beberapa kolom salah satunya kolom bmi yang memiliki jumlah terbesar untuk nilai NaN.
  
    ![](img/nan_val.PNG)
    
 - Fitur Dataset (Pendekatan Linguistik):
    - Demografi singkat mengenai setiap kolom 
       - Gender         : male or female
       - Age            : Age of the patient
    - Perilaku Responden 
       - Hypertension   : Memiliki penyakit Hipertensi atau tidak,ditandai dengan 1 untuk True dan 0 untuk False.
       - Heart_Disease  : Memiliki penyakit Hati atau tidak,ditandai dengan 1 untuk True dan 0 untuk False.
       - Ever_Married   : Apakah sudah menikah atau belum.
       - Work_Type      : Tipe,jenis atau beban pekerjaannya seperti apa?
       - Residence_Type : Dimana lokasi tempat tinggalnya? apakah di perkotaan atau pedesaan.
       - Avg_Glucose_Level : Angka gulanya mencapai tingkat berapa?
       - BMI            : Body Mass Index (berat badan)
       - Smoking_Status : Apakah sering merokok? atau baru pertama kali melakukannya?
    
---


# Data Preparation
- Menghapus kolom yang kurang relevan atau baik untuk prediksi seperti kolom yang mengandung tipe data string.
- Mengisi missing value (NaN) dengan nilai median,dengan tujuan membantu "menormalkan" data yang hilang.
- Proses standarisasi membantu dalam membuat fitur data menjadi bentuk yang lebih mudah diolah oleh algoritma.StandardScaller melakukan proses standarisasi dengan mengurangkan mean atau nilai rata rata kemudian membaginya dengan standar deviasi untuk menggeser nilai distribusi.Menghasilkan distribusi dengan standar deviasi sama dengan 1 dan mean sama dengan 0.
- Scalling dengan Standard Scaler dari sklearn,dengan tujuan membuat numerik dari data agar dapat diproses atau dibaca oleh mesin.
- Train/Test split atau train_test_split merupakan salah satu metode yang digunakan untuk mengevaluasi performa model machine learning.Metode ini membagi dataset menjadi 2 bagian yaitu dataset untuk training dan dataset untuk testing dan sudah ditentukan proporsi pembagiannya,umumnya data train 80% dan data test 20%, atau data train 75% dan data test 25%,tergantung kebutuhan.Penggunaan train_test_split ini juga sangat dianjurkan untuk dataset yang berukuran besar atau bisa juga untuk multiclass.
**Suatu model dikatakan baik jika akurasi yang dihasilkan tinggi dan yang pasti tidak sering terjadi overfitting**

---

## Modelling

Pada percobaan ini,aplikasi menggunakan 2 metode atau algoritma dalam membentuk prediksinya,yaitu : 
- Logistic Regression
  Merupakan sebuah algoritma klasifikasi untuk mencari hubungan antara fitur diskrit atau kontinu dengan probabilitas hasil output disktit tertentu.
  
    - Rumus(Formula) secara umumnya yaitu : 
    
      ![](img/rumus_logistik.jpg)
     
      Dari gambar diatas,maka kesimpulannya adalah bobot dari tiap variabel akan dihitung dalam setiap iterasi atau perulangan untuk mencari nilai yang paling optimal dan bias dari variabel .
     
- Random Forest
  Merupakan kombinasi dari  masing – masing tree yang baik kemudian dikombinasikan ke dalam satu model agar membentuk sebuah prediksi.
  
     - Rumus(Formula) secara umumnya yaitu : 
     
       ![](img/r_forest.png)
       
       Dari gambar diatas,kesimpulannya adalah bahwa setiap tree menciptakan penduga masing masing atau disebut n_estimators(subpohon) dalam mengambil sebuah keputusan yang berbeda.Dari situlah,kemudian akan digabungkan agar membentuk 1 pohon utuh (akhir) agar dapat memberikan hasil klasifikasi dan prediksinya.
  
Penggunaan Model
Berdasarkan hasil yang didapat dari proses modellingnya,Logistic Regression memiliki akurasi yang jauh lebih tinggi dibandingkan dengan Random Forest.

Penggunaan Parameter 
Parameter untuk algoritma Logistic Regression adalah **max_iter=1000**,dimana max_iter adalah jumlah maksimum iterasi atau perulangan yang diambil oleh si solver(pemecah masalah),sedangkan untuk algoritma Random Forest menggunakan **n_estimators=1000, max_depth=16, random_state=55, n_jobs=1** sebagai parameternya,dimana n_estimators menunjukkan banyaknya pohon atau sub-pohon dalam hutan,max_depth menunjukkan kedalaman maksimum pohon,random_state adalah seed yang digunakan oleh generator angka acak ,biasanya dalam bentuk int dan n_jobs adalah jumlah pekerjaan yang harus dijalankan secara pararel dalam menunjukkan prediksinya.


Tahapan yang dilakukan : 
1. Mendefinisikan metode atau algoritma yang digunakan ,disini adalah Logistic Regression & Random Forest.
2. Melakukan train data atau fitting menggunakan kedua algoritma tersebut dengan dataset yang sama yaitu dataset trainning.
3. Melakukan testing pada dataset test agar mendapatkan hasil untuk implementasi ke model.

Dari hasil yang didapat, dapat disimpulkan bahwa algoritma Logistic Regression memiliki akurasi yang jauh lebih baik daripada algoritma Random Forest,berikut detailnya:
- Logistic Regression : 0.937 (93%)
- Random Forest : 0.039 (3.9%) 

        ![](img/akurasi_algo.PNG)


      
## Evaluasi
- Penggunaan algoritma Logistic Regression terbukti lebih baik berdasarkan matrik yang diberikan,tetapi terdapat anomali berupa MSE yang mengatakan bahwa Logistic Regression mempunyai grafik data train dan test yang lebih banyak dibandingkan dengan Random Forest.Dari sini bisa disimpulkan bahwa,algoritma mempengarungi kinerja mesin dalam membentuk prediksi.
 Dari hasil ini,maka akan ditetapkan algoritma Logistic Regression sebagai acuan yang akan digunakan untuk mendapatkan hasil prediksi atau akurasinya.
 
Metrik

- Metrik,merupakan acuan terhadap suatu nilai dalam merepresentasikan performa model yang dihasilkan.

  ![](img/metrik.png)
  
  
- Akurasi 

    - Akurasi merupakan metrik atau acuan yang paling sering terlihat pada pemodelan.Berbentuk angka atau nilai,ini menampilkan bagaimana hasil prediksi terhadap sebuah model.

      ![](img/rumus_akurasi.jpg)
      
    - Berikut perbandingan akurasi dari kedua model : 
    
      ![](img/akurasi.PNG)
      
- MSE (Mean Squarred Error)
    
    - MSE (Mean Squarred Error) merepresentasikan rata – rata kesalahan (error) absolut antara hasil peramalan dengan nilai sebenarnya
    
    - Berikut perbandingan MAE dari kedua model : 
    
      ![](img/plot.PNG)
      
 
 Referensi tambahan yang berhubungan dengan kedua metode : 
 
- Bobot & Bias
  
   - Bobot adalah faktor penting agar jaringan dapat melakukan generalisasi terhadap data yang dilatih.
   
   - Bias,mirip dengan bobot,merupakan penyeimbang atau penetral dari bobot yang ada untuk mencapai nilai standarnya.
   
   - Berikut perbandingan Bobot & Bias dari kedua model : 
   
     ![](img/bias.PNG)
     
- Confussion Matrix
  
  - Berdasarkan hasil metrik yang didapatkan dengan format TP, FP, TN, FN pada model.
  
    ![](img/matrix.PNG)
    
 - Heatmap Visualisasi
 
   - Berikut model visualisasi yang didapatkan dari keseluruhan proses dengan menampilkan frekuensinya.
   
     ![](img/heatmap.PNG)


### Daftar Pustaka : 

- Hosmer, David W. and Stanley Lemeshow. 2000. Applied Logistic Regression Second Edition. New
York: John Wiley & Sons, Inc
- Peng, Chao-Ying Joanne dkk. 2002. “An Introduction to Logistic Regression Analysis and Reporting”.
The Journal of Educational Research Indiana University Bloomington Vol. 96 No. 1.


  
  
   
