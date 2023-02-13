PUT /musicdata
{
    # The whole setting here
    "settings": {
        "similarity": {
            "DFR_similarity": {
                "type": "DFR",
                "basic_model": "g",
                "after_effect": "l",
                "normalization": "h2",
                "normalization.h2.c": "3.0"
            }
        },                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        "analysis": {

            # To filter the special character
            "char_filter": {
                "specialCharacterFilter": {
                    "pattern": "[^A-Za-z0-9]",
                    "type": "pattern_replace",
                    "replacement": ""
                }
            },

            "filter": {
                # For a token stream by concatenating adjacent tokens
                "shingle": {
                    "type": "shingle",
                    "min_shingle_size": 3,
                    "max_shingle_size": 3
                },

                # try the synonyms word
                "synonyms_test": {
                    "type": "synonym",
                    "synonyms": [
                        "firm => company",
                        "love, enjoy"
                    ]
                }
            },

            "analyzer": {
                "my_analyzer": {
                    "tokenizer": "standard",
                    "char_filter": [
                        "html_strip", # Strips HTML elements from a text and replaces HTML entities with their decoded value
                        "specialCharacterFilter"
                    ],
                    "filter": [
                        "lowercase",  # change to lower case
                        "unique",  # Removes duplicate tokens
                        "asciifolding",  # Converts alphabetic, numeric, and symbolic characters
                        "trim",  # Trims whitespace from field
                        "stop",  # "english_stop",
                        "synonyms_test",  # synonyms
                        "stemmer"  # "stemmer_test"
                    ]
                },

                "trigram": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": ["lowercase", "shingle"]
                },

                "reverse": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": ["lowercase", "reverse"]
                }
            },

            "tokenizer": {
                # Treats the initial text as a single token and produces N-grams with min/max lenght
                "edge_ngram": {
                    "type": "edge_ngram",
                    "min_gram": 2,
                    "max_gram": 5,
                    "token_chars": [
                        "letter"
                    ]
                }
            }
        }
    },

    "mappings": {

        "properties": {

            "music_name": {
                "type": "text",
                "similarity": "DFR_similarity",
                "fields": {
                    "trigram": {
                        "type": "text",
                        "analyzer": "trigram"
                    },
                    "reverse": {
                        "type": "text",
                        "analyzer": "reverse"
                    }
                },
                "analyzer": "my_analyzer"
            },

            "music_artist": {
                "type": "text",
                "similarity": "DFR_similarity",
                "fields": {
                    "trigram": {
                        "type": "text",
                        "analyzer": "trigram"
                    },
                    "reverse": {
                        "type": "text",
                        "analyzer": "reverse"
                    }
                },
                "analyzer": "my_analyzer"

            },
            
            "music_track": {
                "type": "text",
                "similarity": "DFR_similarity",
                "fields": {
                    "trigram": {
                        "type": "text",
                        "analyzer": "trigram"
                    },
                    "reverse": {
                        "type": "text",
                        "analyzer": "reverse"
                    }
                },
                "analyzer": "my_analyzer"
            },

            "music_genre": {
                "type": "text",
                "similarity": "DFR_similarity",
                "fields": {
                    "trigram": {
                        "type": "text",
                        "analyzer": "trigram"
                    },
                    "reverse": {
                        "type": "text",
                        "analyzer": "reverse"
                    }
                },
                "analyzer": "my_analyzer"
            },

            "music_release": {
                "type": "text",
                "similarity": "DFR_similarity",
                "fields": {
                    "trigram": {
                        "type": "text",
                        "analyzer": "trigram"
                    },
                    "reverse": {
                        "type": "text",
                        "analyzer": "reverse"
                    }
                },
                "analyzer": "my_analyzer"
            },

            "music_producer": {
                "type": "text",
                "similarity": "DFR_similarity",
                "fields": {
                    "trigram": {
                        "type": "text",
                        "analyzer": "trigram"
                    },
                    "reverse": {
                        "type": "text",
                        "analyzer": "reverse"
                    }
                },
                "analyzer": "my_analyzer"
            },
            
            "music_writer": {
                "type": "text",
                "similarity": "DFR_similarity",
                "fields": {
                    "trigram": {
                        "type": "text",
                        "analyzer": "trigram"
                    },
                    "reverse": {
                        "type": "text",
                        "analyzer": "reverse"
                    }
                },
                "analyzer": "my_analyzer"
            },
            
            "music_lyrics": {
                "type": "text",
                "similarity": "DFR_similarity",
                "fields": {
                    "trigram": {
                        "type": "text",
                        "analyzer": "trigram"
                    },
                    "reverse": {
                        "type": "text",
                        "analyzer": "reverse"
                    }
                },
                "analyzer": "my_analyzer"
            }

        }
    }
}

GET /musicdata/_mapping

GET /musicdata/_search
{
    "query": {
        "match_all": {}
    }
}


DELETE /musicdata
