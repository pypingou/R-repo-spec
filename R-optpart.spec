%global packname  optpart
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          Optimal partitioning of similarity relations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-cluster R-labdsv R-MASS R-plotrix 

BuildRequires:    R-devel tex(latex) R-cluster R-labdsv R-MASS R-plotrix 

%description
The package contains a set of algorithms for creating partitions and
coverings of objects largely based on operations on similarity relations
(or matrices). There are several iterative re-assigmnent algorithms
optimizing different goodness-of-clustering criteria.  In addition, there
are covering algorithms "clique" which derives maximal cliques, and
"maxpact" which creates a covering of maximally compact sets. Graphical
analyses and conversion routines are also included.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.1-1
- initial package for Fedora