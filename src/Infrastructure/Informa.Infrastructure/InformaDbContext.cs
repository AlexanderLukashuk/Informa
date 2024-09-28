using Informa.Application.Interfaces;
using Informa.Domain.Models;
using Microsoft.EntityFrameworkCore;

namespace Informa.Infrastructure;

public class InformaDbContext : DbContext, IInformaDbContext
{
    public DbSet<NewsArticle> NewsArticles { get; set; }

    public InformaDbContext(DbContextOptions<InformaDbContext> options)
        : base(options) { }
}