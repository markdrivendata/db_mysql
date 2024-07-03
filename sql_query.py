QUERIES = {
    'bibliaon_com': f"""
        SELECT
            YEAR(data_publicacao) AS year,
            MONTH(data_publicacao) AS month,
            COUNT(id) AS number_articles,
            'bibliaon.com' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            artigos
        WHERE
            estado LIKE 'publicado'
        GROUP BY
            YEAR(data_publicacao),
            MONTH(data_publicacao)
        UNION ALL
        SELECT
            YEAR(data_atualizacao) AS year,
            MONTH(data_atualizacao) AS month,
            COUNT(IF(DATEDIFF(data_atualizacao, data_publicacao) > 0, id, NULL)) AS number_articles,
            'bibliaon.com' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            artigos
        WHERE
            estado LIKE 'publicado'
        GROUP BY
            YEAR(data_atualizacao),
            MONTH(data_atualizacao)
        UNION ALL
        SELECT
            YEAR(dtatualizacao) AS year,
            MONTH(dtatualizacao) AS month,
            COUNT(id) AS number_articles,
            'bibliaon.com' AS product,
            'Temas' AS content_type,
            "" AS content_freshness
        FROM
            pesquisas
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(dtatualizacao),
            MONTH(dtatualizacao)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(id) AS number_articles,
            'bibliaon.com' AS product,
            'Passagens' AS content_type,
            "" AS content_freshness
        FROM
            passagens
        WHERE
            bloqueado = 0 
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
""",

    'calendarr_com': f"""
            SELECT
                YEAR(data_atualizacao) AS year,
                MONTH(data_atualizacao) AS month,
                COUNT(IF(DATEDIFF(data_atualizacao, data_publicacao) > 0, id, NULL)) AS number_articles,
                'calendarr.com' AS product,
                'Article' AS content_type,
                'Update existing content' AS content_freshness
            FROM
                artigos
            WHERE
                estado LIKE 'publicado'
            GROUP BY
                YEAR(data_atualizacao),
                MONTH(data_atualizacao)
            UNION ALL
            SELECT
                YEAR(data_publicacao) AS year,
                MONTH(data_publicacao) AS month,
                COUNT(id) AS number_articles,
                'calendarr.com' AS product,
                'Article' AS content_type,
                'New content' AS content_freshness
            FROM
                artigos
            WHERE
                estado LIKE 'publicado'
            GROUP BY
                YEAR(data_publicacao),
                MONTH(data_publicacao)
            UNION ALL
            SELECT
                YEAR(date_created) AS year,
                MONTH(date_created) AS month,
                COUNT(id_holiday) AS number_articles,
                'calendarr.com' AS product,
                IF(seo_url IS NULL, 'Date without description', 'Date with description') AS content_type,
                'New content' AS content_freshness
            FROM
                holidays
            WHERE 
                status LIKE 'online'
            GROUP BY
                YEAR(date_created),
                MONTH(date_created),
                IF(seo_url IS NULL, 'Date without description', 'Date with description')
            UNION ALL
            SELECT
                YEAR(date_updated) AS year,
                MONTH(date_updated) AS month,
                COUNT(IF(DATEDIFF(date_updated, date_created) > 0, id_holiday, NULL)) AS number_articles,
                'calendarr.com' AS product,
                IF(seo_url IS NULL, 'Date without description', 'Date with description') AS content_type,
                'Update existing content' AS content_freshness
            FROM
                holidays
            WHERE 
                status LIKE 'online'
            GROUP BY
                YEAR(date_updated),
                MONTH(date_updated),
                IF(seo_url IS NULL, 'Date without description', 'Date with description')
""",

    'culturagenial_com': f"""
        SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'culturagenial.com' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, id, NULL)) AS number_articles,
            'culturagenial.com' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
""",

    'culturagenial_com_es': f"""
        SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'culturagenial.com/es/' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, id, NULL)) AS number_articles,
            'culturagenial.com/es/' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
""",

    'cumplegenial_com': f"""
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated,date_published) > 0, id, NULL)) AS number_articles,
            'cumplegenial.com' AS product,
            'Message' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            messages
        WHERE 
            status = 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
        UNION ALL
        SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'cumplegenial.com' AS product,
            'Message' AS content_type,
            'New content' AS content_freshness
        FROM
            messages
        WHERE 
            status = 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'cumplegenial.com' AS product,
            'List' AS content_type,
            "New content" content_freshness
        FROM
            lists
        WHERE 
            status = 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated,date_published) > 0, id, NULL)) AS number_articles,
            'cumplegenial.com' AS product,
            'List' AS content_type,
            "Update existing content" content_freshness
        FROM
            lists
        WHERE 
            status = 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
""",

    'dicio_com_br': f"""
        SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'dicio.com.br' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online' 
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, id, NULL)) AS number_articles,
            'dicio.com.br' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online' 
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
        UNION ALL
        SELECT
            YEAR(date_update) AS year,
            MONTH(date_update) AS month,
            COUNT(IF(revised = 1, id, NULL)) AS number_articles,
            'dicio.com.br' AS product,
            'Word' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            words
        WHERE 
            is_published = 1
        GROUP BY
            YEAR(date_update),
            MONTH(date_update)
        UNION ALL
        SELECT
            YEAR(date_create) AS year,
            MONTH(date_create) AS month,
            COUNT(IF(revised = 0, id, NULL)) AS number_articles,
            'dicio.com.br' AS product,
            'Word' AS content_type,
            'New content' AS content_freshness
        FROM
            words
        WHERE 
            is_published = 1
        GROUP BY
            YEAR(date_create),
            MONTH(date_create)
        UNION ALL
        SELECT
            YEAR(dtpublicado) AS year,
            MONTH(dtpublicado) AS month,
            COUNT(id) AS number_articles,
            'dicio.com.br' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            dicio_duvidas
        WHERE
            status LIKE 'online' 
        GROUP BY
            YEAR(dtpublicado),
            MONTH(dtpublicado)
        UNION ALL
        SELECT
            YEAR(dtupdate) AS year,
            MONTH(dtupdate) AS month,
            COUNT(IF(DATEDIFF(dtupdate, dtpublicado) > 0, id, NULL)) AS number_articles,
            'dicio.com.br' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            dicio_duvidas
        WHERE
            status LIKE 'online' 
        GROUP BY
            YEAR(dtupdate),
            MONTH(dtupdate)
""",

    'dicionarionomesproprios_com_br': f"""
        SELECT
            YEAR(data_publicacao) AS year,
            MONTH(data_publicacao) AS month,
            COUNT(id) AS number_articles,
            'dicionariodenomesproprios.com.br' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            artigos
        WHER
            estado LIKE 'online'
        GROUP BY
            YEAR(data_publicacao),
            MONTH(data_publicacao)
        UNION ALL
        SELECT
            YEAR(data_atualizacao) AS year,
            MONTH(data_atualizacao) AS month,
            COUNT(IF(DATEDIFF(data_atualizacao, data_publicacao) > 0, id, NULL)) AS number_articles,
            'dicionariodenomesproprios.com.br' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            artigos
        WHERE
            estado LIKE 'online'
        GROUP BY
            YEAR(data_atualizacao),
            MONTH(data_atualizacao)
        UNION ALL
        SELECT
            YEAR(dtupdate) AS year,
            MONTH(dtupdate) AS month,
            COUNT(IF(revisado = 1, id, NULL)) AS number_articles,
            'dicionariodenomesproprios.com.br' AS product,
            'Name' AS content_type,
            "Update existing content" AS content_freshness
        FROM
            nomes
        WHERE
            status LIKE 'online' 
        GROUP BY
            YEAR(dtupdate),
            MONTH(dtupdate)
        UNION ALL
        SELECT
            YEAR(dtinsert) AS year,
            MONTH(dtinsert) AS month,
            COUNT(IF(revisado = 0, id, NULL)) AS number_articles,
            'dicionariodenomesproprios.com.br' AS product,
            'Name' AS content_type,
            "New content" AS content_freshness
        FROM
            nomes
        WHERE
            status LIKE 'online' 
        GROUP BY
            YEAR(dtinsert),
            MONTH(dtinsert)
""",

    'dicionariopopular_com': f"""
        SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'dicionariopopular.com' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, id, NULL)) AS number_articles,
            'dicionariopopular.com' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
""",

    'happybirthdaywisher_com': f"""
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, id, NULL)) AS number_articles,
            'happybirthdaywisher.com' AS product,
            'Message' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            messages
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
        UNION ALL
        SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'happybirthdaywisher.com' AS product,
            'Message' AS content_type,
            'New content' AS content_freshness
        FROM
            messages
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
            SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'happybirthdaywisher.com' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online' 
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, id, NULL)) AS number_articles,
            'happybirthdaywisher.com' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
        UNION ALL
        SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'happybirthdaywisher.com' AS product,
            'List' AS content_type,
            "New content" AS content_freshness
        FROM
            lists
        WHERE
            status LIKE 'online' 
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, id, NULL)) AS number_articles,
            'happybirthdaywisher.com' AS product,
            'List' AS content_type,
            "Update existing content" AS content_freshness
        FROM
            lists
        WHERE
            status LIKE 'online' 
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)

""",

    'jogos360_com_br': f"""
        SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(game_id) AS number_articles,
            'jogos360.com.br' AS product,
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
            'jogos360.com.br' AS product,
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
            'jogos360.com.br' AS product,
            'Categories' AS content_type,
            "" AS content_freshness
        FROM
            categories
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_created),
            MONTH(date_created)
""",

    'ligadosgames_com': f"""
       SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'ligadosgames.com' AS product,
            'Game' AS content_type,
            'New content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, id, NULL)) AS number_articles,
            'ligadosgames.com' AS product,
            'Game' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
""",

    'mensagemaniversario_com_br': f"""
       SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(list_id) AS number_articles,
            'mensagemaniversario.com.br' AS product,
            'List' AS content_type,
            "New content" AS content_freshness
        FROM
            lists
        WHERE
            status LIKE 'published' 
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_update) AS year,
            MONTH(date_update) AS month,
            COUNT(IF(DATEDIFF(date_update, date_published) > 0, list_id, NULL)) AS number_articles,
            'mensagemaniversario.com.br' AS product,
            'List' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            lists
        WHERE
            status LIKE 'published' 
        GROUP BY
            YEAR(date_update),
            MONTH(date_update)
        UNION ALL
        SELECT
            YEAR(date_creation) AS year,
            MONTH(date_creation) AS month,
            COUNT(message_id) AS number_articles,
            'mensagemaniversario.com.br' AS product,
            'Message' AS content_type,
            'New content' AS content_freshness
        FROM
            messages
        WHERE
            status LIKE 'published' 
        GROUP BY
            YEAR(date_creation),
            MONTH(date_creation)
        UNION ALL
        SELECT
            YEAR(date_update) AS year,
            MONTH(date_update) AS month,
            COUNT(IF(DATEDIFF(date_update, date_creation) > 0, message_id, NULL)) AS number_articles,
            'mensagemaniversario.com.br' AS product,
            'Message' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            messages
        WHERE
            status LIKE 'published' 
        GROUP BY
            YEAR(date_update),
            MONTH(date_update)
""",

    'mundodasmensagens_com': f"""
        SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'mundodasmensagens.com' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, id, NULL)) AS number_articles,
            'mundodasmensagens.com' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
        UNION ALL
        SELECT
            YEAR(date_publish) AS year,
            MONTH(date_publish) AS month,
            COUNT(categoria_id) AS number_articles,
            'mundodasmensagens.com' AS product,
            'List' AS content_type,
            "New content" AS content_freshness
        FROM
            categorias
        WHERE
            estado LIKE 'publicado'
        GROUP BY
            YEAR(date_publish),
            MONTH(date_publish)
        UNION ALL
        SELECT
            YEAR(date_update) AS year,
            MONTH(date_update) AS month,
            COUNT(IF(DATEDIFF(date_update, date_publish) > 0, categoria_id, NULL)) AS number_articles,
            'mundodasmensagens.com' AS product,
            'List' AS content_type,
            "Update existing content" AS content_freshness
        FROM
            categorias
        WHERE
            estado LIKE 'publicado'
        GROUP BY
            YEAR(date_update),
            MONTH(date_update)
        UNION ALL
        SELECT
            YEAR(data_actualizado) AS year,
            MONTH(data_actualizado) AS month,
            COUNT(IF(data_actualizado != "0000-00-00 00:00:00", texto_id, NULL)) AS number_articles,
            'mundodasmensagens.com' AS product,
            'Message' AS content_type,
            "Update existing content" AS content_freshness
        FROM
            textos
        WHERE
            estado LIKE 'publicado'
        GROUP BY
            YEAR(data_actualizado),
            MONTH(data_actualizado)
        UNION ALL
        SELECT
            YEAR(data_publicado) AS year,
            MONTH(data_publicado) AS month,
            COUNT(IF(data_actualizado != "0000-00-00 00:00:00", texto_id, NULL)) AS number_articles,
            'mundodasmensagens.com' AS product,
            'Message' AS content_type,
            "New content" AS content_freshness
        FROM
            textos
        WHERE
            estado LIKE 'publicado'
        GROUP BY
            YEAR(data_publicado),
            MONTH(data_publicado)
""",

    'pensador_com': f"""
        SELECT
            YEAR(data_criacao) AS year,
            MONTH(data_criacao) AS month,
            COUNT(id) AS number_articles,
            'pensador.com' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            artigos
        WHERE
            estado LIKE 'publicado'
        GROUP BY
            YEAR(data_criacao),
            MONTH(data_criacao)
        UNION ALL
        SELECT
            YEAR(data_atualizacao) AS year,
            MONTH(data_atualizacao) AS month,
            COUNT(IF(DATEDIFF(data_atualizacao, data_criacao) > 0, id, NULL)) AS number_articles,
            'pensador.com' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            artigos
        WHERE
            estado LIKE 'publicado'
        GROUP BY
            YEAR(data_atualizacao),
            MONTH(data_atualizacao)
        UNION ALL
        SELECT
            YEAR(dtupdate) AS year,
            MONTH(dtupdate) AS month,
            COUNT(IF(revisado LIKE '0' AND tipo LIKE 'categoria', id, NULL)) AS number_articles,
            'pensador.com' AS product,
            'List' AS content_type,
            "New content" AS content_freshness
        FROM
            pesquisas
        WHERE
            lixo LIKE '0'
        GROUP BY
            YEAR(dtupdate),
            MONTH(dtupdate)
        UNION ALL
        SELECT
            YEAR(dtupdate) AS year,
            MONTH(dtupdate) AS month,
            COUNT(IF(revisado LIKE '1' AND tipo LIKE 'categoria', id, NULL)) AS number_articles,
            'pensador.com' AS product,
            'List' AS content_type,
            "Update existing content" AS content_freshness
        FROM
            pesquisas
        WHERE
            lixo LIKE '0'
        GROUP BY
            YEAR(dtupdate),
            MONTH(dtupdate)
""",

    'significados_com_br': f"""
        SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'significados.com.br' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, id, NULL)) AS number_articles,
            'significados.com.br' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
""",

    'sinonimos_com_br': f"""
       SELECT
            YEAR(dt) AS year,
            MONTH(dt) AS month,
            COUNT(id) AS number_articles,
            'sinonimos.com.br' AS product,
            'Word' AS content_type,
            IF(revisado = 0, 'New content', 'Update existing content') AS content_freshness
        FROM
            palavras
        GROUP BY
            YEAR(dt),
            MONTH(dt),
            IF(revisado = 0, 'New content', 'Update existing content')
""",

    'bibliaon_com_es': f"""
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, id, NULL)) AS number_articles,
            'bibliaon.com/es/' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
        UNION ALL
        SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'bibliaon.com/es/' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'bibliaon.com/es/' AS product,
            'Passagens' AS content_type,
            "" AS content_freshness
        FROM
            bible_passages
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
""",

    'todamateria_com_br': f"""
        SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'todamateria.com.br' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            posts
        WHERE
            published = 1
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_modified) AS year,
            MONTH(date_modified) AS month,
            COUNT(IF(DATEDIFF(date_modified, date_published) > 0, id, NULL)) AS number_articles,
            'todamateria.com.br' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            posts
        WHERE
            published = 1
        GROUP BY
            YEAR(date_modified),
            MONTH(date_modified)
""",

    'juegosarea_com': f"""
       SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(game_id) AS number_articles,
            'juegosarea.com' AS product,
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
            'juegosarea.com' AS product,
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
            'juegosarea.com' AS product,
            'Categories' AS content_type,
            "" AS content_freshness
        FROM
            categories
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_created),
            MONTH(date_created)
""",
    'eutotal_com': f"""
       SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'eutotal.com' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, id, NULL)) AS number_articles,
            'eutotal.com' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
""",

    'ebiografia_com': f"""
     SELECT
            YEAR(data_publicacao) AS year,
            MONTH(data_publicacao) AS month,
            COUNT(id) AS number_articles,
            'ebiografia.com' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            artigos
        WHERE
            estado LIKE 'publicado'
        GROUP BY
            YEAR(data_publicacao),
            MONTH(data_publicacao)
        UNION ALL
        SELECT
            YEAR(data_atualizacao) AS year,
            MONTH(data_atualizacao) AS month,
            COUNT(IF(DATEDIFF(data_atualizacao, data_publicacao) > 0, id, NULL)) AS number_articles,
            'ebiografia.com' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            artigos
        WHERE
            estado LIKE 'publicado'
        GROUP BY
            YEAR(data_atualizacao),
            MONTH(data_atualizacao)
""",

    'significados_com': f"""
        SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'significados.com' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, id, NULL)) AS number_articles,
            'significados.com' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)

""",

    'techshake_com': f"""
       SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'techshake.com' AS product,
            'articles' AS content_type,
            'New content' AS content_freshness
        FROM
            articles
        WHERE 
            status = 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated,date_published) > 0, id, NULL)) AS number_articles,
            'techshake.com' AS product,
            'articles' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            articles 
        WHERE 
            status = 'online' AND date_updated IS NOT NULL
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
""",

    'sinonimosonline_com': f"""
        SELECT
            YEAR(dt) AS year,
            MONTH(dt) AS month,
            COUNT(id) AS number_articles,
            'sinonimosonline.com' AS product,
            'Word' AS content_type,
            IF(revisado = 0, 'New content', 'Update existing content') AS content_freshness
        FROM
            palavras
        GROUP BY
            YEAR(dt),
            MONTH(dt),
            IF(revisado = 0, 'New content', 'Update existing content')
""",

    'maioresemelhores_com': f"""
        SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'maioresemelhores.com' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, id, NULL)) AS number_articles,
            'maioresemelhores.com' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
        UNION ALL
        SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'maioresemelhores.com' AS product,
            'List' AS content_type,
            "New content" AS content_freshness
        FROM
            categories
        WHERE
            status = 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, id, NULL)) AS number_articles,
            'maioresemelhores.com' AS product,
            'List' AS content_type,
            "Update existing content" AS content_freshness
        FROM
            categories
        WHERE
            status = 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
""",

    'bibliaon_com_en': f"""
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, id, NULL)) AS number_articles,
            'bibliaon.com/en/' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
        UNION ALL
        SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'bibliaon.com/en/' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'bibliaon.com/en/' AS product,
            'Passagens' AS content_type,
            "" AS content_freshness
        FROM
            bible_passages
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
""",

    'ligadegamers_com': f"""
       SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'ligadegamers.com' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, id, NULL)) AS number_articles,
            'ligadegamers.com' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
""",

    'appgeek_com_br': f"""
       SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'appgeek.com.br' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, id, NULL)) AS number_articles,
            'appgeek.com.br' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
""",

    'todamateria_com': f"""
        SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'todamateria.com' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, id, NULL)) AS number_articles,
            'todamateria.com' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
""",

    'superaficionados_com': f"""
       SELECT
            YEAR(date_published) AS year,
            MONTH(date_published) AS month,
            COUNT(id) AS number_articles,
            'superaficionados.com' AS product,
            'Article' AS content_type,
            'New content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_published),
            MONTH(date_published)
        UNION ALL
        SELECT
            YEAR(date_updated) AS year,
            MONTH(date_updated) AS month,
            COUNT(IF(DATEDIFF(date_updated, date_published) > 0, id, NULL)) AS number_articles,
            'superaficionados.com' AS product,
            'Article' AS content_type,
            'Update existing content' AS content_freshness
        FROM
            articles
        WHERE
            status LIKE 'online'
        GROUP BY
            YEAR(date_updated),
            MONTH(date_updated)
""",

    'blipzi_com': f"""
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
                    """}
