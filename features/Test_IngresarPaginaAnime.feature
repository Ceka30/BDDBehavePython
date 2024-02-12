Feature: Ingresar a Pagina de Anime

  Background:
    Given Abrir el navegador con URL de Google

  Scenario Outline: Ingresar a pagina de Anime
      And Buscar "<texto>" en buscador
      When Seleccionar resultado de la busqueda "<texto>"
      Then Ingresar exitosamente a la pagina "<texto>"
      Examples:
      | texto |
      | AnimeFLV |
      | Crunchyroll |