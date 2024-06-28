query_blipzi_com = f"""
           SELECT
                YEAR(date_published) AS year,
                MONTH(date_published) AS month,
                COUNT(game_id) AS number_articles,
                'blipzi.com' AS product,
                'Game' AS content_type,
                'New content' AS content_freshness
            FROM
                games
            WHERE
                status LIKE 'online'
            GROUP BY
                YEAR(date_published),
                MONTH(date_published)
            UNION ALL
            SELECT
                YEAR(date_updated) AS year,
                MONTH(date_updated) AS month,
                COUNT(IF(DATEDIFF(date_updated, date_published) > 0, game_id, NULL)) AS number_articles,
                'blipzi.com' AS product,
                'Game' AS content_type,
                'Update existing content' AS content_freshness
            FROM
                games
            WHERE
                status LIKE 'online'
            GROUP BY
                YEAR(date_updated),
                MONTH(date_updated)
            UNION ALL
            SELECT
                YEAR(date_created) AS year,
                MONTH(date_created) AS month,
                COUNT(id) AS number_articles,
                'blipzi.com' AS product,
                'Categories' AS content_type,
                "" AS content_freshness
            FROM
                categories
            WHERE
                status LIKE 'online'
            GROUP BY
                YEAR(date_created),
                MONTH(date_created)
                    """
