module.exports = {
  env: {
    browser: true,
    es2021: true,
  },
  extends: ["eslint:recommended", "plugin:react/recommended"],
  parserOptions: {
    ecmaVersion: 12,
    sourceType: "module",
  },
  plugins: ["react"],
  rules: {
    "no-undef": "warn",
    "no-unused-vars": "warn",
    "react/react-in-jsx-scope": "warn",
    "react/jsx-uses-react": "warn",
  },
};
