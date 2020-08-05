package com.example.android.khushhali;

import android.graphics.Bitmap;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;

import android.graphics.Bitmap;
import android.os.Bundle;
//import android.support.v7.app.AppCompatActivity;
//import android.support.v7.widget.Toolbar;
import android.widget.ImageView;
import android.widget.TextView;

import java.io.IOException;

public class Result extends AppCompatActivity {

    TextView textView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_result);
        Bitmap imageBitmap = (Bitmap) getIntent().getBundleExtra("imagedata").get("data");


        ImageView imageView = findViewById(R.id.image);
        imageView.setImageBitmap(imageBitmap);

        textView = findViewById(R.id.label);
        textView.setText("result");
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("https://sih-heroku.herokuapp.com/")
                .build();

      /*  final HerokuService service = retrofit.create(HerokuService.class);
        Call<ResponseBody> call = service.hello();
        call.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> _,
                                   Response<ResponseBody> response) {
                try {
                    textView.setText(response.body().string());
                } catch (IOException e) {
                    e.printStackTrace();
                    textView.setText(e.getMessage());
                }
            }

            @Override
            public void onFailure(Call<ResponseBody> _, Throwable t) {
                t.printStackTrace();
                textView.setText(t.getMessage());
            }
        });*/
    }
}
