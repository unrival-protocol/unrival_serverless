Feature: Agent


  Scenario Outline: create a domain
    Given a public key
    When the holder of this public key creates a domain
    # child properties
    Then a child of this domain has the name <name>
    And <promise> is a promise made by this child
    And the child owner has one entity, the address of which is the public key used to create this domain
    # own properties
    And this domain has no name
    And this domain has no parents
    And "I will keep any promise I make." is a promise made by this domain
    And "If one of my ancestors makes a promise, then I also make that promise." is a promise made by this domain

    Examples: 
      | name       | promise                                                    |
      | name       | "I promise to have a name."                                |
      | promise    | "I promise to have a status."                              |
      | promise    | "I promise to be fulfillable."                             |
      | assessment | "I promise to be assessable."                              |
      | owner      | "I promise to assess honestly."                            |
      | owner      | "I promise to only own entities that keep their promises." |

  Scenario: assess an entity
    Given a child domain
    
  Scenario: cannot assess implicit entities
    Given a child domain

  Scenario: add a stakeholder to a domain
    
  Scenario: add a name without a vote
    Given a domain has one stakeholder
    

  Scenario: add a promise without a vote

  Scenario: add child domain without a vote

  Scenario: add a parent domain without a vote

  Scenario: add a name with a vote

  Scenario: add a promise with a vote

  Scenario: add child domain with a vote

  Scenario: add a parent domain with a vote

