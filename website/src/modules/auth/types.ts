export type ErrorRegister = {
  email: string;
}

export type ErrorLogin = {
  detail: string;
}

export type StateUser = {
  username: string;
  avatar: string;
}

export type StateToken = {
  refresh: string;
  access: string;
}

export type StateAuthen = {
  user: StateUser;
  token: StateToken;
  authenticated: boolean;
}

