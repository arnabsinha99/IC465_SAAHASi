package com.example.android.khushhali.ui.changeLanguage;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModel;
import androidx.lifecycle.ViewModelProviders;

import com.example.android.khushhali.R;
import com.example.android.khushhali.ui.changeLanguage.ChangeLanguageViewModel;

public class ChangeLanguageFragment extends Fragment {

    private ChangeLanguageViewModel changeLanguageViewModel;

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        changeLanguageViewModel =
                ViewModelProviders.of(this).get(ChangeLanguageViewModel.class);
        View root = inflater.inflate(R.layout.fragment_change_language, container, false);
        final TextView textView = root.findViewById(R.id.text_change_language);
        changeLanguageViewModel.getText().observe(this, new Observer<String>() {
            @Override
            public void onChanged(@Nullable String s) {
                textView.setText(s);
            }
        });
        return root;
    }
}