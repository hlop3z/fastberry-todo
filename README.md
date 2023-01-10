# Fastberry-Todo

Todo Example for **Fastberry**

## Install

```sh
pdm install
```

## Run

```sh
pdm app run
```

## Client

```graphql
fragment ErrorFields on Error {
  error
  meta
  messages {
    field
    text
    type
  }
}

fragment PageFields on PageInfo {
  length
  pages
  extra
}

fragment ModelFields on Task {
  id
  title
  description
  status
}

mutation Create {
  create(
    form: {
      title: "First App"
      description: "create an example app."
      status: "open"
    }
  ) {
    ... on Task {
      ...ModelFields
    }
    ... on Error {
      ...ErrorFields
    }
  }
}

mutation Update {
  update(item: "MTo6YTU1ZTUzMmVhYjAyOGI0Mg==", status: "close") {
    ... on Task {
      ...ModelFields
    }
    ... on Error {
      ...ErrorFields
    }
  }
}

mutation Delete {
  delete(item: "Mjo6M2VmOWFiYmI1ZGY1YjY0MQ==")
}

query Detail {
  item: detail(item: "MTo6YTU1ZTUzMmVhYjAyOGI0Mg==") {
    ...ModelFields
  }
}

query Search {
  list: search(status: "open") {
    edges {
      node {
        ...ModelFields
      }
    }
    pageInfo {
      ...PageFields
    }
  }
}

query All {
  list: search(status: null) {
    edges {
      node {
        ...ModelFields
      }
    }
    pageInfo {
      ...PageFields
    }
  }
}
```
