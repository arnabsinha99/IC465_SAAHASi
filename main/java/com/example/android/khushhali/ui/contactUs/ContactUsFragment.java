package com.example.android.khushhali.ui.contactUs;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProviders;

import com.example.android.khushhali.LoadingPageActivity;
import com.example.android.khushhali.R;

public class ContactUsFragment extends Fragment {

    private ContactUsViewModel contactUsViewModel;
    Button buttonWhatsapp;
    Button buttonVoiceCall;

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        contactUsViewModel =
                ViewModelProviders.of(this).get(ContactUsViewModel.class);
        View root = inflater.inflate(R.layout.fragment_contact_us, container, false);
        final TextView textView = root.findViewById(R.id.text_contact_us);
        contactUsViewModel.getText().observe(this, new Observer<String>() {
            @Override
            public void onChanged(@Nullable String s) {
                textView.setText(s);
            }
        });
        return root;
    }
    @Override
    public void onViewCreated(View view, Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        buttonWhatsapp = getView().findViewById(R.id.button_whatsapp);
        buttonVoiceCall = getView().findViewById(R.id.button_voice_call);

        buttonWhatsapp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String url = "https://api.whatsapp.com/send?phone="+"+918586000240";
                Intent intent = new Intent(Intent.ACTION_VIEW);
                intent.setData(Uri.parse(url));
                startActivity(intent);
            }
        });
        buttonVoiceCall.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(Intent.ACTION_DIAL);
                intent.setData(Uri.parse("tel:8586000240"));
                startActivity(intent);
            }
        });
    }
}