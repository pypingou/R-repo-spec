%global packname  parfossil
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Parallelized functions for palaeoecological and palaeogeographical analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-fossil R-foreach 

BuildRequires:    R-devel tex(latex) R-fossil R-foreach 

%description
The package provides a number of easily parallelized functions from the
fossil package. This package is designed to be used with some type of
parallel computing backend, such as multicore, snow or MPI.

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
%doc %{rlibdir}/parfossil/html
%doc %{rlibdir}/parfossil/CITATION
%doc %{rlibdir}/parfossil/DESCRIPTION
%{rlibdir}/parfossil/R
%{rlibdir}/parfossil/Meta
%{rlibdir}/parfossil/help
%{rlibdir}/parfossil/INDEX

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.0-1
- initial package for Fedora