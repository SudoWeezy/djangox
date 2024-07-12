# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

## HTTP Request

* GET corresponds with “getting” a representation for a resource from a URL: it is a pure read, with no mutation of the resource.

* POST submits an entity (or data) to the given resource, often creating or mutating the resource and causing a state change.

* PUT submits an entity (or data) to the given resource for update or replacement, again likely causing a state change.

* PATCH is similar to PUT but implies a partial update and state change rather than a complete replacement of the entity.

* DELETE deletes the given resource.

## HTTP Response Code

* 100-199 Informational responses that provide information about how the server is processing the response.

* 200-299 Successful responses indicating that the request succeeded.

* 300-399 Redirection responses indicating that the request should be sent to some other URL.

* 400-499 Client error responses indicating that the client made some sort of bad request (e.g., asking for something that didn’t exist in the case of 404 errors).

* 500-599 Server error responses indicating that the server encountered an error internally as it attempted to respond to the request.

### Specific codes

* 200 **OK** The HTTP request succeeded.

* 301 **Moved Permanently** The URL for the requested resource has moved to a new location permanently, and the new URL will be provided in the Location response header.

* 302 **Found** The URL for the requested resource has moved to a new location temporarily, and the new URL will be provided in the Location response header.

* 303 **See Other** The URL for the requested resource has moved to a new location, and the new URL will be provided in the Location response header. Additionally, this new URL should be retrieved with a GET request.

* 401 **Unauthorized** The client is not yet authenticated (yes, authenticated, despite the name) and must be authenticated to retrieve the given resource.

* 403 **Forbidden** The client does not have access to this resource.

* 404 **Not Found** The server cannot find the requested resource.

* 500 **Internal Server Error** The server encountered an error when attempting to process the response.

## Libraries

[Alpine.js](https://alpinejs.dev/)
[Tailwind.css](https://tailwindcss.com/)
[Django](https://www.djangoproject.com/)
[Htmx](https://v1.htmx.org/)
[Icon](https://heroicons.com/)