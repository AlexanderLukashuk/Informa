using Informa.Domain.Models;
using Microsoft.EntityFrameworkCore;

namespace Informa.Application.Interfaces;

public interface IInformaDbContext
{
    DbSet<NewsArticle> NewsArticles { get; set; }

    Task<int> SaveChangesAsync(CancellationToken cancellationToken);
}