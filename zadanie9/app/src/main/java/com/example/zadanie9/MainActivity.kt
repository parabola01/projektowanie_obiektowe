package com.example.zadanie9

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class MainActivity : AppCompatActivity() {
    private lateinit var recyclerView: RecyclerView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        recyclerView = findViewById(R.id.recyclerView)
        recyclerView.layoutManager = LinearLayoutManager(this)

        val adapter = CategoryAdapter(DataProvider.categories) { category ->
            val intent = Intent(this, ProductListActivity::class.java)
            intent.putExtra("categoryId", category.id)
            startActivity(intent)
        }

        recyclerView.adapter = adapter
    }
}
