%global packname  GEOmetadb
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.14.2
Release:          1%{?dist}
Summary:          A compilation of metadata from NCBI GEO

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-GEOquery R-RSQLite 


BuildRequires:    R-devel tex(latex) R-GEOquery R-RSQLite



%description
The NCBI Gene Expression Omnibus (GEO) represents the largest public
repository of microarray data. However, finding data of interest can be
challenging using current tools. GEOmetadb is an attempt to make access to
the metadata associated with samples, platforms, and datasets much more
feasible. This is accomplished by parsing all the NCBI GEO metadata into a
SQLite database that can be stored and queried locally. GEOmetadb is
simply a thin wrapper around the SQLite database along with associated
documentation. Finally, the SQLite database is updated regularly as new
data is added to GEO and can be downloaded at will for the most up-to-date
metadata. GEOmetadb paper:
http://bioinformatics.oxfordjournals.org/cgi/content/short/24/23/2798 .

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.14.2-1
- initial package for Fedora