package com.example.android.khushhali.ui.changeLanguage;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

public class ChangeLanguageViewModel extends ViewModel {

    private MutableLiveData<String> mText;

    public ChangeLanguageViewModel() {
        mText = new MutableLiveData<>();
        mText.setValue("This is change language fragment");
    }

    public LiveData<String> getText() {
        return mText;
    }
}