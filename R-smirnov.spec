%global packname  smirnov
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Provides two taxonomic coefficients from E. S. Smirnov "Taxonomic analysis" (1969) book

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This tiny package contains one function smirnov() which calculates two
scaled taxonomic coefficients, Txy (coefficient of similarity) and Txx
(coefficient of originality). These two characteristics may be used for
the analysis of similarities between any number of taxonomic groups, and
also for assessing uniqueness of giving taxon. It is possible to use
smirnov() output as a distance measure: convert it to distance by
"as.dist(1 - smirnov(x))".

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
%doc %{rlibdir}/smirnov/html
%doc %{rlibdir}/smirnov/DESCRIPTION
%{rlibdir}/smirnov/INDEX
%{rlibdir}/smirnov/Meta
%{rlibdir}/smirnov/R
%{rlibdir}/smirnov/NAMESPACE
%{rlibdir}/smirnov/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora