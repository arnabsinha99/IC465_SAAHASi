package com.example.android.khushhali;

import androidx.appcompat.app.AppCompatActivity;
import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.Callback;



import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

public class LoadingPageActivity extends AppCompatActivity {

    int cameraRequestCode = 001;
    TextView resultTextView;
    ImageView imageView;
    File sd;
    File dest;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_loading_page);

        resultTextView = findViewById(R.id.loading_textView);
        imageView = findViewById(R.id.loading_imageView);

        Intent cameraIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        startActivityForResult(cameraIntent,cameraRequestCode);

    }
    @Override
    protected void onActivityResult (int requestCode, int resultCode, Intent data) {
        if (requestCode == cameraRequestCode && resultCode == RESULT_OK) {
            super.onActivityResult(requestCode, resultCode, data);
            Bundle extras = data.getExtras();

           /* File f = new File(Environment.getExternalStorageDirectory(), "crop.txt");

            try {
                    f.createNewFile();
            }
            catch(IOException e)
            {
                e.printStackTrace();
            }


            Bitmap bitmap = imageBitmap;
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            bitmap.compress(Bitmap.CompressFormat.JPEG, 0 , bos);
            byte[] bitmapdata = bos.toByteArray();


            FileOutputStream fos = null;


            try {
                fos = new FileOutputStream(f);
            } catch (FileNotFoundException e) {
                Log.i("hello","in first catch");
                e.printStackTrace();
            }
            try {
                fos.write(bitmapdata);
                fos.flush();
                fos.close();
                Log.i("hello","in secong try");
            } catch (IOException e) {
                Log.i("hello","in secong catch");
                e.printStackTrace();
            }*/
            String filename = "pippo";
            File sd = Environment.getExternalStorageDirectory();
            File dest = new File(sd, filename);

            Bitmap bitmap = (Bitmap)data.getExtras().get("data");
            try {
                FileOutputStream out = new FileOutputStream(dest);
                bitmap.compress(Bitmap.CompressFormat.PNG, 90, out);
                out.flush();
                out.close();
            } catch (Exception e) {
                e.printStackTrace();
            }

            Retrofit retrofit = NetworkClient.getRetrofit();

            RequestBody reqFile = RequestBody.create(MediaType.parse("image/*"), dest);
            MultipartBody.Part body = MultipartBody.Part.createFormData("file", dest.getName(), reqFile);

            //HerokuService service = new Retrofit.Builder().baseUrl("https://sih-heroku.herokuapp.com/").build().create(HerokuService.class);

            HerokuService service = retrofit.create(HerokuService.class);
            Call<ResponseBody> req = service.postImage(body);
            req.enqueue(new Callback<ResponseBody>() {
                @Override
                public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                    // Do Something with response
                    Log.i("abc","abc");
                    resultTextView.setText("Results");
                }

                @Override
                public void onFailure(Call<ResponseBody> call, Throwable t) {
                    //failure message
                    Log.i("abc","tyughio");
                    t.printStackTrace();
                }
            });
        }
    }
}




