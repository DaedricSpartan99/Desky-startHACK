import { createSlice, PayloadAction } from "@reduxjs/toolkit";

/*
 * export interface AccountResponse {
  user: {
    id: string;
    username: string;
    is_active: boolean;
    created: Date;
    updated: Date;
  };
  access: string;
  refresh: string;
}
 *
 *
 */

/*
 * type State = {
      token: string | null;
      refreshToken: string | null;
      account: AccountResponse | null;
    };
 *
 */

const initialState = { token: null, refreshToken: null, account: null };

const authSlice = createSlice({
  name: "auth",
  initialState,
  reducers: {
    // action : PayloadAction<{ token: string; refreshToken: string }>
    setAuthTokens(state,action) {
      state.refreshToken = action.payload.refreshToken;
      state.token = action.payload.token;
    },
    setAccount(state, action) {
      state.account = action.payload;
    },
    logout(state: State) {
      state.account = null;
      state.refreshToken = null;
      state.token = null;
    },
  },
});

export default authSlice;
