%global packname  VLMC
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.12
Release:          1%{?dist}
Summary:          VLMC -- Variable Length Markov Chains

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-12.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-MASS 

BuildRequires:    R-devel tex(latex) R-stats R-MASS 

%description
Functions, Classes & Methods for estimation, prediction, and simulation
(bootstrap) of VLMC -- Variable Length Markov Chain -- Models

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
%doc %{rlibdir}/VLMC/DESCRIPTION
%doc %{rlibdir}/VLMC/html
%{rlibdir}/VLMC/R
%{rlibdir}/VLMC/libs
%{rlibdir}/VLMC/data
%{rlibdir}/VLMC/NAMESPACE
%{rlibdir}/VLMC/help
%{rlibdir}/VLMC/Meta
%{rlibdir}/VLMC/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.12-1
- initial package for Fedora