import { configureStore, getDefaultMiddleware } from "@reduxjs/toolkit";
import searchSlice from "./slices/search";

const searchStore = configureStore({
  reducer: {
    searchSlice
  }
});

export default searchStore;
