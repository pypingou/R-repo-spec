%global packname  TSP
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          Traveling Salesperson Problem (TSP)

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Basic infrastructure and some algorithms for the traveling salesperson
problem (also traveling salesman problem; TSP). The package provides some
simple algorithms and an interface to Concorde, the currently fastest TSP
solver. Concorde itself is not included in the package and has to be
obtained separately.

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
%doc %{rlibdir}/TSP/DESCRIPTION
%doc %{rlibdir}/TSP/CITATION
%doc %{rlibdir}/TSP/doc
%doc %{rlibdir}/TSP/html
%{rlibdir}/TSP/data
%{rlibdir}/TSP/libs
%{rlibdir}/TSP/INDEX
%{rlibdir}/TSP/help
%{rlibdir}/TSP/Meta
%{rlibdir}/TSP/LICENSE
%{rlibdir}/TSP/NAMESPACE
%{rlibdir}/TSP/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.5-1
- initial package for Fedora