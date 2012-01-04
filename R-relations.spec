%global packname  relations
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6
Release:          1%{?dist}
Summary:          Data Structures and Algorithms for Relations

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-sets 
Requires:         R-cluster R-stats R-slam 

BuildRequires:    R-devel tex(latex) R-sets
BuildRequires:    R-cluster R-stats R-slam 


%description
Data structures and algorithms for k-ary relations with arbitrary domains,
featuring relational algebra, predicate functions, and fitters for
consensus relations.

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
%doc %{rlibdir}/relations/html
%doc %{rlibdir}/relations/DESCRIPTION
%doc %{rlibdir}/relations/doc
%{rlibdir}/relations/NAMESPACE
%{rlibdir}/relations/po
%{rlibdir}/relations/data
%{rlibdir}/relations/Meta
%{rlibdir}/relations/R
%{rlibdir}/relations/INDEX
%{rlibdir}/relations/help
%{rlibdir}/relations/NEWS.Rd

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6-1
- initial package for Fedora