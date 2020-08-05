package com.example.android.khushhali.ui.myCrop;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

public class MyCropViewModel extends ViewModel {

    private MutableLiveData<String> mText;

    public MyCropViewModel() {
        mText = new MutableLiveData<>();
        mText.setValue("This is my crop fragment");
    }

    public LiveData<String> getText() {
        return mText;
    }
}