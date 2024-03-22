import { createSlice, PayloadAction } from "@reduxjs/toolkit";

const initialState = { 
  location: null, 
};

const searchSlice = createSlice({
  name: "search",
  initialState,
  reducers: {
    setLocation: (state,action) => {
      state.location = action.payload;
    },
  },
});

export const { setLocation } = searchSlice.actions;

export default searchSlice.reducer;
